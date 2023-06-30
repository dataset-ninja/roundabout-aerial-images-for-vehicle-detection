import os
import shutil
import xml.etree.ElementTree as ET

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import get_file_name
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_ds_path: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    file_info = api.file.get_info_by_path(team_id, teamfiles_ds_path)
    file_name_with_ext = file_info.name
    local_path = os.path.join(storage_dir, file_name_with_ext)
    dataset_path = os.path.splitext(local_path)[0]

    if not os.path.exists(dataset_path):
        sly.logger.info(f"Dataset dir '{dataset_path}' does not exist.")
        if not os.path.exists(local_path):
            sly.logger.info(f"Downloading archive '{teamfiles_ds_path}'...")
            api.file.download(team_id, teamfiles_ds_path, local_path)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        path = unpack_if_archive(local_path)
        sly.logger.info(f"Archive '{file_name_with_ext}' was unpacked successfully to: '{path}'.")
        sly.logger.info(f"Dataset dir contains: '{os.listdir(path)}'.")
        sly.fs.silent_remove(local_path)

    else:
        sly.logger.info(
            f"Archive '{file_name_with_ext}' was already unpacked to '{dataset_path}'. Skipping..."
        )
    return dataset_path


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    teamfiles_dir = "/4import/Roundabout Aerial Images for Vehicle Detection/archive.zip"
    dataset_path = download_dataset(teamfiles_dir)

    images_folder = "original/original/imgs"
    annotations_folder = "original/original/annotations"
    ann_ext = ".xml"
    batch_size = 30

    def _create_ann(image_path, name_to_class):
        labels = []
        tags = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        ann_folder = os.path.join(dataset_path, annotations_folder)
        ann_name = get_file_name(image_path) + ann_ext

        ann_path = os.path.join(ann_folder, ann_name)

        tree = ET.parse(ann_path)
        root = tree.getroot()

        ann_objects = root.findall(".//object")
        for curr_object in ann_objects:
            obj_class_name = curr_object[0].text
            if obj_class_name not in name_to_class:
                new_obj_class = sly.ObjClass(name=obj_class_name, geometry_type=sly.Rectangle)
                name_to_class[obj_class_name] = new_obj_class
                meta = sly.ProjectMeta.from_json(api.project.get_meta(project.id))
                meta = meta.add_obj_class(new_obj_class)
                api.project.update_meta(project.id, meta.to_json())
                sly.logger.info(f"Added new class: {new_obj_class.name}")
            obj_class = name_to_class[obj_class_name]
            left = int(curr_object[4][0].text)
            top = int(curr_object[4][1].text)
            right = int(curr_object[4][2].text)
            bottom = int(curr_object[4][3].text)

            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            label = sly.Label(rect, obj_class)
            labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    name_to_class = {}
    project = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta()

    ds_name = "ds0"
    dataset = api.dataset.create(project.id, ds_name)

    images_path = os.path.join(dataset_path, images_folder)
    images = os.listdir(images_path)

    progress = tqdm(desc="Create dataset {}".format(ds_name), total=len(images))
    for batch_names in sly.batched(images, batch_size=batch_size):
        image_paths = [os.path.join(images_path, image_name) for image_name in batch_names]
        image_infos = api.image.upload_paths(dataset.id, batch_names, image_paths)
        img_ids = [im_info.id for im_info in image_infos]

        anns = [_create_ann(image_path, name_to_class) for image_path in image_paths]
        api.annotation.upload_anns(img_ids, anns)

        progress.update(len(batch_names))

    sly.logger.info("Deleting temporary app storage files...")
    shutil.rmtree(dataset_path)

    return project

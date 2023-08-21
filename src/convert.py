# https://www.kaggle.com/datasets/javiersanchezsoriano/roundabout-aerial-images-for-vehicle-detection

import csv
import os
from collections import defaultdict

import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import get_file_name, get_file_name_with_ext

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "Roundabout Aerial Images"
    dataset_path = "APP_DATA/archive"
    batch_size = 30
    ds_name = "ds"

    images_folder = "original/original/imgs"
    annotations_file = "data.csv"
    tags_data_name = "roundabouts.csv"
    img_height = 1080
    img_wight = 1920

    def create_ann(image_path):
        labels = []

        file_name = get_file_name(image_path)

        image_data = name_to_data.get(file_name)
        if image_data is not None:
            for curr_image_data in image_data:
                obj_class = meta.get_obj_class(curr_image_data[1])
                if obj_class is None:
                    continue
                bboxes = list(map(int, curr_image_data[0]))

                left = bboxes[0]
                top = bboxes[1]
                right = bboxes[2]
                bottom = bboxes[3]
                rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
                label = sly.Label(rect, obj_class)
                labels.append(label)

        scene = file_name.split("_")[0]
        tag_data = scene_to_tags[scene]
        id_roundabout = sly.Tag(tag_id, value=int(tag_data[0]))
        lat = sly.Tag(tag_lat, value=float(tag_data[1]))
        long_ = sly.Tag(tag_long, value=float(tag_data[2]))
        height = sly.Tag(tag_height, value=int(tag_data[3]))
        zoom = sly.Tag(tag_zoom, value=int(tag_data[4]))

        return sly.Annotation(
            img_size=(img_height, img_wight),
            labels=labels,
            img_tags=[id_roundabout, lat, long_, height, zoom],
        )

    obj_class_car = sly.ObjClass("car", sly.Rectangle)
    obj_class_cycle = sly.ObjClass("cycle", sly.Rectangle)
    obj_class_truck = sly.ObjClass("truck", sly.Rectangle)
    obj_class_bus = sly.ObjClass("bus", sly.Rectangle)

    tag_id = sly.TagMeta("id roundabout", sly.TagValueType.ANY_NUMBER)
    tag_lat = sly.TagMeta("lat", sly.TagValueType.ANY_NUMBER)
    tag_long = sly.TagMeta("long", sly.TagValueType.ANY_NUMBER)
    tag_height = sly.TagMeta("height", sly.TagValueType.ANY_NUMBER)
    tag_zoom = sly.TagMeta("height with zoom", sly.TagValueType.ANY_NUMBER)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class_car, obj_class_cycle, obj_class_truck, obj_class_bus],
        tag_metas=[tag_id, tag_lat, tag_long, tag_height, tag_zoom],
    )
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_path = os.path.join(dataset_path, images_folder)
    anns_path = os.path.join(dataset_path, annotations_file)
    tags_data_path = os.path.join(dataset_path, tags_data_name)

    name_to_data = defaultdict(list)
    with open(anns_path, "r") as file:
        csvreader = csv.reader(file)
        for idx, row in enumerate(csvreader):
            if idx != 0:
                name_to_data[get_file_name(row[0])].append((row[1:-1], row[-1]))

    scene_to_tags = {}
    with open(tags_data_path, "r") as file:
        csvreader = csv.reader(file)
        for idx, row in enumerate(csvreader):
            if idx != 0:
                scene_to_tags[get_file_name(row[0])] = row[1:]

    images_names = os.listdir(images_path)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in images_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(images_names_batch))
    return project

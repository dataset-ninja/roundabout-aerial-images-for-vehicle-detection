from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Roundabout Aerial Images"
PROJECT_NAME_FULL: str = "Roundabout Aerial Images for Vehicle Detection"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Domain.VehicleDetection()]
CATEGORY: Category = Category.Aerial(extra=Category.Drones())

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2022

HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/javiersanchezsoriano/roundabout-aerial-images-for-vehicle-detection"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 2143961
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/roundabout-aerial-images-for-vehicle-detection"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/datasets/javiersanchezsoriano/roundabout-aerial-images-for-vehicle-detection/download?datasetVersionNumber=2"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "car": [230, 25, 75],
    "cycle": [60, 180, 75],
    "truck": [255, 225, 25],
    "bus": [0, 130, 200],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://www.mdpi.com/2306-5729/7/4/47"
CITATION_URL: Optional[str] = "https://doi.org/10.3390/data7040047"
AUTHORS: Optional[List[str]] = [
    "Enrique Puertas",
    "Gonzalo De-Las-Heras",
    "Javier Fernández-Andrés",
    "Javier Sánchez-Soriano",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["javier.fernandez@universidadeuropea.es"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Universidad Europea de Madrid",
    "SICE Canada Inc., Toronto",
    "Universidad Francisco de Vitoria, Spain",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://universidadeuropea.com/conocenos/madrid/",
    "https://www.sice.com/en",
    "https://www.ufv.es/",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    "__POSTTEXT__": "Additionally, the meta data about ***roundabout id*** (8 unique roundabouts), Drone's ***lattitude*** and ***longitude***, its ***height*** of exposure and ***height with zoom*** is provided"
}
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings

Dataset **Roundabout Aerial Images** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE1ODFfUm91bmRhYm91dCBBZXJpYWwgSW1hZ2VzL3JvdW5kYWJvdXQtYWVyaWFsLWltYWdlcy1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJGVXNKRkp3cFRYdVhBeE5UK3BVQU4yUm1FeWlCOXAxNFkzdmpqUzNKNzM4PSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Roundabout Aerial Images', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/javiersanchezsoriano/roundabout-aerial-images-for-vehicle-detection/download?datasetVersionNumber=2).
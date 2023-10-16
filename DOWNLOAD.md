Dataset **Roundabout Aerial Images** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/p/r/MY/lQ3dZ5syJJO4JpOayUpctkwDbycQ1bIqwp8uniFZdLMwaNmDemmJaUWJbzrwOdT62jBNk0CoT835KMXqrC6M3UsILTAzRq0pbSYTHTV0dnBpPNK7pZdakKMPN3Il.tar)

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
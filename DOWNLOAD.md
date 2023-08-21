Dataset **Roundabout Aerial Images** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/g/y/5A/4KZL5Foi3RItbm4va03k3fWmVs4GV7O3ZFlg0oiaxXMDA4YZmha2FSR9FtThyE06Whr9SesZBROW8XPj8KXictBZmJhU90KbrX3ph3rxG3aoPafBeiHKASQunBzy.tar)

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
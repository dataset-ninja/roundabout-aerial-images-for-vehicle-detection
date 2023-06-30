Dataset **Roundabout Aerial Images** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/P/n/WH/baNNM10hjKmymxAHSdTgmeGV287RYhZWypGn1EXCFAfbQgslFUCeNjACm81w9cDpjSOCutB7n5DKZzoONLHEv0YbEWrDBukQhFWb75DKNiqlRpOwA9uES1J9xID3.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Roundabout Aerial Images', dst_path='~/dtools/datasets/Roundabout Aerial Images.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/javiersanchezsoriano/roundabout-aerial-images-for-vehicle-detection/download?datasetVersionNumber=2)
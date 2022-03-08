import joblib
from google.cloud import storage
import os

from ObjectivelyFunny import cloud_paths

def download_model(model_name="LSTM", rm=True):

    client = storage.Client().bucket(cloud_paths.BUCKET_NAME)
    storage_location = f'{cloud_paths.STORAGE_LOCATION}{model_name}.joblib'
    blob = client.blob(storage_location)
    blob.download_to_filename('model.joblib')
    print("=> model downloaded from storage")
    model = joblib.load('model.joblib')
    if rm:
        os.remove('model.joblib')
    return model

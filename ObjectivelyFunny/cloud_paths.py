BUCKET_NAME = 'wagon-data-805-melbardis'
BUCKET_DATA_PATH = 'obj-fun-data/'
STORAGE_LOCATION = 'models/obj-fun/model.joblib'

PATH_TO_DATA = f"gs://{BUCKET_NAME}/{BUCKET_DATA_PATH}"
PATH_TO_LOCAL_MODEL = 'model.joblib'
PATH_TO_GCP_MODEL = f"gs://{BUCKET_NAME}/{STORAGE_LOCATION}"

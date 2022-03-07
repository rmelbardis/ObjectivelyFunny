BUCKET_NAME = 'wagon-data-805-melbardis'
BUCKET_DATA_PATH = 'obj-fun-data'
DATA_NAME = 'fully_stripped_df_bo.json'
STORAGE_LOCATION = 'models/obj-fun/model.joblib'

PATH_TO_DATA = f"gs://{BUCKET_NAME}/{BUCKET_DATA_PATH}/{DATA_NAME}"
PATH_TO_LOCAL_MODEL = 'model.joblib'
PATH_TO_GCP_MODEL = f"gs://{BUCKET_NAME}/{STORAGE_LOCATION}"

JAMES_BUCKET_NAME = 'wagon-data-805-farrell'
BUCKET_NAME = 'wagon-data-805-melbardis'
BUCKET_DATA_PATH = 'obj-fun-data'
DATA_NAME = 'fully_stripped_df_bo.json'
STORAGE_LOCATION = 'models/obj-fun/'

PATH_TO_DATA = f"gs://{JAMES_BUCKET_NAME}/{BUCKET_DATA_PATH}/{DATA_NAME}"
PATH_TO_GCP_MODEL = f"gs://{JAMES_BUCKET_NAME}/{STORAGE_LOCATION}"

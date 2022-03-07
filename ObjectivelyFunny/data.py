import pandas as pd

from ObjectivelyFunny import cloud_paths

def get_data():
    """method to get the data from google cloud bucket"""
    df = pd.read_json(cloud_paths.PATH_TO_DATA)
    return df


# if __name__ == '__main__':
#     df = get_data()
#     print(df.head())

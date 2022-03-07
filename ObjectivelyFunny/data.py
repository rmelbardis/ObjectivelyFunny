import pandas as pd

from ObjectivelyFunny import cloud_paths

def get_data():
    """method to get the data from google cloud bucket"""
    df = pd.read_json(cloud_paths.PATH_TO_DATA)
    return df

def get_small_data():
    """method to get data from google cloud, then transform"""
    df = get_data() # get data
    df = df[df['artist']=='Bill Burr'].reset_index(drop=True) # create subset of data
    return df

def create_sequences(word_list, min_length, max_length):
    sequences = []
    for i in range(len(word_list)):
        if i in range(min_length):
            pass
        elif i in range(min_length, max_length):
            seq = word_list[:i]
            sequences.append(seq)
        else:
            seq = word_list[i-max_length:i]
            sequences.append(seq)
    return sequences

# if __name__ == '__main__':
#     df = get_small_data()
#     print(df.head())

import pandas as pd

from ObjectivelyFunny import cloud_paths

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

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

def get_X_y_vocab(X, seq_length):
    '''
    Usage : "X, y, vocab_size, X_seq_length = get_X_y_vocab_seqlength(df)"

    Takes list of sequence lists from a dataframe column called 'sequences'
    and applies the following:
      - transforms the column into a single list of lists
      - Tokenizes the words into integers
      - Applies default padding to seq_length
      - Transforms y into categorical
    '''
    # create single list of sequences
    sequence_list = list(X['sequences'].explode())

    # tokenize
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(sequence_list)
    sequences = tokenizer.texts_to_sequences(sequence_list)

    # padding
    sequences_pad = pad_sequences(sequences, maxlen=seq_length, padding='pre', dtype='int')

    # output creation
    vocab_size = len(tokenizer.word_index) + 1
    X, y = sequences_pad[:,:-1], sequences_pad[:,-1]
    y = to_categorical(y, num_classes=vocab_size)
    X_seq_length = X.shape[1]

    return X, y, vocab_size, X_seq_length

# if __name__ == '__main__':
#     df = get_small_data()
#     print(df.head())

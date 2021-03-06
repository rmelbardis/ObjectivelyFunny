import pandas as pd

from ObjectivelyFunny import cloud_paths

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from gensim.utils import simple_preprocess

def get_data(gender=None, age=None, artist=None, year=None, show_name=None):
    """method to get data from google cloud, then transform"""
    df = pd.read_json(cloud_paths.PATH_TO_DATA) # get data from Google Cloud

    if gender:
        df = df[df['artist_gender'].isin(gender)].reset_index(drop=True) # create subset of data
    if age:
        df = df[df['age_then'].isin(age)].reset_index(drop=True)
    if artist:
        df = df[df['artist'].isin(artist)].reset_index(drop=True)
    if year:
        df = df[df['year'].isin(year)].reset_index(drop=True)
    if show_name:
        df = df[df['show_name'].isin(show_name)].reset_index(drop=True)
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

def get_X_y_vocab_seqlength(X, seq_length):
    '''
    Usage : "X, y, vocab_size, X_seq_length = get_X_y_vocab_seqlength(df, seq_length)"

    Takes list of sequence lists from a dataframe column called 'sequences',
    and required length of X+y sequences.

    Applies the following:
      - transforms the column into a single list of lists
      - Tokenizes the words into integers
      - Applies default padding to seq_length
      - splits each sequence into X = all but the last word and y = last word
      - Transforms y into categorical for prediction
      - updates sequence length to just be the X sequence
      - outputs X, y, vocab_size and X_seq_length
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

def sent_to_words(sentences):
    for sentence in sentences:
        yield(simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

# if __name__ == '__main__':
#     df = get_small_data()
#     print(df.head())

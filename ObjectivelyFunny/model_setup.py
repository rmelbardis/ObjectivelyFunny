# imports
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin

from ObjectivelyFunny.data import create_sequences

class WordSplitter(BaseEstimator, TransformerMixin):
    '''
    Splits full_transcript into 'full_words' using .split()
    Then creates a new columns called 'num_words' that counts the 'full_words'
    '''
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['full_words'] = X['full_transcript'].str.split()
        X['num_words'] = X['full_words'].str.len()
        return pd.DataFrame(X)

class Sequencer(BaseEstimator, TransformerMixin):
    '''
    From 'full_words', creates 'sequences' column -
    list of lists of sequences of consecutive words from min_length to max_length
    '''
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['sequences'] = X['full_words'].apply(create_sequences, args=(self.min_length, self.max_length))
        return pd.DataFrame(X)

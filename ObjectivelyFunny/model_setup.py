# imports
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


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

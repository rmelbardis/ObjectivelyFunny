import string
import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.base import BaseEstimator, TransformerMixin


class MusicRemover(BaseEstimator, TransformerMixin):
    '''
    Removes fragments in notes (default '♫♪')
    pass notes argument as string to function for alternative list
    '''
    def __init__(self, notes='♫♪'):
        self.notes = notes

     def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        for note in self.notes:
            X = X.apply(
            lambda x: re.sub(f'{note}.*?{note}', '', x))
        return X

class RegexRemover(BaseEstimator, TransformerMixin):

    def __init__(self, precision=6):
        self.precision = precision

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        assert isinstance(X, pd.DataFrame)
        X['geohash_pickup'] = X.apply(
            lambda x: gh.encode(x.pickup_latitude, x.pickup_longitude, precision=self.precision), axis=1)
        X['geohash_dropoff'] = X.apply(
            lambda x: gh.encode(x.dropoff_latitude, x.dropoff_longitude, precision=self.precision), axis=1)
        return X[['geohash_pickup', 'geohash_dropoff']]

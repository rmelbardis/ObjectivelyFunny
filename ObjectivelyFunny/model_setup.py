# imports
import string
import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.base import BaseEstimator, TransformerMixin

# nltk downloads
from nltk import download
download('punkt')


class WordSplitter(BaseEstimator, TransformerMixin):
    '''
    Removes fragments in notes list (default ['♫', '♪'])
    pass notes argument as list to function for alternative list
    '''
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['full_words'] = X['full_transcript'].str.split()
        X['num_words'] = X['full_words'].str.len()
        return pd.DataFrame(X)

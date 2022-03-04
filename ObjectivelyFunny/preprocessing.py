import string
import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.base import BaseEstimator, TransformerMixin


class MusicRemover(BaseEstimator, TransformerMixin):
    '''
    Removes fragments in notes list (default ['♫', '♪'])
    pass notes argument as list to function for alternative list
    '''
    def __init__(self, notes=['♫', '♪']):
        self.notes = notes

     def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        for note in self.notes:
            X = X.apply(
            lambda x: re.sub(f'{note}.*?{note}', '', x))
        return X

class BracketRemover(BaseEstimator, TransformerMixin):
    '''
    Removes fragments in [] and () brackets
    set square=False or round=False to keep one or the other
    '''
    def __init__(self, square=True, round=True):
        self.square = square
        self.round = round

     def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        if self.square:
            X = X.apply(
            lambda x: re.sub('\[.*?\]', '', x))
        if self.round:
            X = X.apply(
            lambda x: re.sub('\(.*?\)', '', x))
        return X

class RegexRemover(BaseEstimator, TransformerMixin):
    '''
    Class to remove common regex from comedy transcripts that are not the comedian's words
    Params:
    speaker (default=True) - removes ' word: or word word:'
    ---fill rest out---
    '''
    def __init__(self,
                 speaker=True, subtitles=True, netflix=True,
                 strong=True, adult=True, air_date=True):
        self.speaker = speaker
        self.subtitles = subtitles
        self.netflix = netflix
        self.strong = strong
        self.adult = adult
        self.air_date = air_date

     def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        if self.speaker:
            X = X.apply(
            lambda x: re.sub('\s[\w-]+( \w+)?:\s', '', x))
        if self.subtitles:
            X = X.apply(
            lambda x: re.sub('subtitle(s)? by .*', '', x))
        if self.netflix:
            X = X.apply(
            lambda x: re.sub('(a)? netflix (original )?(comedy )?(special ?)?', '', x))
        if self.strong:
            X = X.apply(
            lambda x: re.sub('(this )?(programme )?(contains )?(very |some )?strong language( |\.)', '', x))
        if self.adult:
            X = X.apply(
            lambda x: re.sub('adult humou?r( |\.?)?', '', x))
        if self.air_date:
            X = X.apply(
            lambda x: re.sub('(original )?air date', '', x))
        return X

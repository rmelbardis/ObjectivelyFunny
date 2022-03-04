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
    Only works on lowercase text
    Params (all Boolean and default=True):
    speaker - removes ' word: or word word:'
    subtitles - removes 'subtitles by ' and everything after up to newline
    netflix - removes variants of 'a netflix original comedy special'
    strong - removes variants of 'this programme contains strong language'
    adult - removes 'adult humour'
    air_date - removes variants of 'original air date'
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

class LowerCase(BaseEstimator, TransformerMixin):
    '''
    Turns text into lowercase text
    '''
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X.str.lower()

class NumRemover(BaseEstimator, TransformerMixin):
    '''
    Removes digits from text
    '''
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.apply(
            lambda x: ''.join(char for char in x if not char.isdigit()))
        return X

class Tokenizer(BaseEstimator, TransformerMixin):
    '''
    Applies the word_tokenizer
    '''
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.apply(
            lambda x: ''.join(char for char in x if not char.isdigit()))
        return X

class Replacer(BaseEstimator, TransformerMixin):
    '''
    Transforms words into other words
    Takes word_dict as a dictionary of {'new word': [list of 'old words'] / 'old word'}
    Outputs the text with each set of values replaced by the key
    '''
    def __init__(self, word_dict):
        self.word_dict = word_dict

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        for k, v in self.word_dict.items():
            if type(v) == str:
                X = X.str.replace(v, k)
            elif:
                for word in v:
                    X = X.str.replace(word, k)
        return X

class PuncRemover(BaseEstimator, TransformerMixin):
    '''
    Removes punctuation from text
    Takes chars (default='“”‘’…♪♫¶') as an optional parameter which is added to the standard string.punctuation string.
    '''
    def __init__(self, extra_chars='“”‘’…♪♫¶'):
        self.extra_chars = extra_chars
        self.punctuation = string.punctuation + self.extra_chars
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        for punc in self.punctuation:
            X = X.str.replace(punc, '')
        return X

class WordRemover(BaseEstimator, TransformerMixin):
    '''
    Removes words from text
    Parameters:
    word_list - list of custom words that need to be removed
    stopwords - Boolean (default=True) - flag on whether to remove the standard nltk english stopwords list
    '''
    def __init__(self, word_list, stopwords=True):
        self.word_list = word_list
        self.stopwords = stopwords

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        def remove_stopw(text, _lst):
            word_tokens = word_tokenize(text)
            return ' '.join(w for w in word_tokens if not w in _lst)
        X = X.apply(remove_stopw, args=(self.word_list,))
        if self.stopwords:
            X = X.apply(remove_stopw, args=(stopwords.words('english'),))
        return X

class Lemmatizer(BaseEstimator, TransformerMixin):
    '''
    Performs standard lemmatizing on words and removes words that are shorter than 3 characters
    '''
    def __init__(self, word_list, stopwords=True):
    self.word_list = word_list
    self.stopwords = stopwords

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        lemmatizer = WordNetLemmatizer()
        X = X.apply(
            lambda x: ' '.join(lemmatizer.lemmatize(word) for word in x.split(' ')
                               if len(lemmatizer.lemmatize(word))>2)
        return X

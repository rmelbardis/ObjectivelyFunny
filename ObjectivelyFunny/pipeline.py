from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer

from ObjectivelyFunny import preprocessing
from ObjectivelyFunny import word_selections

def set_pipeline(include_steps,
                swearing_dict = word_selections.swearing_dict,
                lemmatizer_dict = word_selections.lemmatizer_dict,
                dropword_list = word_selections.standard_dropword_list,
                seq_min_length = 10, seq_max_length = 21):
    '''
    create pipeline for preprocessing

    possible include_steps list:
    ['music', 'brackets', 'regex', 'lowercase', 'numbers', 'uncensor', 'punctuation',
    'lemmatizer', 'manual_lemmatize', 'remove', 'split_words', 'sequences']

    has standard swearing_dict, lemmatizer_dict and dropword_list by default, but - these can be changed
    '''
    blocks = {
            'music': ('music', preprocessing.MusicRemover()),
            'brackets': ('brackets', preprocessing.BracketRemover()),
            'lowercase': ('lowercase', preprocessing.LowerCase()),
            'regex': ('regex', preprocessing.RegexRemover()),
            'numbers': ('numbers', preprocessing.NumRemover()),
            'uncensor': ('uncensor', preprocessing.Replacer(swearing_dict)),
            'punctuation': ('punctuation', preprocessing.PuncRemover()),
            'lemmatizer': ('lemmatizer', preprocessing.Lemmatizer()),
            'manual_lemmatize': ('manual_lemmatize', preprocessing.Replacer(lemmatizer_dict)),
            'remove': ('remove', preprocessing.WordRemover(dropword_list)),
            'remove2': ('remove2', preprocessing.WordRemover(dropword_list)),
            'split_words': ('split_words', preprocessing.WordSplitter()),
            'sequences': ('sequences', preprocessing.Sequencer(seq_min_length, seq_max_length))
        }

    incl_blocks = [blocks[bloc] for bloc in include_steps]

    pipe = Pipeline(incl_blocks)

    return pipe

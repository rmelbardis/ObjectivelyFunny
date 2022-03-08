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
    'lemmatizer', 'manual_lemmatizer', 'remove', 'split_words', 'sequences']

    has standard swearing_dict, lemmatizer_dict and dropword_list by default, but - these can be changed
    '''
    blocks = [
            ('music', preprocessing.MusicRemover()),
            ('brackets', preprocessing.BracketRemover()),
            ('lowercase', preprocessing.LowerCase()),
            ('regex', preprocessing.RegexRemover()),
            ('numbers', preprocessing.NumRemover()),
            ('uncensor', preprocessing.Replacer(swearing_dict)),
            ('punctuation', preprocessing.PuncRemover()),
            ('lemmatizer', preprocessing.Lemmatizer()),
            ('manual_lemmatize', preprocessing.Replacer(lemmatizer_dict)),
            ('remove', preprocessing.WordRemover(dropword_list)),
            ('split_words', preprocessing.WordSplitter()),
            ('sequences', preprocessing.Sequencer(seq_min_length, seq_max_length))
        ]

    incl_blocks = []
    for bloc in blocks:
            if bloc[0] in include_steps:
                incl_blocks.append(bloc)

    pipe = Pipeline(incl_blocks)

    return pipe

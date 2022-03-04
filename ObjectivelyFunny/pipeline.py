from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer

from ObjectivelyFunny import preprocessing

def set_pipeline():
    '''
    create pipeline
    '''
    include_steps = ['music']
    # re-institute swearing
    swearing_dict = {}

    # lemmatizer dictionary
    lemmatizer_dict = {}

    # words to drop
    word_list = []

    blocks = [
            ('music', preprocessing.MusicRemover()),
            ('brackets', preprocessing.BracketRemover()),
            ('lowercase', preprocessing.LowerCase()),
            ('numbers', preprocessing.NumRemover()),
            ('uncensor', preprocessing.Replacer(swearing_dict)),
            ('punctuation', preprocessing.PuncRemover()),
            ('lemmatizer', preprocessing.Lemmatizer),
            ('manual_lemmatizer', preprocessing.Replacer(lemmatizer_dict)),
            ('remove', preprocessing.WordRemover(word_list)),
        ]

    for bloc in blocks:
            if bloc[0] not in include_steps:
                blocks.remove(bloc)

    preprocessor_pipe = Pipeline(blocks)
    transformer = ColumnTransformer(('preprocess_full', preprocessor_pipe, 'full_transcript'),
                                          remainder="drop")

    return transformer

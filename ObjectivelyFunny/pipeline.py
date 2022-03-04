from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer

from ObjectivelyFunny import preprocessing

def set_pipeline(include_steps,
                swearing_dict = {
                    'fuck': ['fucking', 'f*ck', 'f_ck', 'f**k', 'f***'],
                    'bitch': ['b*tch', 'b_tch', 'b****', 'b**ch', 'b***h'],
                    'shit': ['sh*t', 'sh_t', 's**t', 's***']},
                lemmatizer_dict = {
                    'get': 'got',
                    'go': 'gon',
                    'say': 'said',
                    'go': 'went',
                    'find': 'finding'},
                dropword_list = [
                'thank', 'cheering', 'recorded', 'applause', 'laughter', 'laughing', 'murmuring', 'chatter',
                'aired', 'filmed', 'ladies', 'gentlemen', 'welcome', 'stage', 'transcript', 'netflix',
                'apollo', 'like', 'goodnight', 'mutter', 'noo', 'nuh', 'oof', 'maan', 'cause', 'okay',
                'hey', 'also', 'someone', 'somebody', 'everybody', 'also', 'part' , 'sometimes', 'maybe',
                'three', 'second', 'everything', 'minute', 'name', 'kind', 'point', 'yeah', 'hello', 'one',
                'two', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'whine', 'hnn', 'malla', 'letta',
                'namoo', 'getta', 'nama', 'mana', 'chk','manoo', 'hadda', 'ama', 'carlin',
                'go', 'know', 'host', 'goodnight', 'get', 'gon', 'think', 'say', 'right', 'look',
                'thing', 'make', 'know', 'want', 'going', 'would', 'could', 'gentlemen', 'let', 'please',
                'hbo', 'special' 'yes', 'take', 'say', 'got', 'come', 'see', 'really', 'tell',
                'well', 'give', 'said'])
    '''
    create pipeline for preprocessing

    possible include_steps list:
    ['music', 'brackets', 'lowercase', 'numbers', 'uncensor', 'punctuation',
    'lemmatizer', 'manual_lemmatizer', 'remove']

    has standard swearing_dict, lemmatizer_dict and dropword_list by default, but - these can be changed
    '''
    blocks = [
            ('music', preprocessing.MusicRemover()),
            ('brackets', preprocessing.BracketRemover()),
            ('lowercase', preprocessing.LowerCase()),
            ('numbers', preprocessing.NumRemover()),
            ('uncensor', preprocessing.Replacer(swearing_dict)),
            ('punctuation', preprocessing.PuncRemover()),
            ('lemmatizer', preprocessing.Lemmatizer),
            ('manual_lemmatizer', preprocessing.Replacer(lemmatizer_dict)),
            ('remove', preprocessing.WordRemover(dropword_list)),
        ]

    for bloc in blocks:
            if bloc[0] not in include_steps:
                blocks.remove(bloc)

    preprocessor_pipe = Pipeline(blocks)
    transformer = ColumnTransformer(('preprocess_full', preprocessor_pipe, 'full_transcript'),
                                          remainder="drop")

    return transformer

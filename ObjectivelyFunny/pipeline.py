from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer

from ObjectivelyFunny import preprocessing
import ipdb

def set_pipeline(include_steps,
                swearing_dict = {
                    "fuck": [r"fucking", r"f\*ck", r"f_ck", r"f\*\*k", r"f\*\*\*"],
                    "bitch": [r"b\*tch", r"b_tch", r"b\*\*\*\*", r"b\*\*ch", r"b\*\*\*h"],
                    "shit": [r"sh\*t", r"sh_t", r"s\*\*t", r"s\*\*\*"]},
                lemmatizer_dict = {
                    'get': 'got',
                    'go': 'gon',
                    'say': 'said',
                    'go': 'went',
                    'find': 'finding'},
                dropword_list = [
                'thank', 'cheering', 'recorded', 'applause', 'laughter', 'laughing', 'murmuring', 'chatter',
                'aired', 'filmed', 'ladies', 'gentlemen', 'lady', 'gentleman', 'welcome', 'stage', 'transcript', 'netflix',
                'apollo', 'like', 'goodnight', 'mutter', 'noo', 'nuh', 'oof', 'maan', 'cause', 'okay',
                'hey', 'also', 'someone', 'somebody', 'everybody', 'also', 'part' , 'sometimes', 'maybe',
                'three', 'second', 'everything', 'minute', 'name', 'kind', 'point', 'yeah', 'hello', 'one',
                'two', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'whine', 'hnn', 'malla', 'letta',
                'namoo', 'getta', 'nama', 'mana', 'chk','manoo', 'hadda', 'ama', 'carlin',
                'go', 'know', 'host', 'goodnight', 'get', 'gon', 'think', 'say', 'right', 'look',
                'thing', 'make', 'know', 'want', 'going', 'would', 'could', 'gentlemen', 'let', 'please',
                'hbo', 'special' 'yes', 'take', 'say', 'got', 'come', 'see', 'really', 'tell',
                'well', 'give', 'said']):
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
            ('regex', preprocessing.RegexRemover()),
            ('lowercase', preprocessing.LowerCase()),
            ('numbers', preprocessing.NumRemover()),
            ('uncensor', preprocessing.Replacer(swearing_dict)),
            ('punctuation', preprocessing.PuncRemover()),
            ('lemmatizer', preprocessing.Lemmatizer()),
            ('manual_lemmatize', preprocessing.Replacer(lemmatizer_dict)),
            ('remove', preprocessing.WordRemover(dropword_list))
        ]

    incl_blocks = []
    for bloc in blocks:
            if bloc[0] in include_steps:
                incl_blocks.append(bloc)

    pipe = Pipeline(incl_blocks)

    return pipe

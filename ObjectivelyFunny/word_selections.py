swearing_dict = {
    "fuck": [r"fucking", r"f\*ck", r"f_ck", r"f\*\*k", r"f\*\*\*"],
    "bitch": [r"b\*tch", r"b_tch", r"b\*\*\*\*", r"b\*\*ch", r"b\*\*\*h"],
    "shit": [r"sh\*t", r"sh_t", r"s\*\*t", r"s\*\*\*"]}

lemmatizer_dict = {
    'get': 'got',
    'go': 'gon',
    'say': 'said',
    'go': 'went',
    'find': 'finding'}

standard_dropword_list = [
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
'well', 'give', 'said', 'people', 'mean', 'even', 'never', 'way', 'happen', 'put', 'much',
'lot', 'ever', 'still', 'live', 'quite', 'sort', 'actually', 'use', 'tonight', 'find', 'always',
'time', 'good', 'back', 'show', 'little', 'big', 'day', 'talk', 'start', 'need', 'bad', 'first', 'great',
'try', 'year', 'word', 'turn', 'bring', 'feel', 'bit', 'ck', 'cke', 'gger', 'ckin', 'groan', 'groaning',
'high', 'low', 'dingdingde', 'audience', 'cheer']

decade_dropword_list = ['fuck', 'fucking', 'shit', 'motherfucker', 'man', 'woman', 'guy']

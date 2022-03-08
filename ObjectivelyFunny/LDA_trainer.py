# imports
from google.cloud import storage

# from ObjectivelyFunny import cloud_paths
from ObjectivelyFunny.pipeline import set_pipeline
from ObjectivelyFunny.data import get_data, sent_to_words
from ObjectivelyFunny import word_selections

from gensim.models import phrases, Phrases
from gensim import corpora
from gensim.models.ldamodel import LdaModel

class LDATrainer():

    def __init__(self, update_every=5, model_path='model'):
        self.model_path = model_path
        self.update_every = update_every

    def make_words(self, X):
        self.transcript_list = X['full_transcript'].values.tolist()
        self.words = list(sent_to_words(self.transcript_list))
        return self

    def make_grams(self):
        self.bigram = Phrases(self.words, min_count=3, threshold=5)
        self.trigram = Phrases(self.bigram[self.words], threshold=3)
        self.bigram_mod = phrases.Phraser(self.bigram)
        self.trigram_mod = phrases.Phraser(self.trigram)
        self.bigrams = [self.bigram_mod[word] for word in self.words]
        self.trigrams = [self.trigram_mod[self.bigram_mod[word]] for word in self.words]
        return self

    def make_dictionary(self):
        self.id2word = corpora.Dictionary(self.bigrams)
        self.corpus = [self.id2word.doc2bow(bigram) for bigram in self.bigrams]
        return self

    def run(self):
        self.model = LdaModel(corpus=self.corpus,
                        id2word=self.id2word,
                        update_every=self.update_every,
                        num_topics=31,
                        random_state=100,
                        chunksize=15,
                        passes=10,
                        alpha=0.4,
                        eta=0.5,
                        per_word_topics=True)
        return self

    def save_model(self):
        '''
        saves model
        '''
        # client = storage.Client()
        # bucket = client.get_bucket(cloud_paths.BUCKET_NAME)
        # blob = bucket.blob(f'{cloud_paths.STORAGE_LOCATION}{self.model_path}')

        # Save model to disk.
        self.model.save(f'LDA_models/{self.model_path}')

if __name__ == "__main__":
    # input parameters for looping through LDA types
    name_dict = {'1': 'under_30s',
                 '2': '30s',
                 '3': '40s',
                 '4': '50s',
                 '5': 'over_60s'}

    age_list = [list(range(10, 30)),
                 list(range(30, 40)),
                 list(range(40, 50)),
                 list(range(50, 60)),
                 list(range(60, 80))]

    for i, age_range in enumerate(age_list):
        print(f'Starting run {i+1}:')
        df = get_data(age=age_range)
        print('Data acquired')
        clean_steps = ['music', 'brackets', 'lowercase', 'regex', 'numbers', 'uncensor', 'remove', 'punctuation',
        'lemmatizer', 'manual_lemmatize', 'remove2']
        clean_df = set_pipeline(clean_steps,
                            dropword_list = word_selections.standard_dropword_list + word_selections.decade_dropword_list
                            ).fit_transform(df)
        print('Dataframe cleaned')

        model = LDATrainer(update_every=10, model_path=f'age_groups/{name_dict[str(i+1)]}')
        model.make_words(clean_df).make_grams().make_dictionary()
        print('Gram dictionary made')
        model.run()
        print('Model finished running')
        model.save_model()
        print('model_saved')

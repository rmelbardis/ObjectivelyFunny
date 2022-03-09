# imports
from google.cloud import storage

from ObjectivelyFunny import cloud_paths
from ObjectivelyFunny.pipeline import set_pipeline
from ObjectivelyFunny.data import get_data
import gpt_2_simple as gpt2
import shutil


class GPT2Trainer():

    def __init__(self, df, model_name='GPT2_Fem'):
        self.model_name = model_name
        self.df = df
        self.script_string = None
        self.script_file = None
        self.sess = None

    def make_script(self):
        self.script_string = ' '.join(self.df['full_transcript'])
        with open('script.txt', 'w') as script_file:
            script_file.write(self.script_string)
        return self

    def run(self):
        """train the model"""
        gpt2.download_gpt2(model_name="124M")
        self.sess = gpt2.start_tf_sess()

        gpt2.finetune(self.sess,
                      dataset='script.txt',
                      model_name='124M',
                      steps=1000,
                      restore_from='fresh',
                      run_name='script_run',
                      print_every=100,
                      sample_every=1000,
                      save_every=250)
        return self

#    def save_model(self):
#        """method that saves the model into a .joblib file and uploads it on Google Storage /models folder
#       HINTS : use joblib library and google-cloud-storage"""


if __name__ == "__main__":
    df = get_data()
    clean_steps = ['music', 'uncensor', 'regex']
    clean_df = set_pipeline(clean_steps).fit_transform(df)

    session = GPT2Trainer(clean_df)
    session.make_script()
    session.run()

    shutil.make_archive('all_comedians_ton', 'zip', 'checkpoint')
    client = storage.Client()
    bucket = client.bucket('wagon-data-805-farrell')
    blob = bucket.blob('all_comedians_ton')
    blob.upload_from_filename('all_comedians_ton.zip')

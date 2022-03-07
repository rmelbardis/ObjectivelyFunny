# imports
from ObjectivelyFunny import cloud_paths
from ObjectivelyFunny.model_setup import initialize_model
import joblib
from google.cloud import storage

from ObjectivelyFunny.pipeline import set_pipeline
from ObjectivelyFunny.data import get_data, get_small_data, get_X_y_vocab_seqlength

class Trainer():

    def __init__(self, X, y, model, epochs=50, batch_size=128, validation_split=0.05, model_name='LSTM'):
        self.pipeline = None
        self.X = X
        self.y = y
        self.model = model
        self.epochs = epochs
        self.batch_size = batch_size
        self.validation_split = validation_split
        self.model_name = model_name

    def run(self):
        """train the model"""
        self.model.fit(self.X, self.y,
                       epochs = self.epochs,
                       validation_split = self.validation_split,
                       batch_size = self.batch_size)
        return self

    def save_model(self):
        """method that saves the model into a .joblib file and uploads it on Google Storage /models folder
        HINTS : use joblib library and google-cloud-storage"""

        # saving the trained model to disk is mandatory to then beeing able to upload it to storage
        # Implement here
        joblib.dump(self.pipeline, f'{self.model_name}.joblib')
        print(f"{self.model_name}.joblib saved locally")

        client = storage.Client()
        bucket = client.bucket(cloud_paths.BUCKET_NAME)
        blob = bucket.blob(f'{cloud_paths.STORAGE_LOCATION}{self.model_name}.joblib')
        blob.upload_from_filename(f'{self.model_name}.joblib')
        print(f"uploaded {self.model_name}.joblib to gcp cloud storage under \n => {cloud_paths.STORAGE_LOCATION}{self.model_name}.joblib")

if __name__ == "__main__":
    df = get_small_data()

    clean_steps = ['music', 'uncensor', 'regex', 'split_words', 'sequences']
    clean_df = set_pipeline(clean_steps).fit_transform(df)

    seq_length = 21
    X, y, vocab_size, X_seq_length = get_X_y_vocab_seqlength(clean_df, seq_length)

    model = Trainer(X, y, initialize_model(vocab_size, X_seq_length, embed_dims=50))
    model.run()
    model.save_model()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import ImageColorGenerator

class ComedyWordCloud:
    def __init__(self, df, mask=None):
        self.df = df
        self.mask = mask

    def generate_wordcloud(self, selection):
        '''
        Initiating a word cloud with
        '''
        wc = WordCloud(width=500, height = 500, background_color='white',
                    max_words = 150, collocations=False, contour_width=50,
                    contour_color='steelblue',
                    stopwords = STOPWORDS, mask=self.mask)
        word_cloud = wc.generate(selection)
        return word_cloud

    def plot_cloud(self, selection):
        '''
        plot a word cloud with a selection of text
        using a given mask
        '''
        # Generate word cloud and set the size
        wordcloud = self.generate_wordcloud(selection)
        plt.figure(figsize=(30, 20))
        # Display image
        if self.mask is None:
            plt.imshow(wordcloud)
        else:
            image_colors = ImageColorGenerator(self.mask)
            plt.imshow(wordcloud.recolor(color_func=image_colors),
                       interpolation="bilinear")
        # No axis details
        plt.axis("off")
        plt.show();


    def get_index(self, df, option, condition):
        '''
        Takes option as a string, with options of: ['artist', 'age', 'gender']
        Takes condition as string
        Returns a list of index in the dataframe meeting the condition
        '''
        option_dict = {'age': 'age_then', 'gender': 'artist_gender'}
        gender_dict = {'F': '1', 'M': '2', 'Q': '3'}

        if option not in ['artist', 'age', 'gender']:
            return 'Options are: artist, age or gender.'

        if option=='gender' and condition not in ['F', 'M', 'Q']:
            return 'Choose from: F(emale), M(ale) or Q(ueer).'

        if type(condition) is not str:
            return 'Please put your condition in a string.'

        condition = condition.title()

        # translating user selection into dataframe column name
        for k, v in option_dict.items():
            option = option.replace(k, v)
        option = option.lower()

        if option=='artist':
            output= df[df[option] == condition].index
        else:
            # encoding gender conditions
            if option=='artist_gender':
                for k, v in gender_dict.items():
                    condition = condition.replace(k, v)
            output = df[df[option] == int(condition)].index
        if len(output)<1:
                return f'No results with {option} as {condition}, please check.'
        return output

    def plot_decade_cloud(self, df, decade):
        '''
        Input a decade as int
        plot a word cloud for that decade
        '''

        if type(decade)!=int:
            return 'Please input decade value as an int.'
        if decade not in [1960, 1970, 1980, 1990, 2000, 2010, 2020]:
            return 'select a decade from [1960, 1970, 1980, 1990, 2000, 2010, 2020]'
        decade_df = df[(df.year//10)*10 == decade]

        t = decade_df['full_transcript_clean']
        selection = ' '.join(t)
        print(f"Plotting with transcripts of {len(selection)} characters...")
        print(f'Here is a word cloud of transcripts from the {decade}s.')
        self.plot_cloud(selection)

    def plot_some_cloud(self, df, option, condition):
        '''
        search for index meeting conditions
        plot a word cloud
        '''

        index = self.get_index(df, option, condition)
        if index[0] == index[-1]:
            index = index[0]
            selection = df['full_transcript_clean'][index]
        else:
            t = df['full_transcript_clean'][index]
            selection = ' '.join(t)

        no_of_transcripts = index[-1]-index[0]+1

        print(f'{no_of_transcripts} transcripts found.')
        print(f"Plotting with transcripts of {len(selection)} characters...")

        self.plot_cloud(selection)

if __name__ == "__main__":
    # Get and clean data
    df = pd.read_json('../raw_data/fully_stripped_df.json')
    mask = np.array(Image.open('../images/1960.jpg'))
    wc = ComedyWordCloud(df, mask)
    wc.plot_decade_cloud(df, 1960)

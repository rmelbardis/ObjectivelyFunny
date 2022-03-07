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
    def __init__(self, df):
        self.df = df
        self.year = None
        self.mask = None

    def generate_wordcloud(self, selection):
        '''
        Generating a default word cloud
        '''
        custom_color = color_combo(self)

        wc = WordCloud(width=500, height = 500, background_color='white',
                    max_words = 150, collocations=False,
                    stopwords = STOPWORDS, mask=custom_color[1],
                    contour_width=10, contour_color=custom_color[0])
        word_cloud = wc.generate(selection)
        return word_cloud

    def plot_cloud(self, selection):
        '''
        Plot a word cloud with a selection of text
        using a given mask
        '''
        # Generate word cloud and set the size
        wordcloud = self.generate_wordcloud(selection)
        plt.figure(figsize=(10,8))
        # Display image
        if self.mask is None:
            plt.imshow(wordcloud)
        else:
            image_colors = ImageColorGenerator(self.mask)
            plt.imshow(wordcloud.recolor(color_func=image_colors),
                       interpolation="bilinear")
        # No axis details
        plt.axis("off")
        plt.savefig(f"{self.year}_cloud.png", format="png")
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

    def plot_decade_cloud(self, year):
        '''
        Input a decade number as int,
        plot a word cloud for that decade
        '''
        self.year = year
        if not type(self.year) is int:
            message = 'Please inpute decade as an int.'
            print(message)
            return message
        if self.year not in [1960, 1970, 1980, 1990, 2000, 2010, 2020]:
            message = 'Decade number not supported. Please choose from 1960-2020.'
            print(message)
            return message

        decade_df = self.df[(self.df.year//10)*10 == self.year]

        t = decade_df['full_transcript_clean']
        selection = ' '.join(t)
        print(f"Plotting with transcripts of {len(selection)} characters...")
        print(f'Here is a word cloud of transcripts from the {self.year}s.')
        self.plot_cloud(selection)

    def plot_some_cloud(self, df, option, condition):
        '''
        Search for index meeting conditions
        Plot a word cloud using selected text
        '''

        index = self.get_index(df, option, condition)
        if len(index) > 1:
            index = index[0]
            selection = df['full_transcript_clean'][index]
            no_of_transcripts = index[-1]-index[0]+1
        else:
            t = df['full_transcript_clean'][index]
            selection = ' '.join(t)
            no_of_transcripts = 1

        print(f'You selected {condition} as {option}.')
        print(f'{no_of_transcripts} transcript(s) found.')
        print(f"Plotting with transcripts of {len(selection)} characters...")

        self.plot_cloud(selection)

def color_combo(self):
    image = f'{self.year}.jpg'
    mask = np.array(Image.open(f'../images/{image}'))
    color_dict = {'2020.jpg': 'orange', '1960.jpg': 'purple',
                  '2010.jpg': 'orange', '2000.jpg': 'navy',
                  '1970.jpg': 'green', '1990.jpg': 'brown',
                  '1980.jpg': 'black'}

    if image in color_dict:
        color = color_dict[image]
        # for k,v in color_dict.items():
        #     color = image.replace(k, v)
    else:
        color = 'white'

    self.mask = mask

    return color, mask

if __name__ == "__main__":
    # Get and clean data
    df = pd.read_json('../raw_data/fully_stripped_df.json')
    # image = '../images/emoji.png'
    #mask = np.array(Image.open(image))


    wc = ComedyWordCloud(df)
    wc.plot_decade_cloud(1970)


     #wc.plot_some_cloud(df, 'artist', 'mae martin')

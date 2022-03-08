import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

class ComedyWordCloud:
    def __init__(self, df):
        self.df = df
        self.year = None
        self.mask = None
        self.option = None
        self.condition = None
        self.age = None

    def color_combo(self):
        if self.year != 1989:
            image = f'{self.year}.jpg'
        else:
            image = f'1980.jpg'
        mask = np.array(Image.open(f'../images/{image}'))
        color_dict = {'2020.jpg': 'orange', '1980.jpg': 'black',
                    '2010.jpg': 'orange', '2000.jpg': 'navy',
                    '1990.jpg': 'brown'}
        # '1960.jpg': 'purple', '1970.jpg': 'green', '1980.jpg': 'black'

        if image in color_dict:
            color = color_dict[image]
            # for k,v in color_dict.items():
            #     color = image.replace(k, v)
        else:
            color = 'white'

        self.mask = mask

        return color, mask

    def generate_wordcloud(self):
        '''
        Generating a default word cloud
        '''
        if self.year is not None:
            custom_color = self.color_combo()
            wc = WordCloud(width=500, height = 500, background_color='white',
                    max_words = 150, collocations=False,
                    stopwords = STOPWORDS, mask=custom_color[1],
                    contour_width=10, contour_color=custom_color[0])
        else:
            self.mask = np.array(Image.open(f'../images/emoji.png'))
            wc = WordCloud(width=500, height = 500, background_color='white',
                    max_words = 150, collocations=False,
                    stopwords = STOPWORDS, mask=self.mask)
        word_cloud = wc.generate(self.selection)
        return word_cloud

    def plot_cloud(self):
        '''
        Plot a word cloud with a selection of text
        using a given mask
        '''
        # Generate word cloud and set the size
        wordcloud = self.generate_wordcloud()
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
        if self.year:
            plt.savefig(f"../cloud-images/{self.year}_cloud.png", format="png")
        elif self.age:
            plt.savefig(f"../cloud-images/{self.age}_cloud.png", format="png")
        else:
            plt.savefig(f"../cloud-images/{self.option}_{self.condition}_cloud.png", format="png")
        #plt.show();

    def get_index(self):
        '''
        Returns a list of index in the dataframe meeting the condition
        '''
        option_dict = {'age': 'age_then', 'gender': 'artist_gender'}
        gender_dict = {'F': '1', 'M': '2', 'Q': '3'}

        if self.option not in ['artist', 'age', 'gender']:
            return 'Options are: artist, age or gender.'

        if self.option=='gender' and self.condition not in ['F', 'M', 'Q']:
            return 'Choose from: F(emale), M(ale) or Q(ueer).'

        if type(self.condition) is not str:
            return 'Please put your condition in a string.'

        self.condition = self.condition.title()

        # translating user selection into dataframe column name
        for k, v in option_dict.items():
            self.option = self.option.replace(k, v)
        self.option = self.option.lower()

        if self.option=='artist':
            output= self.df[self.df[self.option] == self.condition].index
        else:
            # encoding gender conditions
            if self.option=='artist_gender':
                for k, v in gender_dict.items():
                    self.condition = self.condition.replace(k, v)
            output = self.df[self.df[self.option] == int(self.condition)].index
        if len(output)<1:
            message = f'No results with {self.option} as {self.condition}, please check.'
            print(message)
            return message

        return output

    def plot_decade_cloud(self, year):
        '''
        Input a decade number as an int,
        plot a word cloud for that decade
        '''
        self.year = year
        if not type(self.year) is int:
            message = 'Please inpute decade as an int.'
            print(message)
            return message
        if self.year not in [1989, 1990, 2000, 2010, 2020]:
            message = 'Decade number not supported. Please choose from 1960-2020.'
            print(message)
            return message

        if self.year == 1989:
            decade_df = self.df[(self.df.year//10)*10 <= self.year]

        else:
            decade_df = self.df[(self.df.year//10)*10 == self.year]

        t = decade_df['full_transcript_clean']
        self.selection = ' '.join(t)
        print(f"Plotting with transcripts of {len(self.selection)} characters...")
        print(f'Here is a word cloud of transcripts from the {self.year}s.')
        self.plot_cloud()

    def plot_age_cloud(self, age):
        '''
        Input a decade number as an int,
        plot a word cloud for that decade
        '''
        self.age= age
        if not type(self.age) is str:
            message = 'Please inpute age group as a string.'
            print(message)
            return message
        if self.age not in ['U30', '30', '40', '50', '60', 'O60']:
            message = 'Age group not supported.'
            print(message)
            return message

        age_group_key = pd.read_json('../raw_data/age_group.json')

        t = self.df[age_group_key['age_group']== self.age]['full_transcript_clean']
        self.selection = ' '.join(t)
        print(f"Plotting with transcripts of {len(self.selection)} characters...")
        print(f'Here is a word cloud of transcripts from the age group {self.age}.')
        self.plot_cloud()

    def plot_some_cloud(self, option, condition):
        '''
        Search for index meeting conditions
        Plot a word cloud using selected text
        '''
        self.option = option
        self.condition = condition

        print(f'You selected {condition} as {option}.')

        index = self.get_index()
        print('Searching...')

        if len(index) > 1:
            self.selection = self.df['full_transcript_clean'].loc[index]
            self.selection = ' '.join(self.selection)
            no_of_transcripts = len(index)
        else:
            t = self.df['full_transcript_clean'][index]
            self.selection = ' '.join(t)
            no_of_transcripts = 1
        print(f'{no_of_transcripts} transcript(s) found.')

        print(f"Plotting with transcripts of {len(self.selection)} characters...")

        self.plot_cloud()


if __name__ == "__main__":
    # Get and clean data
    df = pd.read_json('../raw_data/temp_df_for_testing.json')
    wc = ComedyWordCloud(df)

    # for num in [1989, 1990, 2000, 2010, 2020]:
    #     wc.plot_decade_cloud(num)
    #wc.plot_some_cloud('gender', 'F')
    #for char in ['U30', '30', '40', '50', '60', 'O60']:
    #    wc.plot_age_cloud(char)

    wc.plot_decade_cloud(1989)

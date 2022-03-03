from curses import keyname
from matplotlib import container
from matplotlib.pyplot import text
import streamlit as st
# Import the required module for text
# to speech conversion
from gtts import gTTS
import pandas as pd

CSS = """
h1 {
    color: red;
}
.stApp {
    background-image: url(https://s1.cdn.autoevolution.com/images/news/gallery/kia-s-sexy-robot-girl-alyssa-campanella-video-photo-gallery_7.jpg);
    background-size: cover;
}
"""
if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

df = pd.read_json('../raw_data/artist_year_name.json')


heading = st.container()
heading.title('Objectively Funny')
heading.header('Welcome to the Amazing Comedy Bot')
st.markdown("<h1 style='text-align: center; color: green;'>A Message from Bot Dot</h1>", unsafe_allow_html=True)
# bot_intro = 'Hello! I hope you are having a fine day... I am the amazing comedy bot. Hopefully I don\'t swear to fucking much or make an ass-hole of myself'
# ta_tts = gTTS(bot_intro, lang ='en', tld='cn', slow=False)
# ta_tts.save('intro.mp3')
audio_file = open('intro.mp3', 'rb')
audio_intro = audio_file.read()
st.audio(audio_intro, format='audio/ogg',start_time=0)

# def choose_artist():
#     chosen_artist = st.text_input('Please choose a comedian you would like to hear from')
#     the_artist = df[df['artist'] == chosen_artist]
#     return the_artist

# def choose_title(the_artist):
#     script = the_artist['full_transcript']
#     st.write(the_artist['title'])
#     choose_title = st.number_input('choose the title by index', value=int)
#     return the_artist.iloc[choose_title]

#side bar with Artist Year and Title
artists = df['artist'].drop_duplicates()
artist_choice = st.sidebar.selectbox('Select your artist:', artists)
years = df["year"].loc[df["artist"] == artist_choice]
year_choice = st.sidebar.selectbox('Year', years)
titles = df['show_name'].loc[df['year'] == year_choice]
title_choice = st.sidebar.selectbox('title', titles)
awesome = df.loc[(df['artist']==artist_choice) & (df['year']==year_choice) & (df['show_name']==title_choice)]
st.table(awesome['full_transcript'])
df_selection = df.query(
    ("artist_choice == @artist_choice) and (year_choice == @year_choice) and (tilte_choice == @title_choice)")
)

#Displays the sidebar search
with st.expander('Let\'s see some samples of comedian scripts'):
    st.table(awesome['full_transcript'])


#choose_title(choose_artist())

# chosen_title = the_artist.iloc[choose_title]

#


#     ta_tts = gTTS(reduce_script, lang ='en', tld='cn', slow=False)
#     ta_tts.save('script.mp3')
#     audio_file = open('script.mp3', 'rb')
#     audio_bytes = audio_file.read()
#     return st.audio(audio_bytes, format='audio/ogg',start_time=0)

#in app.py file
#test in this file with streamlit
audio_file = open('script.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg',start_time=0)

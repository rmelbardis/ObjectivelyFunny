import streamlit as st
# Import the required module for text
# to speech conversion
from gtts import gTTS

st.write('hello there')

text_en = 'Hello.... I am looking forward to becoming a stand up comedian and representing your team. I don\'t know what I am going to say... but hopefully I won\'t be fucking swearing too much or be an asshole; it is good NO?'
ta_tts = gTTS(text_en, lang ='en', tld='ca')
ta_tts.save('trans.mp3')
audio_file = open('trans.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg',start_time=0)

#in app.py file
#test in this file with streamlit

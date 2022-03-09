import streamlit as st
from PIL import Image
from gtts import gTTS
import requests

def app():
    with open('bot_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    text_input= st.text_input('Type below', 'Hello hello hello')
    #st.write(f'{len(text_input)} characters')

    api_url = 'https://obj-fun-2-2g6nxe3ofq-ew.a.run.app/comedian'

    params = {
        'prefix': text_input, # text for joke
    }

    bot_says = ''
    joke1=''
    joke2=''
    joke3=''
    with st.expander('Click here'):
        if st.button('generate'):
            response = requests.get(api_url, params=params)
            a = response.json()
            st.write(a)
            bot_says = str(a['lines'])
            joke1 = str(a['lines'][0])
            joke2 = str(a['lines'][1])
            joke3 = str(a['lines'][2])


    if len(bot_says)>0:
        st.write(bot_says)
        with open('bot_talk.txt', 'w') as t:
                t.write(bot_says)
        with open('joke1.txt', 'w') as t:
            t.write(joke1)

    if st.button('play', key=1):
        with open('joke1.txt', 'r') as q:
            lines = q.readline()
            ta_tts = gTTS(lines, lang ='en', tld='cn', slow=False)
            ta_tts.save('joke1.mp3')
        audio_file = open('joke1.mp3', 'rb')
        audio_test = audio_file.read()
        st.audio(audio_test, format='audio/ogg', start_time=0)

    #bot_intro = 'Thankyou, oh thankyou, thankyou so much... I am the amazing comedy bot. Hopefully I don\'t swear to much or make an ass of myself'
    #ta_tts = gTTS(bot_intro, lang ='en', tld='cn', slow=False)
    #ta_tts.save('intro.mp3')



    st.header('A bot that produces scripts from all comedians')
    col1, col2, col3 = st.columns(3)
    with col1:
        image2 = Image.open('logo.png')
        st.image(image2, width=350)
    with col2:
        if st.button('Examples', key=3):
            st.write('A script produced here from all comedians')
            st.write('generate all comedian scripts')

    st.header('A bot which produces short jokes with a prompt text')
    col1, col2, col3 = st.columns(3)
    with col1:
        image3 = Image.open('boy-bot.png')
        st.image(image3, width=350)
    with col2:
        if st.button('Examples', key=4):
            st.write('A bot which prodcues short jokes with a prompt')
            st.write('bot generated here')

    st.header('A bot that produces a script based upon female comedy')
    col1, col2, col3 = st.columns(3)
    with col1:
        image1 = Image.open('robecca.png')
        st.image(image1, width=350)
    with col2:
        if st.button('Click here to hear from female comedians', key=2):
            st.write('A script produced here from all female comedians')
            st.write('generate a script from female comedians')

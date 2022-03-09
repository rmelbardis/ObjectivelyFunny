import streamlit as st
from gtts import gTTS

def app():
    with open('bot_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    text_input= st.text_input('Type below', 'Hello hello hello')
    st.write(f'{len(text_input)} characters')

    #bot_intro = 'Thankyou, oh thankyou, thankyou so much... I am the amazing comedy bot. Hopefully I don\'t swear to much or make an ass of myself'
    #ta_tts = gTTS(bot_intro, lang ='en', tld='cn', slow=False)
    #ta_tts.save('intro.mp3')
    audio_file = open('intro.mp3', 'rb')
    audio_intro = audio_file.read()

    if st.button('play', key=1):
        st.audio(audio_intro, format='audio/ogg',start_time=0)

    st.header('A bot that produces a script based upon female comedy')
    st.write('A script produced here from all female comedians')
    if st.button('female comedians', key=2):
        st.write('generate a script from female comedians')

    st.header('A bot that produces scripts from all comedians')
    st.write('A script produced here from all comedians')
    if st.button('All Comedians combined', key=3):
        st.write('generate all comedian scripts')

    st.header('A bot which produces short jokes with a prompt text')
    st.write('A bot which prodcues short jokes with a prompt')
    if st.button('bot one liners', key=4):
        st.write('bot generated here')
    
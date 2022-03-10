import streamlit as st
from PIL import Image
from gtts import gTTS
from predict import generate_text, get_jokes

def app():
    text_output =''
    bot_says = ''
    joke1=''
    joke2=''
    joke3=''

    with open('styles/bot_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.write('Type your prompt here')
    text_input= st.text_input('', 'Welcome')

    st.header('Introducing... Robecca')
    st.write('A bot that produces a script based upon female comedy')

    col1, col2, col3 = st.columns(3)
    with col1:
        image1 = Image.open('images/robecca.png')
        st.image(image1, width=350)
    with col2:
        if st.button('Click here to generate', key=2):
            with st.spinner('Wait for it...'):
                text_output, message= generate_text(text_input)
            st.success('Done!')
            st.markdown(message)
            bot_says, joke1, joke2, joke3 = get_jokes(text_output)
            st.markdown('🎉 Completed')

    if len(bot_says)>0:
        with open('jokes/bot_talk.txt', 'w') as t:
                t.write(bot_says)
        for i, char in enumerate([joke1, joke2, joke3]):
            with open(f'jokes/joke{i+1}.txt', 'w') as t:
                t.write(char)

    if st.button('♻️  Show results'):
        for i, char in enumerate([joke1, joke2, joke3]):
            with open(f'jokes/joke{i+1}.txt', 'r') as d:
                line = d.readline()
                st.write(i+1,':', line)

    st.write('-----------')

    st.write('Which joke would you like to hear?')
    option = st.selectbox(
     '',
     ('1', '2', '3'))

    if st.button('play', key=1):
        # index 0 is the first joke (i.e. joke1)
        num = int(option)

        with open(f'jokes/joke{num}.txt', 'r') as q:
            # extracting the string from saved file
            lines = q.readline()
            # generating and saving the audio file
            ta_tts = gTTS(lines, lang ='en', tld='cn', slow=False)
            ta_tts.save(f'jokes/joke{num}.mp3')
        # locating and opening the audio file
        audio_file = open(f'jokes/joke{num}.mp3', 'rb')
        audio_test = audio_file.read()
        # showing the text again
        st.markdown(lines)
        # playing the audio file
        st.audio(audio_test, format='audio/ogg', start_time=0)

    st.write('-----------')

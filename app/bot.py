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

    st.header('Disclaimer: ')
    st.markdown('- *The output is not curated by humans. Stand-up comedy uses\
        a lot of explicit language and some viewers may find the output offensive.*')
    st.markdown("- *Uses OpenAI's GPT2 model and finetuned using gpt2-simple\
        (credit: Max Woolf)*")
    st.markdown("- Finetuned on 82 scripts, totalling 2.74m characters and 518k\
        words from the following comedians: 'Aisling Bea', 'Ali Wong',\
            'Amanda Seales', 'Amy Schumer',  'Andi Osho', 'Angela Barnes',\
                'Anjelah Johnson', 'Bridget Everett', 'Celia Pacquola',\
                    'Chelsea Peretti', 'Christina Pazsitzky',\
                        'Cristela Alonzo', 'Dawn French', 'Desiree Burch',\
                            'Ellen Degeneres', 'Ellie Taylor', 'Emily Heller',\
                                'Enissa Amani', 'Felicity Ward', 'Francesca Martinez',\
                                    'Gina Yashere', 'Hannah Gadsby', 'Holly Walsh',\
                                        'Iliza Shlesinger', 'Jen Brister', 'Jen Kirkman',\
                                            'Katherine Ryan', 'Kathleen Madigan', 'Kerry Godliman',\
                                                'Lisa Lampanelli', 'Lucy Porter', 'Luisa Omielan',\
                                                    'Maria Bamford', 'Michelle Wolf', 'Miranda Hart',\
                                                        'Nikki Glaser', 'Roisin Conaty', 'Sara Pascoe',\
                                                            'Sarah Cooper', 'Sarah Millican', 'Sarah Silverman',\
                                                                'Shappi Khorsandi', 'Tiffany Haddish', 'Tig Notaro',\
                                                                    'Urzila Carlson', 'Victoria Wood', 'Wanda Sykes',\
                                                                        'Whitney Cummings', 'Zoe Lyons'. ")
    st.header('Please welcome to the stage... Robecca Stepford!')
    st.write('She is a bot who produces stand-up comedy lines based on transcripts\
        of female comedians. Just give her a few words to start!')
    st.write('Type your prompt here, we recommend the start of a sentence:')
    text_input= st.text_input('', 'When I was a kid')


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

    st.write('She can even speak! Which joke would you like to hear?')
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

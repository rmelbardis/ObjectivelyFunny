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

    with st.expander("Click here to see Robecca's top 10 jokes (so far)"):
        st.write('''
1 : it always seems like the last thing you would want to do is have sex with your ex-wife. Well, I guess that's why I'm here. Because it's the last thing you would want to do. I mean, I… I've been with a woman for… thirty years, and she's been beautiful and kind and kind and kind and kind and kind. And I… I asked her out on a date. She said, "Come on, let's go out and have a drink." And I said, "No, I don't want to. \n
2 : "space” And so, I just came out to my mom, and my mom was like, “Is there anything you love?” And she was like… “I love the way we speak.” And… and I was like, “I don’t know what you’re saying.” And she was like, “May I ask you a question?” And I was like, “No, I’m so sorry", \n
3 : i have never eaten in my life, but sometimes I think I have, and sometimes I think I have… I think I have a… It’s nearly a year and a half, and… I’ve had a lot of sex. And… I don’t know how to tell, but… It’s almost like an ice cream punch, and… I don’t like to think about it, because I’m too excited. \n
4 : i am a dustbin” For those of you that don’t know what dustbin is, it is a collection of dust on a stick that people sit on for hours looking at dust in their underwear. I’m not even kidding. This right here. It’s a little side-effect of my upbringing that’s sort of made me a dustbin. \n
5 : it always seems to be giving voice to someone's biology. That's why I'm seriously considering adoption.  People say to me, "Stewart, you're too old to be adopted."  I stopped breast-feeding at five.  How was your day?  LAUGHTER AND APPLAUSE  After hearing that my real parents were budgies, I couldn't look at myself in the mirror.  Yes, I'm a pretty boy. \n
6 : it always seems to have it all. I had to say something. Last night, I went to a karaoke bar that didn't play any '70s music. At first, I was afraid. Oh, I was petrified. I farted in a full lift today which was wrong on so many levels. My dad has a weird hobby. He collects empty bottles which sounds so much better than "alcoholic", doesn't it? I was raised by my father. \n
7 : i know this person’s got AIDS, so she should’ve got to see it. She’s got to see for herself, okay? You go to the doctor and he’ll tell you that you’re infectious. He’ll think that you’re a horrible person, but that you’re a clever person. \n
8 : i'm starting to think you're just like the next person to die, you know, you just go get a job. I mean, I saw one of your videos and I was like, “I’ll be the first one to die,” and then I heard somebody calling in sick with a stomach brace. \n
9 : did you really think I’m gonna be giving a TED Talk about how the Internet is ruining my life? Do I have to get this over with? I’m gonna tell you what I wanna do now! I wanna appeal to the best in society! I’m gonna win this argument. This is for you. No one wants to hear about the worst example of sexual harassment they’ve ever had. And you’re right. Second Amendment people! Oh, wait. \n
10 : i wish i was young. Now that is a real, real fuck joke. It’s not that I can’t remember it. It’s just that shit has changed. Some of the shit on that roast is still in the oven, so, I had to replace the wafer with the dryer. You know how that goes. And then, the seats are in the back, the queue is nowhere to be found.''')

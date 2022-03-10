import streamlit as st
from PIL import Image

def app():
    gh_url = 'https://github.com/rmelbardis/ObjectivelyFunny'
    image1 = Image.open('images/workflow-2-paths.001.jpeg')

    with open('styles/about_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    '''
    ------------------------------
    '''

    st.header('**Welcome to our home page!**')
    st.markdown("<h1 style='font-size: 20px; color: white;'>We recommend the use of dark mode. You can change the theme in the settings (on your right).</h1>",
                    unsafe_allow_html=True)

    st.subheader('**Our project**')
    st.write('This project was made by 4 students from the Le Wagon Data Science Bootcamp batch 805.')
    st.write('We have sourced and processed a wide range of stand-up scripts to analyse comedy and comedians.')
    st.write("Please check our [GitHub page](%s)" % gh_url)

    st.subheader('Here you can find:')
    st.write("1) Word clouds on comedy topics")
    st.write("2) Robecca: an AI bot that tells you jokes based on your text input")

    st.subheader('Need help?')
    st.write('- Use the **sidebar** on the left to go to different sections.')
    st.write('- 📪 Please speak to Rei if you have any questions.')

    st.header('About our data')
    st.subheader('Data Overview')
    st.write('- Data Size: 555 individual transcripts')
    st.write('- Average age of comedians: 41')
    st.write("- 84% Male, 15% Female, 1% Gender queer")

    st.subheader('Data preprocessing')
    st.image(image1, width=600)

    st.header('Acknowledgments')

    st.subheader('Data sources:')

    url1 = "http://scrapsfromtheloft.com/stand-up-comedy-scripts/"
    st.write("- [Scraps From the Loft](%s)" % url1)
    url2 = 'https://subsaga.com/bbc/browse/genre/comedy/standup/?page=0'
    st.write("- [Subsaga](%s)" % url2)
    url3 = 'https://www.themoviedb.org/?language=en-GB'
    st.write("- [The Movie Database (TMDB)](%s)" % url3)

    st.subheader('Packages and APIs:')
    url4 = 'https://pypi.org/project/tmdbsimple/'
    st.write("- [tmdbsimple](%s)" % url4)
    url5 = 'https://openai.com/api/'
    st.write('- [GPT-2](%s)' % url5)
    url6 = 'https://github.com/minimaxir/gpt-2-simple'
    st.write('- [gpt-2-simple](%s)' % url6)

    st.subheader('Special thanks:')
    st.write("- Amanda, Julio, Marie, Mohamad, Vinny, Yannis, Yassine")
    st.write("- and all lecturers and TAs at Le Wagon London")

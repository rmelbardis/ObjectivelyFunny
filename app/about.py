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
    st.write('This project is made by 4 students from Le Wagon Data Science Bootcamp batch 805.')

    st.subheader('**Our project**')
    st.write('...has sourced and processed a wide range of stand-up scripts to analyse comedy and comedians.')

    st.subheader('Here you can find:')
    st.write("1) Word Clouds on comedy topics")
    st.write("2) An AI bot that tells you a joke based on your text input")

    st.subheader('Need help?')
    st.write('- Use the **sidebar** on the left to go to different sections.')
    st.write('- 📪 Please speak to Rei if you have any questions.')

    st.header('About our data')
    st.write("- Please check our GitHub page here: [link](%s)" % gh_url)

    st.subheader('Data preprocessing')
    st.image(image1, width=600)

    st.header('Acknowledgments')

    st.subheader('Data sources:')

    url1 = "http://scrapsfromtheloft.com/stand-up-comedy-scripts/"
    st.write("- Scraps From the Loft [link](%s)" % url1)
    url2 = 'https://subsaga.com/bbc/browse/genre/comedy/standup/?page=0'
    st.write("- Subsaga [link](%s)" % url2)
    url3 = 'https://www.themoviedb.org/?language=en-GB'
    st.write("- The Movie Database (TMDB) [link](%s)" % url3)

    st.subheader('Packages and APIs:')
    url4 = 'https://pypi.org/project/tmdbsimple/'
    st.write("- tmdbsimple [link](%s)" % url4)
    url5 = 'https://openai.com/api/'
    st.write('- GPT-2 [link](%s)' % url5)

    st.subheader('Special thanks:')
    st.write("- Amanda, Julio, Marie, Mohamad, Vinny, Yannis, Yassine")

import streamlit as st
from PIL import Image

def app():
    with open('about_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    '''
    ------------------------------
    '''


    st.write('Welcome to our home page.')
    gh_url = 'https://github.com/rmelbardis/ObjectivelyFunny'
    st.write("Our GitHub page [link](%s)" % gh_url)

    st.write('Please speak to Rei if you have any questions.')

    st.header('Data preprocessing')
    image1 = Image.open('workflow-2-paths.001.jpeg')
    st.image(image1, width=600)

    st.header('Acknowledgments')

    st.subheader('Data sources:')

    url1 = "http://scrapsfromtheloft.com/stand-up-comedy-scripts/"
    st.write("1. Scraps From the Loft [link](%s)" % url1)
    url2 = 'https://subsaga.com/bbc/browse/genre/comedy/standup/?page=0'
    st.write("2. Subsaga [link](%s)" % url2)
    url3 = 'https://www.themoviedb.org/?language=en-GB'
    st.write("3. The Movie Database (TMDB) [link](%s)" % url3)

    st.subheader('Packages and APIs:')
    url4 = 'https://pypi.org/project/tmdbsimple/'
    st.write("1. tmdbsimple [link](%s)" % url4)

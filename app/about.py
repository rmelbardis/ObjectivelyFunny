import streamlit as st
from PIL import Image

def app():
    gh_url = 'https://github.com/rmelbardis/ObjectivelyFunny'

    with open('styles/about_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    logo = Image.open('images/logo.png')
    st.image(logo, width=100)

    '''
    ------------------------------
    '''

    st.header('**Welcome to our our project!**')
    st.markdown("<h1 style='font-size: 18px; color: white;'>We recommend the use of dark mode. You can change the theme in the settings (on your right).</h1>",
                    unsafe_allow_html=True)

    st.write('This project was made by 4 students from the Le Wagon Data Science Bootcamp.')
    st.write('We have sourced and processed a wide range of stand-up scripts to analyse comedians and make our own comedy.')
    st.write("[GitHub Repo](%s)" % gh_url)

    st.subheader('Use the **sidebar** on the left to navigate the app:')
    st.write("1) Word clouds on comedy topics")
    st.write("2) Robecca Stepford: an AI bot that tells you jokes based on your text input")

    st.header('About our data')
    st.subheader('Data at a glance')
    st.write('- 555 individual transcripts')
    st.write('- 268 comedians')
    st.write('- 19 million characters')
    st.write('- 3.6 million words')
    st.write('- Information about artist gender, artist age and release year')

    st.header('Acknowledgments')

    st.subheader('Data sources:')

    url1 = "http://scrapsfromtheloft.com/stand-up-comedy-scripts/"
    st.write("- [Scraps From the Loft](%s)" % url1)
    url2 = 'https://subsaga.com/bbc/browse/genre/comedy/standup/?page=0'
    st.write("- [Subsaga](%s)" % url2)
    url3 = 'https://www.themoviedb.org/?language=en-GB'
    st.write("- [The Movie Database (TMDB)](%s)" % url3)

    st.subheader('Packages and APIs:')
    url6 = 'https://github.com/minimaxir/gpt-2-simple'
    st.write('- [gpt-2-simple](%s)' % url6)
    url5 = 'https://radimrehurek.com/gensim/'
    st.write('- [Gensim](%s)' % url5)
    url4 = 'https://pypi.org/project/tmdbsimple/'
    st.write("- [tmdbsimple](%s)" % url4)

    st.subheader('Special thanks:')
    st.write("- Amanda, Christophe, Julio, Marie, Mohamad, Vinny, Yannis, Yassine")
    st.write("- and all lecturers and TAs at Le Wagon London")
    url7 = 'https://emoji-maker.com/'
    st.write("- [Emoji App Studio](%s)" % url7)

    st.markdown("![Alt Text](https://i.imgur.com/aRT5t36.gif)")

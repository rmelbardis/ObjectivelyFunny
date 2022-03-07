import streamlit as st
from PIL import Image
import os


# new_title = '<p style="font-family:sans-serif; color:White; font-size: 80px;">Examples</p>'
# st.markdown(new_title, unsafe_allow_html=True)

'''
# ☁ Some examples of word clouds
------------------------------
'''

CSS = """
h1 {
    color: white;
}
p {
    color: white;
    font-size: 30px;
    font-family: monospace;
}
.stApp {
    background-image: url(https://thumbs.dreamstime.com/b/stand-up-comedy-show-microphone-stool-ray-spotlight-brick-wall-161788000.jpg);
    background-size: cover;
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


st.write('Which decade would you like to see? 🤔')

option = st.selectbox(
    '',
    ('1960s', '1970s', '1980s', '1990s','2000s','2010s','2020s'))

st.write('You selected:', option)

option = option.replace('s', '')
image = Image.open(f'../ObjectivelyFunny/cloud-images/{option}_cloud.png')
# image = Image.open('../ObjectivelyFunny/images/emoji.png')

"""
    ---------------------------------
"""
if st.button('Generate'):
    st.write('Results generated 🎉')
    'Here is your cloud:'
    st.image(image, width=800, caption=f'{option}s word cloud')
else:
    st.write('Cloud not generated yet 😞')

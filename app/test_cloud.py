import streamlit as st
from PIL import Image

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
    background-image: url(https://i.ibb.co/H4FjXXj/27598206.jpg);
    background-size: cover;
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

option = st.selectbox(
    'Gender',
    ('Female', 'Male', 'Gender queer', 'All'))

st.write('🤔 You selected:', option)

option = st.selectbox(
    'Age',
    ('Under 25', '26-35', '36-45', 'Over 45'))

st.write('🤔 You selected:', option)

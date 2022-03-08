import streamlit as st
from PIL import Image

def app():
    '''
    # ☁ About
    ------------------------------
    '''
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.write('Please message Rei if you have any questions or just scream help.')

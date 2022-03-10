import streamlit as st
from PIL import Image

def app():
    '''
    # ☁ Gender Clouds
    ------------------------------
    '''
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("<h1 style='text-align: center; font-family: sans-serif; color: white;'>Ladies</h1>",
                    unsafe_allow_html=True)
            for i in range(1, 5):
                image = Image.open(f'word-clouds/Ladies{i}.png')
                st.image(image, width=300)


        with col2:
            st.markdown("<h1 style='text-align: center; font-family: sans-serif; color: white;'>Gentlemen</h1>",
                    unsafe_allow_html=True)
            for i in range(1, 5):
                image = Image.open(f'word-clouds/Gentlemen{i}.png')
                st.image(image, width=300)

        with col3:
            st.markdown("<h1 style='text-align: center; font-family: sans-serif; color: white;'>Gender Queer</h1>",
                    unsafe_allow_html=True)
            for i in range(1, 5):
                image = Image.open(f'word-clouds/Genderqueer{i}.png')
                st.image(image, width=300)

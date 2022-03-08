import streamlit as st
from PIL import Image

def app():
    '''
    # ☁ Gender Clouds
    ------------------------------
    '''
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            image1 = Image.open(f'../cloud-images/artist_gender_1_cloud.png')
            st.markdown("<h1 style='text-align: center; font-family: sans-serif; color: white;'>Ladies</h1>",
                    unsafe_allow_html=True)
            st.image(image1, width=550)

        with col2:
            image2 = Image.open(f'../cloud-images/artist_gender_2_cloud.png')
            st.markdown("<h1 style='text-align: center; font-family: sans-serif; color: white;'>Gentlemen</h1>",
                    unsafe_allow_html=True)
            st.image(image2, width=550)

        image3 = Image.open(f'../cloud-images/artist_gender_3_cloud.png')
        st.markdown("<h1 style='text-align: center; font-family: sans-serif; color: white;'>Gender Queer</h1>",
                    unsafe_allow_html=True)
        st.image(image3, width=550)

import streamlit as st
from PIL import Image
import age_cloud, decade_cloud, gender_cloud
import pandas as pd
from multipage import MultiPage

def app():
    # '''
    # # ☁ Choose your clouds
    # ------------------------------
    # '''
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    app = MultiPage()

    app.add_page("Age", age_cloud.app)
    app.add_page("Decade", decade_cloud.app)
    app.add_page("Gender", gender_cloud.app)

    app.run()

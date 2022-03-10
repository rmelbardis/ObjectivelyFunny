import streamlit as st
import age_cloud, decade_cloud, gender_cloud
from multipage import MultiPage

def app():
    with open('styles/cloud_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    app = MultiPage()

    app.add_page("Age", age_cloud.app)
    app.add_page("Decade", decade_cloud.app)
    app.add_page("Gender", gender_cloud.app)

    app.run()

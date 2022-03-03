# Streamlit Test

import streamlit as st
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

st.title('Comedy Topics Test')
st. markdown("""
This app performs Word Cloud
* **Python libraries:** streamlit, pandas, Wordcloud..
""")

st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.header("Select Gender")
genders = ['Female', 'Male', 'Genderqueer']

st.sidebar.header("Select Age")
ages = ['18-24', '25-30', '31-35', '36-40', '41-45', '46-50', '51-55', '56-60', '61-65', '66-70']

st.sidebar.header("Select Decade")
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

gender_query = st.sidebar.selectbox('Gender', genders)
age_query = st.sidebar.selectbox('Age', ages)
decade_query = st.sidebar.selectbox('Decade', decades)

st.sidebar.header("Select No. of words you want to display")
words = st.sidebar.selectbox("No. of words", range(10, 1000, 10))

if genders is not None:
    wordcloud = WordCloud(background_color = "white", max_words =
              words,stopwords = stopwords).generate(cleaned_textss)

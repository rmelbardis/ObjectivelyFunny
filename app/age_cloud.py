import streamlit as st
from PIL import Image

'''
# ☁ Compare word clouds by age groups
------------------------------
'''
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

add_selectbox = st.sidebar.selectbox(
    "Jump to",
    ("Main", "About", "Comedy Bot", "Clouds")
)

age_group_dict = {'Under 30': 'U30',
                  '30-39': '30',
                  '40-49': '40',
                  '50-59': '50',
                  '60-69': '60',
                  'Over 60': 'U60'}

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        option1 = st.selectbox(
        '',
        ('Under 30', '30-39', '40-49', '50-59', '60-69', 'Over 60'),
        key=1)
        st.write('Age group １:', option1)
        result1= age_group_dict[option1]

    with col2:
        option2 = st.selectbox(
        '',
        ('Under 30', '30-39', '40-49', '50-59', '60-69', 'Over 60'),
        key=2)
        st.write('Age group ２:', option2)
        result2= age_group_dict[option2]


    image1 = Image.open(f'../cloud-images/{result1}_cloud.png')

    if option1 == option2:
        st.warning('Change one of your options to compare different age groups')
        if st.button('Continue with one age group'):
            st.write('Results generated 🎉')
            st.header(f'People aged {option1}')
            st.image(image1, width=700)
        else:
            st.write('😞 Cloud not generated yet.')

    else:
        image2 = Image.open(f'../cloud-images/{result2}_cloud.png')

        col1, col2 = st.columns(2)

        """
            ---------------------------------
        """
        if st.button('Generate'):
            st.write('Results generated 🎉')
            """
            ---------------------------------
            """
            with col1:
                st.header(f'People aged {option1}')
                st.image(image1, width=550)
            with col2:
                st.header(f'People aged {option2}')
                st.image(image2, width=550)
        else:
            st.write('😞 Cloud not generated yet.')

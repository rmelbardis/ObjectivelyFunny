import streamlit as st
from PIL import Image

'''
# ☁ Compare word clouds by age groups
------------------------------
'''

def app():
    age_group_dict = {'Under 30': 'U30',
                    '30-39': '30',
                    '40-49': '40',
                    '50-59': '50',
                    'Over 60': 'O60'}

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            option1 = st.selectbox(
            '',
            ('Under 30', '30-39', '40-49', '50-59', 'Over 60'),
            key=1)
            st.write('Age group １:', option1)
            result1= age_group_dict[option1]

        with col2:
            option2 = st.selectbox(
            '',
            ('Under 30', '30-39', '40-49', '50-59', 'Over 60'),
            key=2)
            st.write('Age group ２:', option2)
            result2= age_group_dict[option2]

        st.write('-----------')

        image1 = Image.open(f'word-clouds/{result1}_cloud.png')

        if option1 == option2:
            st.warning('Change one of your options to compare different age groups')
            if st.button('Continue with one age group'):
                st.write('Results generated 🎉')
                st.header(f'People aged {option1}')
                st.image(image1, width=700)
            else:
                st.write('😞 Cloud not generated yet.')

        else:
            image2 = Image.open(f'word-clouds/{result2}_cloud.png')

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
                    st.image(image1, width=500)
                with col2:
                    st.header(f'People aged {option2}')
                    st.image(image2, width=500)
            else:
                st.write('😞 Cloud not generated yet.')

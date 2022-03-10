import streamlit as st
from PIL import Image

def app():
    '''
    # ☁ Compare word clouds by decades
    ------------------------------
    '''
    with st.container():
        st.write('⌛ Which decades do you want to compare?')

        col1, col2 = st.columns(2)

        with col1:
            option1 = st.slider('Select the first decade', min_value=1980,
                                max_value =2020, step=10, key=1)
            if option1==1980:
                # 1980 here is equivalent to 1989 in the dataframe
                # which was used to represent before 1990
                st.write('Decade １:', 'before 1990')
                option2=1989
            else:
                st.write('Decade １:', f'{option1}s')

        with col2:
            option2 = st.slider('Select the second decade', min_value=1980,
                                max_value =2020, step=10, key=2)
            if option2==1980:
                # 1980 here is equivalent to 1989 in the dataframe
                # which was used to represent before 1990
                st.write('Decade ２:', 'before 1990')
                option2=1989
            else:
                st.write('Decade ２:', f'{option2}s')

        image1 = Image.open(f'                      cloud-images/{option1}_cloud.png')

        if option1 == option2:
            st.warning('Change one of your options to compare different decades')
            """
                ---------------------------------
            """
            if st.button('Continue with one decade'):
                st.write('Results generated 🎉')
                st.image(image1, width=700, caption=f'{option1}s word cloud')
            else:
                """
                ---------------------------------
                """
                st.write('😞 Cloud not generated yet.')

        else:
            image2 = Image.open(f'cloud-images/{option2}_cloud.png')

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
                    st.image(image1, width=550, caption=f'{option1}s word cloud')
                with col2:
                    st.image(image2, width=550, caption=f'{option2}s word cloud')
            else:
                st.write('😞 Cloud not generated yet.')

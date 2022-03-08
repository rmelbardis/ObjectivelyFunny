import streamlit as st
from PIL import Image

'''
# ☁ Compare decade word clouds
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


st.write('⌛ Which decades do you want to compare')

col1, col2 = st.columns(2)

with col1:
    option1 = st.selectbox(
     '',
     ('Under 30', '30-40', '41-50', '51-60', 'Over 60'))
    st.write('Age group １:', option1)

with col2:
    option2 = st.slider('Select the second age group', min_value=1980,  max_value =2020,
                    step=10, key=2)
    st.write('Age group ２:', option2)

image1 = Image.open(f'../cloud-images/{option1}_cloud.png')

if option1 == option2:
    st.warning('Change one of your options to compare different decades')
    if st.button('Continue with one decade'):
        st.write('Results generated 🎉')
        st.image(image1, width=500, caption=f'{option1}s word cloud')
    else:
        st.write('😞 Cloud not generated yet.')

else:
    image2 = Image.open(f'../cloud-images/{option2}_cloud.png')
    # image = Image.open('../ObjectivelyFunny/images/emoji.png')


    col1, col2 = st.columns(2)


    """
        ---------------------------------
    """
    if st.button('Generate'):
        st.write('Results generated 🎉')
        'Here is your cloud:'
        with col1:
            st.header("pic1")
            st.image(image1, width=300, caption=f'{option1}s word cloud')
        with col2:
            st.header("pic2")
            st.image(image2, width=300, caption=f'{option2}s word cloud')
    else:
        st.write('😞 Cloud not generated yet.')

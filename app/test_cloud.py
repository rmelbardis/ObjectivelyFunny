import streamlit as st
from PIL import Image


# new_title = '<p style="font-family:sans-serif; color:White; font-size: 80px;">Examples</p>'
# st.markdown(new_title, unsafe_allow_html=True)

option = st.selectbox(
    'Gender',
    ('Female', 'Male', 'Gender queer', 'All'))

st.write('🤔 You selected:', option)

option = st.selectbox(
    'Age',
    ('Under 25', '26-35', '36-45', 'Over 45'))

st.write('🤔 You selected:', option)

'''
# ☁ Some examples of word clouds
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


st.write('⌛ Which decade would you like to see?')

option = st.selectbox(
    '',
    ('1960s', '1970s', '1980s', '1990s','2000s','2010s','2020s'))

st.write('🤔 You selected:', option)

option = option.replace('s', '')
image = Image.open(f'../cloud-images/{option}_cloud.png')
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
        st.write('another pic?')
    with col2:
        st.header("pic2")
        st.image(image, width=500, caption=f'{option}s word cloud')
else:
    st.write('😞 Cloud not generated yet.')

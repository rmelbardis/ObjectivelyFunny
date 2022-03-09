import streamlit as st

def app():
    with open('about_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    '''
    ------------------------------
    '''
    
    st.write('Welcome to our home page.')

    st.write('Please message Rei if you have any questions or just scream help.')

# https://i.ibb.co/p21Hz91/rob-laughter-WW1js-In-Xgw-M-unsplash.jpg

#     @import url(http://fonts.googleapis.com/css?family=Roboto:400,100,100italic,300,300ita‌​lic,400italic,500,500italic,700,700italic,900italic,900);
# html, body, html * {
#   font-family: 'Roboto', sans-serif;
# }

import streamlit as st

def app():
    with open('bot_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    text_input= st.text_input('Type below', 'Hello hello hello')
    st.write(f'{len(text_input)} characters')

    if st.button('play'):
        st.write('We are not ready yet')

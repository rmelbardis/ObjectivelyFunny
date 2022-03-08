import streamlit as st

def app():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
    title = st.text_input('Type below', 'Hello hello hello')
    if st.button('play'):
        st.write('nothing is ready yet')

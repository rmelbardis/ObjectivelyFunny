import streamlit as st
from multipage import MultiPage
import about, cloud_land, bot
from PIL import Image

# Create an instance of the app
app = MultiPage()

# Title of the main page
col1, col2 = st.columns(2)

with col1:
    st.title("Objectively Funny")

# Add all your applications (pages) here
app.add_page("About",about.app)
app.add_page("Clouds",cloud_land.app)
app.add_page("Bot",bot.app)

# The main app
app.run()

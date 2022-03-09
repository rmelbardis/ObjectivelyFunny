import streamlit as st
from PIL import Image
from multipage import MultiPage
import about, cloud_land, bot

# Import the required module for text
# to speech conversion
#from gtts import gTTS

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Objectively Funny")

# Add all your applications (pages) here
app.add_page("About",about.app)
app.add_page("Clouds",cloud_land.app)
app.add_page("Bot",bot.app)

# The main app
app.run()

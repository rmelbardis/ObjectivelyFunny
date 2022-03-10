import time
import requests
from gtts import gTTS
from datetime import timedelta

API_URL = 'https://obj-fun-2-2g6nxe3ofq-ew.a.run.app/comedian'

def generate_text(text):
    text = str(text)
    params = {'prefix': text}
    start_time = time.monotonic()
    response = requests.get(API_URL, params=params)
    end_time = time.monotonic()
    time_difference = timedelta(seconds=end_time - start_time).seconds
    message = f"Finished in {time_difference} seconds"
    a = response.json()
    return a, message

def get_jokes(a):
    bot_says = str(a['lines'])
    joke1 = str(a['lines'][0])
    joke2 = str(a['lines'][1])
    joke3 = str(a['lines'][2])
    return bot_says, joke1, joke2, joke3

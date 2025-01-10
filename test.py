import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Load a Lottie animation from a URL
lottie_animation = load_lottie_url("https://lottie.host/291c3c67-ed2d-48db-abb6-f5b86cef2d07/hl1SzeIeW3.json")

# Display the animation in Streamlit
st.title("Lottie Animation Example")
if lottie_animation:
    st_lottie(lottie_animation, height=300, key="example")
else:
    st.error("Failed to load animation.")

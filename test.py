import requests
import streamlit as st
from pathlib import Path
from PIL import Image



# profile_pic = Image.open('/home/micheal/Documents/GitHub/Streamlit_Resume/MY_RESUME/assets/CertificateOfCompletion_Python Essential Training_page-0001.png')



# profile_pic = Image.open(profile_pic)

# st.image (profile_pic, width=230)

import streamlit as st
from PIL import Image
import os

# Path to the image
file_path = os.path.expanduser('~/Documents/GitHub/Streamlit_Resume/MY_RESUME/assets/CertificateOfCompletion_Python Essential Training_page-0001.png')

# Check if the file exists
if os.path.exists(file_path):
    st.write("File exists, attempting to open...")
    profile_pic = Image.open(file_path)
    st.image(profile_pic, caption="Profile Picture", use_column_width=True)  # Render image in the web app
    st.write("Image loaded successfully!")
else:
    st.write(f"File not found at: {file_path}")

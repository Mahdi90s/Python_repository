import streamlit as st
# from streamlit_lottie import st_lottie
import requests

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import seaborn as sns
from sklearn.datasets import load_iris

# def load_lottie_url(url: str):
#     response = requests.get(url)
#     if response.status_code != 200:
#         return None
#     return response.json()

# # Load a Lottie animation from a URL
# lottie_animation = load_lottie_url("https://lottie.host/291c3c67-ed2d-48db-abb6-f5b86cef2d07/hl1SzeIeW3.json")

# # Display the animation in Streamlit
# st.title("Lottie Animation Example")
# if lottie_animation:
#     st_lottie(lottie_animation, height=300, key="example")
# else:
#     st.error("Failed to load animation.")


# Line charts in Streamlit
# Create a line chart which we'll grow overtime

rows = np.random.randn(1,1)

'Growing Line Chart:'
Chart = st.line_chart(rows)

for i in range(1,100):
    new_rows = rows[0] + np.random.randn(1,1)
    # add rows method
    Chart.add_rows(new_rows)
    rows = new_rows
    time.sleep(0.05) # to stop it for 5 milscond
    
    
    values = np.random.rand(10)
    'Matplotlibs Line Chart:'
    fig, ax = plt.subplots()
    ax.plot(values)
    st.pyplot(fig)
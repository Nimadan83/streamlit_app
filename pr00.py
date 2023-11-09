import os 
from deepface import DeepFace
import streamlit as st
import numpy as np
from PIL import Image 
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title = 'my web app', page_icon = ":tada", layout = 'wide')

def loud_lt(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
x = loud_lt('https://lottie.host/65356586-262b-4376-8bef-7a66963cdcc2/6LxVvEdmSJ.json')


st.header('What this site do?')


nu = st.button('show me')
if nu:
    st.write("With this site you can see which celebrity you look like, just upload your photobelow and wait a few moments.")
image1 = st.file_uploader("Upload Image 1", type=["jpg", "jpeg", "png"])

if image1 is not None:
    st.image(image1)
    img1 = np.array(Image.open(image1))

st_lottie(x,height = 200)

def img(img_1):
    smallest_dir = None
    for file in os.listdir('new_database'):
        if file.endswith(".jpg"):
            w = f"new_database/{file}"
            x = DeepFace.verify(img_1, w)
            if x['verified']:
                st.write("to khode ", file.split('.')[0], "hasti")
                IMAGE = Image.open(w)
                st.image(IMAGE)
                break
            if smallest_dir is None:
                smallest_dir = (file.split('.')[0], x['distance'])
            else:
                smallest_dir = (file.split('.')[0], x['distance']) if x['distance'] < smallest_dir[1] else smallest_dir
    else:
        st.write(f"to shabihe  {smallest_dir[0]} hasti")
        IMAGE = Image.open(f"new_database/{smallest_dir[0]}.jpg")
        st.image(IMAGE)
        
        
clic = st.button('click my')

if clic:
    img(img1)


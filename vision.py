from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load gemini pro model and get responses

#gemini pro is used for text
#geminipro vision is used for image
model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input, image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text


#initialize streamlit app

st.set_page_config(page_title = "Gemini Image Demo")
st.header("Gemini Image application")
input = st.text_input("Input: ", key="input") ##input text box
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image =""
##when submiy is clicked

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)


submit = st.button("Tell me about the image")

##if submit is clicked
if submit:
    response = get_gemini_response(input,image)
    st.write(response)

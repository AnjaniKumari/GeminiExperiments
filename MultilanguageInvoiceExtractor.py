from dotenv import load_dotenv
##loading all the environment variables from .env
load_dotenv() 

#streamlit is framework for building app quickly
import streamlit as st

import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini pro vision
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,image,prompt):
    # print("input",input)
    # print("image",image)
    # print("prompt===>",prompt)
    response = model.generate_content([input, image[0], prompt])
    # print(response)
    return response.text

#initilize streamlit app
st.set_page_config(page_title="MultiLanguage Invoice Exractor")
input = st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice",type=["jpeg","png","jpg"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)


submit = st.button("Tell me about the invoice")
input_prompt = """
You are an expert in understanding invpices. WE will upload an image as invoice an dyou will have to answer any question based on the uploaded invoice image.
"""

#convert the uploaded file to bite
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        #read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts= [
            {
                "mime_type": uploaded_file.type, #get the mime type of the uploaded file
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


# if submit button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The response is")
    st.write(response)
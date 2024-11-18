from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load gemini pro model and get responses

#gemini pro is used for text
#geminipro vision is used for image
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


#initialize streamlit app

st.set_page_config(page_title = "Q&A demo")
st.header("Gemini application")
input = st.text_input("Input: ", key="input") ##input text box
submit = st.button("Ask the  Question")

##when submiy is clicked

if submit:
    response = get_gemini_response(input)
    st.write(response)
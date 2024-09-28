from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
def my_output(query):
    response=model.generate_content(query)
    return response.text
st.set_page_config(page_title="MY CHAT BOT")
st.header("MY CHAT BOT")
input=st.text_input("Input",key="input")
submit=st.button("Ask")
if submit:
    response=my_output(input)
    st.subheader("YOUR ANSWER:")
    st.write(response)
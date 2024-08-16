import streamlit as st
import google.generativeai as genai

API_KEY = "Add your API KEY"  

genai.configure(api_key = API_KEY)

#initializing model 

model = genai.GenerativeModel('gemini-1.5-flash')

def getResponse(user_input):
    response = model.generate_content(user_input)
    return response.text


st.title("Gemini Chatbot")

user_input = st.text_input("Enter your Prompt: ")

if st.button("Get Response"):
    if user_input:
        output = getResponse(user_input)
        st.write(f'Chatbot Response: {output}')
        
    else:
        st.write("Please enter a Prompt")

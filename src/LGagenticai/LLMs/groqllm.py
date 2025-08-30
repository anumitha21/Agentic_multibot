#read groq api key
# we have to read from the frontend
import os
from langchain_groq import ChatGroq
import streamlit as st

class groqllm:
    def __init__(self,user_control_input):#init user controls
        self.user_control_input=user_control_input#to get the input

    #to load the model

    def get_llm_model(self):
        try:
            groq_api_key = self.user_control_input.get("GROQ_API_KEY", "")
            selected_groq_model = self.user_control_input.get('selected_groq_model', "")
            
            # Check if API key is provided
            if not groq_api_key:
                st.error("Please enter your GROQ API key")
                return None
            
            # Check if model is selected
            if not selected_groq_model:
                st.error("Please select a GROQ model")
                return None

            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
            return llm

        except Exception as e:
            st.error(f"Error occurred with LLM initialization: {e}")
            return None
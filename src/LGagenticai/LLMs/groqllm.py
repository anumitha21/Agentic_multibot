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
            groq_api_key = self.user_control_input["GROQ_API_KEY"]
            selected_groq_model = self.user_control_input['selected_groq_model']
            if groq_api_key=='' and os.environ["GROQ_API_KEY"]=="":
                st.error("Please enter your GROQ API key")

            llm = ChatGroq(api_key=groq_api_key,model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error occured wih Exception : {e}")
        return llm
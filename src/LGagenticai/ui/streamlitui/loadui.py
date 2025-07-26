#load ui parts of the page

import streamlit as st
import os

from src.LGagenticai.ui.streamlitui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config() # should loadallt eh config
        self.user_control={} # this will hold all the user controls

    def loadstreamlitui(self):
        st.set_page_config(page_title=" 🤖  " + self.config.get_page_title(),layout="wide")
        st.header(" 👾 🤖  " + self.config.get_page_title())
        

        with st.sidebar:
            #get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            
            #LLM selection
            self.user_control["selected_llm"] =st.selectbox("Select LLM",llm_options)
            
            if self.user_control["selected_llm"] == "Groq":
               #Model selection
               model_options = self.config.get_groq_options()
               self.user_control["selected_groq_model"] = st.selectbox("Select Model",model_options)
               self.user_control["GROQ_API_KEY"]=st.session_state["GROQ_API_KEY"]=st.text_input("API KEY",type="password")

               #warining  validate api key

               if not self.user_control["GROQ_API_KEY"]:
                   st.warning("Please enter ypur groq api key to proceed")


              ## use case selection
            self.user_control["selected_usecase"] = st.selectbox("Select Use Case",usecase_options)
    
        return self.user_control
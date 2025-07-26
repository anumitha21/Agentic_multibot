#displays the result

import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage,BaseMessage
import json


class Displayresultstreamlit:
    def __init__(self,usercase, graph, user_message):
        self.usercase = usercase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usercase=self.usercase
        graph=self.graph
        user_message=self.user_message
        print(user_message)
        if usercase == "Basic Chatbot":
                for event in graph.stream({'messages':("user",user_message)}): # streaming responses from a LangGraph
                ##for event in graph.stream({'messages': [HumanMessage(content=user_message)]}):
                    print(event.values()) # This prints the full internal contents of the event in the console 
                    for value in event.values():
                        print(value['messages']) # console output, not shown in the UI.
                        with st.chat_message("user"):
                            st.write(user_message) # prints the user message in the 
                        with st.chat_message("assistant"):
                            st.write(value['messages'].content) # prints the chatout message in the UI
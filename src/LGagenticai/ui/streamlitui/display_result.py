#displays the result
import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
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
            try:
                for event in graph.stream({'messages': [("user", user_message)]}):
                    for value in event.values():
                        if 'messages' in value and value['messages']:
                            message = value['messages'][-1] if isinstance(value['messages'], list) else value['messages']
                            with st.chat_message("assistant"):
                                st.write(message.content)
            except Exception as e:
                st.error(f"Error in basic chatbot: {str(e)}")
        
        elif usercase == "Chatbot with Web Search":
        # Prepare state and invoke the graph
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)

            for message in res['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)

                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")

                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                       st.write(message.content)

        elif usercase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news... ⏳"):
                result = graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")





                            
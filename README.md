# 🤖 Agentic AI Chatbot


## 📝Project Description 
LangGraph Agentic AI is an AI application featuring a Streamlit-based user interface that leverages large language models (LLMs) and graph-based processing to handle user-selected use cases. The application allows users to input their thoughts, configures an LLM model accordingly, builds a graph structure based on the selected use case, and displays the results interactively through the Streamlit UI.

## ✨ Features 
- Interactive Streamlit UI for user input and interaction
- Integration with LLM models for natural language processing
- Graph-based setup and processing tailored to specific use cases
- Robust exception handling for a smooth user experience

## 🛠️ Technologies & Libraries Used
This project leverages the following tools and libraries to build an Agentic AI Chatbot:

- Python – Core programming language
- Streamlit – Interactive web UI
- LangChain – Framework for developing LLM-powered applications
- LangGraph – Multi-agent orchestration and graph-based workflow engine
- Groq – LLM providers integrated for various model support
- Pydantic – Data validation and management using Python type hints

## 🛠️ Installation 

1. It is recommended to create a Python virtual environment:
   ```bash
   python -m venv penv
   source penv/Scripts/activate   # On Windows
   # or
   source penv/bin/activate       # On Unix or MacOS
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Requirements 

Key dependencies are listed in `requirements.txt` and include:
- langchain_community
- langchain_core
- langgraph
- langchain
- langchain_groq
- streamlit

## ▶️ Usage 

Run the application by executing the following command in the project root directory:

```bash
python app.py
```

This will launch the Streamlit UI where you can enter your input, select use cases, and interact with the AI agent.

## 📁 Project Structure

```
.
├── app.py                             # Main entry point to run the application
├── src/
│   └── LGagenticai/
│       ├── main.py                   # Loads and runs the LangGraph Agentic AI application
│       ├── LLMs/                     # Modules related to LLM configuration and interaction
│       ├── graph/                    # Graph builder modules for use case-specific LangGraph flows
│       ├── nodes/                    # Individual node definitions used in the graph processing
│       ├── state/                    # State management for maintaining agent memory and context
│       ├── tools/                    # Utility tools used across the application
│       └── ui/
│           └── streamlitui/          # Streamlit UI components and layout configurations
```


## 📄 License 

This project is licensed under the terms of the MIT License.

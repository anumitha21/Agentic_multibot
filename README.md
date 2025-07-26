# 🤖  Agentic AI Chatbot

## 🧠 Overview

**LangGraph Agentic AI** is an intelligent, agent-based AI chatbot framework built using **LangGraph**, **LangChain**, and **Streamlit**. It enables users to interact with LLMs (such as OpenAI or Groq models) through a user-friendly graphical interface and dynamic agent workflows defined as graphs.

This project serves as a template for building highly customizable AI agents, each capable of handling unique user-defined use cases by combining tools, memory, reasoning, and conversational interfaces.

---

## 🚀 Key Features

* **Streamlit UI**: Interactive, responsive front-end for selecting LLMs, use cases, and entering queries.
* **Modular Agent Graph**: Each use case is implemented as a distinct graph composed of nodes (tools, retrievers, memory modules, and logic).
* **State Management**: Built-in memory and state tracking for multi-turn interactions.
* **Tool & LLM Integration**: Easily plug in tools (retrievers, calculators, etc.) and switch between LLMs like OpenAI, Groq, and more.
* **Extensible Architecture**: Easily extend nodes, state logic, or graph workflows for new use cases.
* **Use Case-Aware Agents**: Automatically adjust flow and responses based on user-selected use cases.
* **Robust Error Handling**: Warnings and fallback paths for unsupported inputs or configuration issues.

---
📁 Project Structure

├── app.py                         # Main entry point to run the application.
└── src/
    └── LGagenticai/
        ├── main.py               # Loads and runs the LangGraph Agentic AI application.
        ├── LLMs/                 # Contains modules related to large language models configuration.
        ├── graph/                # Graph builder modules for setting up use case-specific graphs.
        ├── nodes/                # Node definitions used in the graph processing.
        ├── state/                # State management modules.
        ├── tools/                # Utility tools used across the application.
        └── ui/
            └── streamlitui/      # Streamlit UI components and configuration files.

---

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/langgraph-agentic-ai.git
   cd langgraph-agentic-ai
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv penv
   penv\Scripts\activate   # Windows
   # or
   source penv/bin/activate  # Mac/Linux
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Dependencies

Key dependencies are listed in requirements.txt and include:
- langchain_community
- langchain_core
- langgraph
- langchain
- langchain_groq
- streamlit

## ▶️ Running the App

Launch the app from the project root:

```bash
streamlit run app.py
```
-- 

## ✏️ How It Works

1. **User selects** a model and use case in the Streamlit UI.
2. `main.py` dynamically builds a **LangGraph graph** with nodes specific to the use case.
3. Nodes process the user query via **tools, retrievers, graders**, or **rewriters**.
4. Final response is generated and returned in the Streamlit app.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

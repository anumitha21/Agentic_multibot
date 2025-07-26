# LangGraph Agentic AI 🤖🚀

## Project Description 📝
LangGraph Agentic AI is an AI application featuring a Streamlit-based user interface that leverages large language models (LLMs) and graph-based processing to handle user-selected use cases. The application allows users to input their thoughts, configures an LLM model accordingly, builds a graph structure based on the selected use case, and displays the results interactively through the Streamlit UI.

## Features ✨
- Interactive Streamlit UI for user input and interaction
- Integration with LLM models for natural language processing
- Graph-based setup and processing tailored to specific use cases
- Robust exception handling for a smooth user experience

## Installation 🛠️

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

## Usage ▶️

Run the application by executing the following command in the project root directory:

```bash
python app.py
```

This will launch the Streamlit UI where you can enter your input, select use cases, and interact with the AI agent.

## Project Structure 📁

- `app.py`: Main entry point to run the application.
- `src/LGagenticai/`: Core source code directory containing:
  - `main.py`: Loads and runs the LangGraph Agentic AI application.
  - `LLMs/`: Contains modules related to large language models configuration.
  - `graph/`: Graph builder modules for setting up use case-specific graphs.
  - `nodes/`: Node definitions used in the graph processing.
  - `state/`: State management modules.
  - `tools/`: Utility tools used across the application.
  - `ui/streamlitui/`: Streamlit UI components and configuration files.

## Dependencies 📦

Key dependencies are listed in `requirements.txt` and include:
- langchain_community
- langchain_core
- langgraph
- langchain
- langchain_groq
- faiss-cpu
- tavily-python
- streamlit

## License 📄

This project is licensed under the terms of the MIT License.

## Contribution 🤝

Contributions are welcome. Please open issues or submit pull requests for improvements or bug fixes.

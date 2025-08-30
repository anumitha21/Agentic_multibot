## In this folder all the components will be called here, i.e the folder we have created under LGagenticai
# We are making a connection from loadui.py
import streamlit as st
from src.LGagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.LGagenticai.LLMs.groqllm import groqllm
from src.LGagenticai.graph.gbuilder import builder
from src.LGagenticai.ui.streamlitui.display_result import Displayresultstreamlit

def load_lg_agenticai_app():
    """
    Loads and runs the langgrpah agentic ai application with streamlit UI.
    This function intializes the UI , handles user input , configures the LLM model,
    sets up the graph based on the selected use case , and displays the output , while implementing the 
    exception handling for robustness.

    """

    ## load ui
    # Initialize session state variables if they don't exist
    if 'IsFetchButtonClicked' not in st.session_state:
        st.session_state.IsFetchButtonClicked = False
    if 'timeframe' not in st.session_state:
        st.session_state.timeframe = None

    ui = LoadStreamlitUI()
    user_input = ui.loadstreamlitui()

    if not user_input:
        st.error("Please select and enter the input text")
        return
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your thought")

    if user_message:
        try:
            # load the model
            obj_llm_config = groqllm(user_control_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized")
                return
          
            # Initialize and set up the graph based on the use_case
            usercase = user_input.get("selected_usecase")

            if not usercase:
                st.error("Error: No usecase selected.")
                return
          
            # Graph builder
            graph_builder = builder(model)
            try:
                graph = graph_builder.setup_graph(usercase)
                Displayresultstreamlit(usercase, graph, user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error: Graph setup failed. {e}")
                return
          
        except Exception as e:
            st.error(f"Error: Application failed. {e}")
            return



            



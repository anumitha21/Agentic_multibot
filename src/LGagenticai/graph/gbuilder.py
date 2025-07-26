from langgraph.graph import StateGraph
from src.LGagenticai.state.state import State
from langgraph.graph import START,END
from src.LGagenticai.nodes.chatbot_node import botnode

class builder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def chatbot_graphbuilder(self):
        """
        Builds a basic chatbot using langgraph.
        Which answers users query neatly and clear
        this method intializes a chatbot node using the 'botnode' class
        and integrates into the graph. The chatbot node is set as both the 
        entry and point of the graph
        """
        self.chatbot_node = botnode(self.llm)
        
        self.graph_builder.add_node("chatbot",self.chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected usecase.

        """

        if usecase == "Basic Chatbot":
            self.chatbot_graphbuilder()
        return self.graph_builder.compile()

       


from langgraph.graph import StateGraph
from src.LGagenticai.state.state import State
from langgraph.graph import START,END
from src.LGagenticai.nodes.chatbot_node import botnode
from src.LGagenticai.tools.websearchtool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition,ToolNode
from src.LGagenticai.nodes.chatbot_tool import chatbotwithtool
from src.LGagenticai.nodes.ai_news import AInewsnode

class builder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def chatbot_graphbuilder(self):
        """
        Builds a basic chatbot using langgraph.
        
        """
        self.chatbot_node = botnode(self.llm)
        
        self.graph_builder.add_node("chatbot",self.chatbot_node.process)
        self.graph_builder.set_entry_point("chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_websearch(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
        #define tool and toolnode
        tools=get_tools()
        tool_node=create_tool_node(tools)

        #define the llm
        llm=self.llm


        #chatbot node
        obj_chatbottool = chatbotwithtool(llm)
        chatbot_node = obj_chatbottool.create_chatbot(tools)

         #add node
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        #define conditional and direct edge
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition) #it decides where to go...decision takes place here
        self.graph_builder.add_edge("tools","chatbot")
        ##self.graph_builder.add_edge("chatbot",END) #not necassary to write


    def ai_news_builder_graph(self):

        ai_newnode=AInewsnode(self.llm)
    
        ##add nodes

        self.graph_builder.add_node("Fetch_news",ai_newnode.fetch_news)
        self.graph_builder.add_node("News_summarizer",ai_newnode.summarize_news)
        self.graph_builder.add_node("save_result",ai_newnode.save_result)

        ##add edges
        ##insteadof starting with start..we can also do

        self.graph_builder.set_entry_point("Fetch_news")
        self.graph_builder.add_edge("Fetch_news","News_summarizer")
        self.graph_builder.add_edge("News_summarizer","save_result")
        self.graph_builder.add_edge("save_result",END)

    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected usecase.
        """
        # Create a new graph builder for each use case to prevent state conflicts
        self.graph_builder = StateGraph(State)
    
        if usecase == "Basic Chatbot":
            self.chatbot_graphbuilder()
    
        elif usecase == "Chatbot with Web Search":
            self.chatbot_with_websearch()
    
        elif usecase == "AI News":
            self.ai_news_builder_graph()
    
        return self.graph_builder.compile()



       


from src.LGagenticai.state.state import State

class chatbotwithtool:
    """
    chatbot logic enchanced with tool integration
    """

    def __init__(self,model):
        self.llm=model
  
    def process(self, state: State) -> dict: ##✅ Use process() when you just want to handle simple input-processing without real tools.
        ##if we dint have any tools
        """
        Processes the input state and generates a response with tool integration.
         """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        # Simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]} 


    def create_chatbot(self, tools): ## when you need a more flexible chatbot that can integrate with actual tools, 
      """
      Returns a chatbot node function.
      """
      llm_with_tools = self.llm.bind_tools(tools)

      def chatbot_node(state: State):
        """
            Chatbot logic for processing the input state and returning a response.
        """
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

      return chatbot_node



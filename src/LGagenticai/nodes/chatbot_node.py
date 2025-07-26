from src.LGagenticai.state.state import State


class botnode:
    """
    this is basic chatbot logic implementation

    """

    def __init__(self,model):
        self.llm = model

    def process(self,state:State)->dict:
        """
        processes the input state and generate a chatbot repsonse
        
        """
        return {"messages":self.llm.invoke(state['messages'])}
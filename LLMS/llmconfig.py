from LLMHandler.llmhandler import LLMHandler


class LLMConfig:
    def __init__(self,user_control):
        self.user_control = user_control
    def get_llm_config(self):
        
        user_control = self.user_control
        handler = LLMHandler(user_control)
        llm_config = handler.handle_request()
        
        return llm_config
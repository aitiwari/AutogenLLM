from LLMS.groqllm import GroqLLM
from LLMS.hfllm import get_hf_llmconfig
from LLMS.oaillm import OAILLM


class LLMHandler:
    def __init__(self, user_controls_input):
        self.user_control = user_controls_input
        self.api_type = user_controls_input.get('api_type')

    def handle_request(self):
        # Dispatch to the appropriate method based on api_type
        handler_method_name = f"{self.api_type}_handler"
        if hasattr(self, handler_method_name):
            handler_method = getattr(self, handler_method_name)
            handler_method()
        else:
            raise ValueError(f"Unsupported API type: {self.api_type}")
        
    def huggingface_handler(self):
        llm_config = get_hf_llmconfig()
        return llm_config

    def groq_handler(self):
        obj_llm_config = GroqLLM(user_controls_input=self.user_control)
        llm_config = obj_llm_config.groq_llm_config()
        return llm_config
    
    def common_handler(self):
        obj_llm_config = OAILLM(user_controls_input=self.user_control)
        obj_llm_config.oai_llm_config()

    def google_handler(self):
        self.common_handler()

    def mistral_handler(self):
        self.common_handler()

    def anthropic_handler(self):
        self.common_handler()

    def bedrock_handler(self):
        self.common_handler()

    def ollama_handler(self):
        self.common_handler()
    def together_handler(self):
        self.common_handler()
    
    def openai_handler(self):
        self.common_handler()



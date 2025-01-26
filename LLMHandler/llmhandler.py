from LLMS.groqllm import GroqLLM


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

    def groq_handler(self):
        obj_llm_config = GroqLLM(user_controls_input=self.user_control)
        llm_config = obj_llm_config.groq_llm_config()
        return llm_config

    # def google_handler(self):
    #     obj_llm_config = GoogleLLM(user_controls_input=self.user_control)
    #     obj_llm_config.google_llm_config()

    # def mistral_handler(self):
    #     obj_llm_config = MistralLLM(user_controls_input=self.user_control)
    #     obj_llm_config.mistral_llm_config()

    # def anthropic_handler(self):
    #     obj_llm_config = AnthropicLLM(user_controls_input=self.user_control)
    #     obj_llm_config.anthropic_llm_config()

    # def bedrock_handler(self):
    #     obj_llm_config = BedrockLLM(user_controls_input=self.user_control)
    #     obj_llm_config.bedrock_llm_config()

    # def ollama_handler(self):
    #     obj_llm_config = OllamaLLM(user_controls_input=self.user_control)
    #     obj_llm_config.ollama_llm_config()

    # def openai_handler(self):
    #     obj_llm_config = OpenAILLM(user_controls_input=self.user_control)
    #     obj_llm_config.openai_llm_config()



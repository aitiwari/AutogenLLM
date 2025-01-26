import streamlit as st
import json


class Streamlit_UI() :
    def __init__(self):
        pass
    
        
    # Function to load JSON files
    def load_json(self,file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading {file_path}: {e}")
            return []
    
    
    def load_streamlit_ui(self):
            
        # Load configuration files
        anthropic_file = "./LLMCONFIG/ANTROPIC_CLAUDE_CONFIG_LIST.json"
        google_file = "./LLMCONFIG/GOOGLE_GEMINI_CONFIG_LIST.json"
        mistral_file = "./LLMCONFIG/MISTRAL_AI_CONFIG_LIST.json"
        ollama_file = "./LLMCONFIG/OLLAMA_LLM_CONFIG_LIST.json"
        groq_file = "./LLMCONFIG/GROQ_CONFIG_LIST.json"
        bedrock_file = "./LLMCONFIG/BEDROCK_CONFIG_LIST.json"

        # Load model configurations
        anthropic_models = self.load_json(anthropic_file)
        google_models = self.load_json(google_file)
        mistral_models = self.load_json(mistral_file)
        ollama_models = self.load_json(ollama_file)
        groq_models = self.load_json(groq_file)
        bedrock_models = self.load_json(bedrock_file)

        # Combine all API types into a single dictionary
        api_data = {
            "anthropic": anthropic_models,
            "bedrock": bedrock_models,
            "google": google_models,
            "groq": groq_models,
            "mistral": mistral_models,
            "ollama": ollama_models,
            "openai": [],

        }
        user_inputs = {}
        
        with st.sidebar:

            # Streamlit UI
            st.title("LLM Configuraton ⚙️")

            # Dropdown to select API type
            user_inputs['api_type'] = api_type = st.selectbox("Select API Type", options=api_data.keys())

            # Input handling for OpenAI
            if api_type == "openai":
                st.write("### Provide OpenAI Configuration Details")
                selected_model_name = st.text_input("Enter Model Name", value="")
                st.session_state['api_key'] = st.text_input("Enter API Key", value="", type="password")
              

                # Display selected configuration
                st.write("### Selected Configuration")
                st.write(f"API Type: {api_type}")
                st.write(f"Model: {selected_model_name}")
                st.write("User Inputs:")
                st.json(user_inputs)

            else:
                # Get models based on selected API type
                selected_models = api_data.get(api_type, [])

                # Dropdown to select model
                model_names = [model["model"] for model in selected_models]
                selected_model_name = st.selectbox("Select Model", options=model_names)

                # Find the selected model configuration
                selected_model_config = next(
                    (model for model in selected_models if model["model"] == selected_model_name), {}
                )
                # Input fields for the selected model configuration
                st.write("### Provide Configuration Details")

                for key, value in selected_model_config.items():
                    if key not in ["api_type", "model"]:
                        # Use a password field for API keys, otherwise a text input
                        input_label = f"Enter {key}"
                        if "key" in key.lower():
                            st.session_state['api_key'] = user_inputs[key] = st.text_input(input_label, value="", type="password")
                        elif isinstance(value, bool):
                            user_inputs[key] = st.checkbox(input_label, value=value)
                        else:
                            user_inputs[key] = st.text_input(input_label, value=str(value))
                            
            user_inputs['selected_model_name']= selected_model_name 
            
        return user_inputs                
            
   
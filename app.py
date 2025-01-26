
import streamlit as st
from streamlitui.loadui import Streamlit_UI
from usecases.basicexample import BasicExample
from LLMS.llmconfig import LLMConfig

# MAIN Function START


if __name__ == "__main__":
    
        user_inputs_controls = Streamlit_UI().load_streamlit_ui()
        user_inputs_display = user_inputs_controls
        # Mask API key in displayed outputs
        # if "api_key" in user_inputs_controls:
        #     user_inputs_display["api_key"] = "*****"

        
        with st.sidebar:
            # Display selected configuration
            st.write("User Inputs:")
            st.json(user_inputs_display)

        # Basic usecasse :
        
        # userInput
        problem = st.chat_input("Start Chat")
        if problem : 
            # LLM Configuration
            LLMConfig(user_inputs_controls).get_llm_config()
            if 'config_list' in st.session_state['llm_config'] : 
                llm_config = st.session_state['llm_config']
            obj_basic_example = BasicExample(assistant_name="Assistant", user_proxy_name='Userproxy',
                                                        llm_config=llm_config,
                                                        problem=problem)
            obj_basic_example.run()

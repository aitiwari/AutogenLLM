
import streamlit as st
from streamlitui.loadui import Streamlit_UI
from usecases.basicexample import BasicExample
from usecases.basicexamplecustommodel import BasicExampleCustomModel
from LLMS.llmconfig import LLMConfig

# MAIN Function START


if __name__ == "__main__":
    
        user_inputs_controls = Streamlit_UI().load_streamlit_ui()
        user_inputs_display = user_inputs_controls

        # Basic usecasse :
        # user chat
        problem = st.chat_input("Start Chat")
        if problem : 
            # LLM Configuration
            LLMConfig(user_inputs_controls).get_llm_config()
            if 'config_list' in st.session_state['llm_config'] : 
                llm_config = st.session_state['llm_config']
            
            # for custom moddel condition     
            if user_inputs_controls['api_type']== "huggingface":
                with st.chat_message('user'):
                    st.write(problem)
                obj_basic_example_custom = BasicExampleCustomModel(assistant_name="Assistant", user_proxy_name='Userproxy',
                                                        llm_config=llm_config,
                                                        problem=problem)
                obj_basic_example_custom.run()
            
            else :
                    
                obj_basic_example = BasicExample(assistant_name="Assistant", user_proxy_name='Userproxy',
                                                            llm_config=llm_config,
                                                            problem=problem)
                obj_basic_example.run()

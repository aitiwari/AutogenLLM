import autogen
import os

import streamlit as st


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def groq_llm_config(self):
        config_list = [
            {
            "api_type": 'groq',
            "model": self.user_controls_input['selected_model_name'], 
            "api_key": st.session_state["api_key"],
            "cache_seed": None
            }
        ]

        llm_config = {"config_list": config_list, "request_timeout": 60}
        st.session_state['llm_config'] = llm_config
        return llm_config

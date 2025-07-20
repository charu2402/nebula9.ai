import streamlit as st
from agents.interviewer import load_conversation

def init_session_state():
    if 'interview_started' not in st.session_state:
        st.session_state['interview_started'] = False
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    if 'rounds' not in st.session_state:
        st.session_state['rounds'] = 0
    if 'conversation' not in st.session_state:
        st.session_state['conversation'] = load_conversation()

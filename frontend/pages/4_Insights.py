import streamlit as st
import importlib
import home
import feature_page
import mapping
import email
import streamlit.components.v1 as components
# import SessionState
from backend.repository import idea
import requests

def insights():
    st.title('Your Average Feedback ')
    # product ideas dropdown
    # options = st.session_state['idea_list']
    options = ['1','2','3','4']
    user_idea = st.selectbox("Select an option",options)
    token = st.session_state["authentication_status"]
    headers = {'Authorization': f'Bearer {token}'}
    payload_idea = {'idea':str(idea)}

    if user_idea:
        st.write('Your average feedback is') # ratings average
        st.write()
        st.write('Summary of the written feedbacks') # summary average
        st.write()

    
import streamlit as st
import streamlit as st
import pandas as pd
import os
import requests
import urllib
from streamlit_extras.switch_page_button import switch_page
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = False
if 'feature_status' not in st.session_state:
    st.session_state['feature_status'] = False
if 'fav_idea' not in st.session_state:
    st.session_state['fav_idea'] = ''
if 'mvp_status' not in st.session_state:
    st.session_state['mvp_status'] = False
if 'idea_list' not in st.session_state:
    st.session_state['idea_list'] = []
if 'feature_list' not in st.session_state:
    st.session_state['feature_list'] = []
# from streamlit import SessionState

def insights():
    st.title('Your Average Feedback for your Product')
    # product ideas dropdown
    # options = st.session_state['idea_list']
    options = st.session_state['idea_list']
    user_idea = st.selectbox("Select an option",options)
    
    

    if user_idea:
        token = st.session_state["authentication_status"]
        headers = {'Authorization': f'Bearer {token}'}
        payload_idea = {'idea':str(user_idea)}
        output = requests.get("http://localhost:8000/idea/get-insights-of-idea", params = payload_idea,headers=headers)
        if output.status_code == 200:
            result = output.json()
            rating = result['average_rating']  
            summary = result['feed_back']  
            st.write('Your average rating is') # ratings average
            st.write(rating)
            st.write('Summary of the written feedbacks') # summary average
            st.write(summary)

#     cutomer_insight = st.text_input()
if st.session_state["authentication_status"] == False:
    st.subheader("Please Login before use")
else:
    insights()
# # if st.button('Go to Home Page'):
# #     # SessionState.selected_page = 'Home'
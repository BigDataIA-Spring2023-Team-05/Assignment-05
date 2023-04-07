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
dict = st.experimental_get_query_params()
token = dict['token']
print(token)
def rating():

    #creating a ratings page where entering th
    st.write('Give your rating for the product idea :')
    rating = st.text_input('Enter your value out of 5 here') 
    st.write('Feedback')
    feed_back = st.text_input('Enter your feedback regarding the product here')

    user_token = st.session_state["authentication_status"]
    headers = {'Authorization': f'Bearer {user_token}'}
    payload_idea = {'review_token':str(token)}
    output = requests.post("http://backend:8000//idea/recieve-feedback-from-email", params = payload_idea,headers=headers)
    if output.status_code == 200:
        st.success('Review sent')
    else:
        st.error('Review could not be sent currently')
    
if st.session_state["authentication_status"] == False:
    st.subheader("Please Login before use")
else:
    rating()
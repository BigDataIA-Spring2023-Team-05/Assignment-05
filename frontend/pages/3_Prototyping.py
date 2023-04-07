import streamlit as st
# from streamlit import SessionState
import streamlit as st
import pandas as pd
import os
import requests
import urllib

# from streamlit import SessionState
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
url = 'http://localhost:8000/idea/get-all-user-ideas'
token = st.session_state['authentication_status']
headers = {'Authorization': f'Bearer {token}'}
result_ideas = requests.post(url, headers= headers )
output_ideas = result_ideas.json()
output_list = []
for item in output_ideas:
  idea_name = item['user_ideas']
  output_list.append(idea_name)
st.session_state['idea_list'] = output_list
def prototype():

    st.subheader('Prototyping and sharing')
    st.write('Select one of your favourite ideas :')

    options = st.session_state['idea_list']
    user_idea = st.selectbox("Select an option",options)
    gen_bt = st.button("Generate",key = 'generate')
    # if gen_bt:


    with st.form("my_form"):     
        email = st.text_input("Email Input")
    # subject for email
        sub = st.text_input("Subject")
        mission = st.text_input("Mission Statement")
    # confirm_password = st.text_input("Confirm Password", type="password")

    # Checkbox for agreeing to terms
    # agree_to_terms = st.checkbox("I agree to the terms and conditions")
        submitted = st.form_submit_button("Submit")
        if submitted:
            url = 'http://localhost:8000/user/sign-up'
            headers = {'Authorization': f'Bearer {token}'}
            myobj = {'email' : email, 'subject': sub, 'mission' : mission , 'idea_title' : user_idea }
            result = requests.post(url, json = myobj, headers = headers)
    
    # Validation logic
    
      

#     cutomer_insight = st.text_input()
if st.session_state["authentication_status"] == False and st.session_state["feature_status"] == False and st.session_state['mvp_status'] == False:
      st.subheader("Please Login before use")

elif st.session_state["authentication_status"] != False and st.session_state["feature_status"] == True and st.session_state['mvp_status'] == True:
    #   print('in loop')
        prototype()

# # if st.button('Go to Home Page'):
# #     # SessionState.selected_page = 'Home'
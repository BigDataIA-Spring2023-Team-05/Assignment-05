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
def prototype():

    st.subheader('Prototyping and sharing')
    st.write('Select one of your favourite ideas :')

    gen_bt = st.button("Generate",key = 'generate')
    # if gen_bt

    with st.form("my_form"):     
        email = st.text_input("Email Input")
    # subject for email
    sub = st.text_input("Subject")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    # Checkbox for agreeing to terms
    agree_to_terms = st.checkbox("I agree to the terms and conditions")
    submitted = st.form_submit_button("Submit")

    
    # Validation logic
    if submitted:
        if not email:
            st.warning("Please enter your right email")
        
        elif not sub:
            st.warning("Please enter your Subject")
        elif not password:
            st.warning("Please enter your password")
        elif password != confirm_password:
            st.warning("Passwords do not match")
        elif not agree_to_terms:
            st.warning("Please agree to the terms and conditions")

#     cutomer_insight = st.text_input()
if st.session_state["authentication_status"] == False and st.session_state["feature_status"] == False and st.session_state['mvp_status'] == False:
      st.subheader("Please Login before use")

elif st.session_state["authentication_status"] != False and st.session_state["feature_status"] == True and st.session_state['mvp_status'] == True:
    #   print('in loop')
        prototype()

# # if st.button('Go to Home Page'):
# #     # SessionState.selected_page = 'Home'
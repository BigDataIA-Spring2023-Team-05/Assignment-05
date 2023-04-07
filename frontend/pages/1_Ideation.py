import streamlit as st
import pandas as pd
import os
import requests
from streamlit_extras.switch_page_button import switch_page
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = False
if 'feature_status' not in st.session_state:
    st.session_state['feature_status'] = False
if 'fav_idea' not in st.session_state:
    st.session_state['fav_idea'] = ''
if 'mvp_status' not in st.session_state:
    st.session_state['mvp_status'] = False

    
# Define function to create page layout
def ideation_page():
    st.title('Welcome to Ideation Page')
    st.subheader('Brainstorm your Ideas')

    # st.title('Ideation')


    # Create a text input box to get the ideas from the user

    idea = st.text_input("Enter your Product idea here")

    idea_bt = st.button("GO !",key = 'idea_bt')
    if idea_bt:
        token = st.session_state["authentication_status"]
        headers = {'Authorization': f'Bearer {token}'}
        payload_idea = {'idea':str(idea)}
        output = requests.get("http://localhost:8000/idea/get-user-segments-for-product-idea", params = payload_idea,headers=headers)
        
        if output.status_code == 200:
            result_idea = output.json()
            user_segments_list  = result_idea['user_segments']
            # print(user_segments_list)
            user_segments = '\n'.join(user_segments_list)
            # print(user_segments)
            st.write("Your User segments : ")
            st.write(user_segments)
        else: 
            st.warning('Server Issue')

    # Display the user input below the text box
    


    # Create a text box to get input about the user segment from the user
    user_segment = st.text_input("Enter your User Segement")
    user_bt = st.button("GO !",key ='user_bt')
    if user_bt:
        token = st.session_state["authentication_status"]
        headers = {'Authorization': f'Bearer {token}'}
        payload_user = {'idea':str(user_segment)}
        output = requests.get("http://localhost:8000/idea/get-product-ideas-for-user-segment", params = payload_user,headers=headers)
        
        if output.status_code == 200:
            result_idea = output.json()
            product_ideas_list = result_idea['product_ideas']
            product_ideas = '\n'.join(product_ideas_list)
            
            st.write("Your product ideas : ")
            st.write(product_ideas)
        else: 
            st.warning('Server Issue')



    # Display the list output to the user
    

    #button to go to the next page
    button = st.button('Confirm')


    #Taking the most favorite idea out of the lot and going ahead with the design
    st.session_state['fav_idea']  = st.text_input('Your preferred product Idea is')

    #Button to navigate to the next page
    feature_page = st.button('Go to Feature Page')
    if feature_page:
        st.session_state['feature_status'] = True
        switch_page('Features')
            
if st.session_state["authentication_status"] == False:
      st.subheader("Please Login before use")
else:
    ideation_page()





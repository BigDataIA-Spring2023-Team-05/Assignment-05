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
if 'feature_list' not in st.session_state:
    st.session_state['feature_list'] = []

# st.title('Feature Page')
def feature_page():

        st.title('Feature Page')

        st.write('Your Product Idea is :')
        # st.write(st.session_state['fav_idea'])
        st.write(st.session_state['fav_idea'])
        # refresh_bt = st.button('Refresh', key = 'refresh' )
        st.write('Feature List for Product Ideas!')
        # if refresh_bt:
        #      token = st.session_state["authentication_status"]
        #      headers = {'Authorization': f'Bearer {token}'}
        #      payload_idea = {'idea':str(fav_idea)}
        #      output = requests.get("http://localhost:8000/idea/get-features-list-for-product-ideas", params = payload_idea,headers=headers)
        #      if output.status_code == 200:
        #             result_feature = output.json()
        #             st.session_state['feature_list']  = result_feature['features_list']
        #             # print(user_segments_list)
        #             features = '\n'.join(st.session_state['feature_list'])
        #             # print(user_segments)
        #             st.write("Your Product Features  : ")
        #             st.write(features)
        #      else: 
        #         st.warning('Server Issue')
        # else:
        token = st.session_state["authentication_status"]
        headers = {'Authorization': f'Bearer {token}'}
        fav_idea:str = str(st.session_state['fav_idea'])
    
        payload_idea = {'product_idea': fav_idea}

        params = urllib.parse.urlencode(payload_idea, quote_via=urllib.parse.quote)

        output = requests.get("http://localhost:8000/idea/get-features-list-for-product-ideas", params = params, headers=headers)
        if output.status_code == 200:
                result_feature = output.json()
                st.session_state['feature_list']  = result_feature['features_list']
                # print(user_segments_list)
                features = '\n'.join(st.session_state['feature_list'])
                # print(user_segments)
                st.write("Your Product Features  : ")
                st.write(features)
        else: 
            st.warning('Server Issue')
        st.write('Create your user story here')


        #User Story generated from GPT

        
        options = st.session_state['feature_list']
        selected_option = st.selectbox("Select an option",options)

        st.write('User Story')

        # Show the selected option
        st.write("You selected:", selected_option)

        st.write('Like idea?')
        st.button('Create your MVP')


        st.button('Go to Home Page')
            # SessionState.selected_page = 'Home'
# print(st.session_state["authentication_status"])
# print(st.session_state["feature_status"])
if st.session_state["authentication_status"] == False and st.session_state["feature_status"] == False:
      st.subheader("Please Login before use")

elif st.session_state["authentication_status"] != False and st.session_state["feature_status"] == True:
      print('in loop')
      feature_page()
  

# st.set_page_config(page_title="Streamlit_feature_page", page_icon=":smiley:", layout="wide",
#                     initial_sidebar_state="expanded", background_color="#f5f5f5")
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
        features = '\n'.join(st.session_state['feature_list'])
                # print(user_segments)
        st.write("Your Product Features  : ")
        st.write(features)
        # token = st.session_state["authentication_status"]
        # headers = {'Authorization': f'Bearer {token}'}
        # fav_idea:str = str(st.session_state['fav_idea'])
    
        # payload_idea = {'product_idea': fav_idea}

        # params = urllib.parse.urlencode(payload_idea, quote_via=urllib.parse.quote)

        # output = requests.get("http://localhost:8000/idea/get-features-list-for-product-ideas", params = params, headers=headers)
        # if output.status_code == 200:
        #         result_feature = output.json()
        #         st.session_state['feature_list']  = result_feature['features_list']
        #         # print(user_segments_list)
        #         features = '\n'.join(st.session_state['feature_list'])
        #         # print(user_segments)
        #         st.write("Your Product Features  : ")
        #         st.write(features)
        # else: 
        #     st.warning('Server Issue')
        st.write('Create your user story here')


        #User Story generated from GPT

        
        options = st.session_state['feature_list']
        selected_option = st.selectbox("Select an option",options)
        if selected_option:
            user_story = selected_option.split('.')[1]
            st.write("You selected user story:", user_story)

            print('--------------- Feature after spliting-----------------')
            print(user_story)
            print('--------------- ---------------------------------------')
            
                
            token = st.session_state["authentication_status"]
            headers = {'Authorization': f'Bearer {token}'}
            sel_feature:str = str(user_story)
        
            payload_idea = {'product_feature': sel_feature}

            params = urllib.parse.urlencode(payload_idea, quote_via=urllib.parse.quote)

            output = requests.get("http://localhost:8000/idea/get-to-do-list-for-product-feature", params = params, headers=headers)
            if output.status_code == 200:
                    result_todo = output.json()
                    todo_list  = result_todo['features_list']
                    # print(user_segments_list)
                    todo = '\n'.join(todo_list)
                    # print(user_segments)
                    st.write("Your User Stories / to-do list  : ")
                    st.write(todo)
            else: 
                st.warning('Server Issue')
             
        
        
            st.subheader('Sure about you Idea?')
            mvp_bt = st.button('Create your MVP')
            if mvp_bt:
                st.session_state['mvp_status'] = True
                url = 'http://localhost:8000/idea/approve-mvp'
                headers = {'Authorization': f'Bearer {token}'}
                fav_idea:str = str(st.session_state['fav_idea'])
                features = '\n'.join(st.session_state['feature_list'])
                myobj = {'idea_title': fav_idea ,'features': features}
                print('--------------- Feature after spliting 2222 -----------------')
                print(fav_idea)
                print('--------------- 222  ---------------------------------------')
                print(features)

                result = requests.post(url, headers= headers,json= myobj )
                print('--------------- 222  ---------------------------------------')
                
                print(result)

                print('--------------- 222  ---------------------------------------')
                if result.status_code == 200:
                    st.success('Saved your results')
                    switch_page('Prototyping')
                elif result.status_code == 409:
                    st.warning('This product Idea already exists') 
                else:
                    st.error('Could not save resuilts idea & feature-list ')
            

        # st.button('Go to Home Page')
            # SessionState.selected_page = 'Home'
# print(st.session_state["authentication_status"])
# print(st.session_state["feature_status"])
if st.session_state["authentication_status"] == False and st.session_state["feature_status"] == False:
    st.subheader("Please Login before use")
elif st.session_state["authentication_status"] != False and st.session_state["feature_status"] == False:
    print(st.session_state["authentication_status"])
    print(st.session_state["feature_status"])
    st.subheader("Use Ideation Page to come here")
elif st.session_state["authentication_status"] != False and st.session_state["feature_status"] == True:
    #   print('in loop')
    feature_page()
  

# st.set_page_config(page_title="Streamlit_feature_page", page_icon=":smiley:", layout="wide",
#                     initial_sidebar_state="expanded", background_color="#f5f5f5")
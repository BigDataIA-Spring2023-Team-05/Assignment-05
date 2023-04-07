import streamlit as st
# from streamlit import SessionState
import streamlit as st
import pandas as pd
import os
import requests
import urllib
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ.get('OPEN_AI_API_KEY')
# from backend.utils import open_ai_chat
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
if 'html_code' not in st.session_state:
    st.session_state['html_code'] = ''

url = 'http://backend:8000/idea/get-all-user-ideas'
token = st.session_state['authentication_status']
headers = {'Authorization': f'Bearer {token}'}
result_ideas = requests.post(url, headers= headers )
output_ideas = result_ideas.json()
html_code = ''
print(output_ideas)
output_list = []
for item in output_ideas:
    idea_name = str(item['idea_title'])
    output_list.append(idea_name)
st.session_state['idea_list'] = output_list


#############
def generate_html_code_for_product_idea(product_feature: str):
        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [
                    {'role': 'user', 'content': f'create an html code this \'{product_feature}\'?'}
                ],
                temperature = 0.70,
            )


        print(completion)

        result = completion.choices[0].message.content
        return result


# Close the file

def prototype():
 
    st.subheader('Prototyping and sharing')
    st.write('Select one of your favourite ideas :')
    
    options = st.session_state['idea_list']
    user_idea = st.selectbox("Select an option",options)
    gen_bt = st.button("Generate",key = 'generate')
    if gen_bt:
        st.write('html code generation')
        html_code = generate_html_code_for_product_idea(user_idea)
        print(html_code)
        with st.form("my_form"): 
            email = st.text_input("Email Input")
            # subject for email
            # sub = st.text_input("Subject")
            mission = st.text_input("Mission Statement")
            # confirm_password = st.text_input("Confirm Password", type="password")
            
            # Checkbox for agreeing to terms
            # agree_to_terms = st.checkbox("I agree to the terms and conditions")
            submitted = st.form_submit_button("Submit")
            if submitted:
                url = 'http://backend:8000/idea/send-email-for-feedback'
                headers = {'Authorization': f'Bearer {token}'}
                myobj = {'email_id' : email, 'mission_statement' : mission , 'idea_title' : user_idea,'html_code':html_code }
                result = requests.post(url, json = myobj, headers = headers)
                if result.status_code == 200:
                    st.success('Email sent !!')
                    switch_page('Insights')
                else:
                    st.warning('Email could not be sent , please check details')
# Open a new .html file in write mode
        with open("my_html_file.html", "w") as f:
    # Write the HTML code to the file
            f.write(html_code)
            # Close the file
        f.close()
        st.session_state['html_code'] = html_code
    
    
 
 # Validation logic
 
 
 
# cutomer_insight = st.text_input()
if st.session_state["authentication_status"] == False and st.session_state["feature_status"] == False and st.session_state['mvp_status'] == False:
    st.subheader("Please Login before use")
 
else:
 # print('in loop')
    prototype()
 
# # if st.button('Go to Home Page'):
# # # SessionState.selected_page = 'Home'
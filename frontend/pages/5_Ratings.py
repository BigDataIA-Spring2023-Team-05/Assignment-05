import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# from streamlit import SessionState
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = False

def rating():

    #creating a ratings page where entering th
    st.write('Give your rating for the product idea :')
    st.text_input('Enter your value out of 5 here') 
    token = st.session_state["authentication_status"]
    headers = {'Authorization': f'Bearer {token}'}
    payload_idea = {'idea':str(idea)}
    output = requests.get("http://localhost:8000//idea/recieve-feedback-from-email", params = payload_idea,headers=headers)
    output = idea.add_feedback(token, rating: int, feedback: str, db: Session)
    st.write('Feedback')
    st.text_input('Enter your feedback regarding the product here')


rating()

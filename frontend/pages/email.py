import streamlit as st
# from streamlit import SessionState

def email():

    st.write('Create your own prototype')

    idea = st.text_input("Idea:")

    input = st.text_input("Input:")

    Output = st.text_input("Output:")

    prototype = st.text_input('html prototypes')

    email = st.text_input("Email")

    #form input
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


# # if st.button('Go to Home Page'):
# #     # SessionState.selected_page = 'Home'
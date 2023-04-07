
import streamlit as st
# from streamlit import SessionState

def mapping():
    st.title("Cant seem to write your ideas out, tell it out and we'll map the features for you")



    st.write('This page would take your requirements and map the values and features according to it.')




    st.write('Upload your product idea here ')
      

    uploaded_file = st.file_uploader("Choose a file", type=["mp3", "wav"])

    if uploaded_file is not None:
        data = uploaded_file.read()
        st.write(data)

        st.title('Mapped to Feature Summary')

        # if st.button('Go to Home Page'):
        #     #  SessionState.selected_page = 'Home'
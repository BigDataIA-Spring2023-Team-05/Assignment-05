
import streamlit as st
# from streamlit import SessionState


def feature_page():

        st.title('Feature Page')

        st.write('Your Product Idea')
        st.text_input('Enter your product idea for which you want the features')
        st.button('Refresh'
                  
                  )
        st.write('Feature List for Product Ideas!')


        st.button('Confirm')

        st.write('Create your user story here')


        #User Story generated from GPT

        
        options = ["Feature1","Feature2","Feature3","Feature4"]
        selected_option = st.selectbox("Select an option",options)

        st.write('User Story')

        # Show the selected option
        st.write("You selected:", selected_option)

        st.write('Like idea?')
        st.button('Create your MVP')


        st.button('Go to Home Page')
            # SessionState.selected_page = 'Home'


# st.set_page_config(page_title="Streamlit_feature_page", page_icon=":smiley:", layout="wide",
#                     initial_sidebar_state="expanded", background_color="#f5f5f5")
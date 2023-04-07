import streamlit as st
# import SessionState



# Define function to create page layout

def home():
        st.title('Welcome to PROMA!')
        st.title('Your product management automation tool')

        st.title('Ideation')


        # Create a text input box to get the ideas from the user
        idea = st.text_input("Enter your idea here")

        # Display the user input below the text box
        st.write("Your User segments are ", idea)

         
        # Create a text box to get input about the user segment from the user
        user_input = st.text_input("Enter your ideas:")



        # Display the list output to the user
        st.write("Your product ideas are:", user_input)

        #button to go to the next page
        button = st.button('Confirm')


        #Taking the most favorite idea out of the lot and going ahead with the design
        st.text_input('Your preferred product Idea is')

        #Button to navigate to the next page
        st.button('Go to Feature Page')
            

            # st.write("The list of the products is")







# # Define page names
# page_names = ['Home', 'Feature Page', 'MVP & Email', 'Feature Mapping']

# # Initialize SessionState
# session_state = SessionState.get(selected_page=None)

# # Create sidebar with page selection
# selected_page = session_state.selected_page
# if selected_page is None:
#     selected_page = 'Home'
# session_state.selected_page = st.sidebar.selectbox('Select a page:', page_names, index=page_names.index(selected_page))

# # Display the selected page layout
# page_layout(selected_page)

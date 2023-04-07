import streamlit as st
import importlib
import home
import feature_page
import mapping
import email
import streamlit.components.v1 as components
# import SessionState

def main():
    page = st.sidebar.selectbox("Select a page", ["home", "feature_page", "mapping","email",])

    if page == "home":
        page_module = importlib.import_module("home")
        page_module.home()
    elif page == "feature_page":
        page_module = importlib.import_module("feature_page")
        page_module.feature_page()
    elif page == "mapping":
        page_module = importlib.import_module("mapping")
        page_module.mapping()
    elif page == "email":
        page_module = importlib.import_module("email")
        page_module.email()
out = st.experimental_get_query_params()
print(out)
if __name__ == "__main__":
    main()

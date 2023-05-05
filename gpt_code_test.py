# streamlit run gpt_code_test.py

import streamlit as st

# Define the first layer
menu = ["Home", "About"]
choice = st.sidebar.selectbox("Menu", menu)

# Show the appropriate page based on the user's choice
if choice == "Home":
    st.write("Welcome to the home page!")
else:
    st.write("Welcome to the about page!")

# Define an expandable section in the sidebar
with st.sidebar.expander("Options"):
    # Add options to the expandable section
    option1 = st.checkbox("Option 1")
    option2 = st.checkbox("Option 2")
    option3 = st.checkbox("Option 3")
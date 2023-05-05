# streamlit run gpt_code_test.py

import streamlit as st

# Define a function to check if the user is authenticated
def is_authenticated(password):
    return password == "password123"

# Define the login page
def login():
    st.title("Login")

    # Add a password input field
    password = st.text_input("Password", type="password")

    # Add a login button
    if st.button("Login"):
        # Check if the password is correct
        if is_authenticated(password):
            # If the password is correct, set the authenticated session state to True
            st.session_state.authenticated = True
        else:
            # If the password is incorrect, display an error message
            st.error("Incorrect password.")

# Define the dashboard page
def dashboard():
    st.title("Dashboard")

    # Display the contents of the dashboard here

# Define the logout page
def logout():
    st.title("Logout")

    # Remove the authenticated session state
    st.session_state.pop("authenticated", None)

# Define the app
def app():
    # Initialize the authenticated session state to False
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # Show the appropriate page based on the authenticated session state
    if st.session_state.authenticated:
        page = st.sidebar.radio("Navigation", ["Dashboard", "Logout"])
        if page == "Dashboard":
            dashboard()
        elif page == "Logout":
            logout()
    else:
        login()

# Run the app
if __name__ == "__main__":
    app()

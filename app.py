import streamlit as st

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "password123"

st.set_page_config(page_title="Login Page", page_icon="🔐")

st.title("🔐 Streamlit Login")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login Form
if not st.session_state.logged_in:
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        login = st.form_submit_button("Login")

        if login:
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error("Invalid Username or Password")

# Dashboard
else:
    st.success(f"Welcome, {USERNAME}! 🎉")

    st.write("This is your dashboard.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
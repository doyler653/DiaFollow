import streamlit as st

# Simple viewer authentication
def login():
    st.sidebar.title("Viewer Login")
    viewer_id = st.sidebar.text_input("Enter your ID")
    role = st.sidebar.selectbox("Role", ["parent", "doctor"])
    if viewer_id:
        st.session_state['viewer_id'] = viewer_id
        st.session_state['role'] = role
    return st.session_state.get('viewer_id', None)

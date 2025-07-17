import streamlit as st

st.title("Secrets Test")

st.write("GROQ API KEY:", st.secrets["GROQ_API_KEY"])
st.write("Email user:", st.secrets["EMAIL_USER"])


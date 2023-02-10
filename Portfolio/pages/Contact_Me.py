import streamlit as st
from send_email import sendEmail


st.header("Contact Me")


with st.form(key="-FORM-"):
  user_email = st.text_input("Email Address", placeholder="Enter your email address")
  raw_message = st.text_area("Message", placeholder="Enter your message here...")
  SUBJECT = "Python Portfolio App"
  TEXT = f"{raw_message}\nFrom: {user_email}"
  user_message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
  button = st.form_submit_button("Submit")
  if button:
    response = sendEmail(sentFrom=user_email, msg=user_message)
    st.info(response)
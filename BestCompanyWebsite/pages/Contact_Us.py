import streamlit as st
import pandas
from send_email import sendEmail

df = pandas.read_csv("topics.csv")
print(df)


st.header("Contact Me")


with st.form(key="-FORM-"):
  user_email = st.text_input("Your Email Address", placeholder="Enter your email address")
  topic = st.selectbox("Please select the topic you would like to discuss", (df["topic"]))
  raw_message = st.text_area("Message", placeholder="Enter your message here...")
  SUBJECT = "The Best Company"
  TEXT = f"Topic: {topic}\n\n{raw_message}\nFrom: {user_email}"
  user_message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
  button = st.form_submit_button("Submit")
  if button:
    response = sendEmail(sentFrom=user_email, msg=user_message)
    st.info(response)
import json
import streamlit as st
from streamlit_timeline import timeline
from streamlit_pills import pills
import time
from send_email import sendEmail

st.set_page_config(
  page_title="Python Portfolio | John Horn Jr.",
  layout="wide",
initial_sidebar_state="collapsed")

with st.sidebar:
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


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# HOME PAGE --------------

col1, col2 = st.columns([0.5,2])

with col1:
  st.image("assets/images/photo.jpg", width=150)

with col2:
  st.title("John Horn Jr.")
  about_me = """
  Software engineer with the ability to learn and collaborate in rapidly changing enviroments and compositions. Worked through 1000+ hours of bootcamp structure, learning JavaScript, NodeJS, Angular, and Python. Eager to tackle web development/design challenges to achieve lasting impacts on user experience. I speak native english and conversational Japanese."""
  st.info(about_me)

st.subheader("Career Snapshot")

with st.spinner(text="Building Timeline"):
  with open("timeline.json", 'r') as file:
    data = file.read()
    timeline(data, height=500)

st.subheader("Skills & Tools ⚒️")

selected = pills("", ["HTML", "CSS", "JavaScript", "Python", "TypeScript", "NodeJS", "PHP", "C#", "VB.Net", "SQL", "Angular", "Vue", "Flutter", "Dart"], ["🍔", "🍕", "🍟", "🍠", "🍤", "🍦", "🍩", "🍫", "🍪", "🍨", "🍰", "🍱", "🍿", "🍲"])
st.write(selected)

page_description = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(page_description)

# Get Data
with open('data.json') as file:
  content = file.read()

apps = json.loads(content)

col3, col_spacer, col4 = st.columns([1.5, 0.5, 1.5])

# Loop through data
for index, app in enumerate(apps):
  if index % 2:
    with col4:
      st.subheader(app['title'])
      st.write(app['description'])
      st.image(app['image'])
      st.write(f"[Source Code]({app['url']})")
  else:
    with col3:
      st.subheader(app['title'])
      st.write(app['description'])
      st.image(app['image'])
      st.write(f"[Source Code]({app['url']})")

st.balloons()

  # print(f"{title}\n{description}\n{url}\n{image_path}")

import json
import streamlit as st

# HOME PAGE --------------

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
  st.image("assets/images/photo.jpg", width=250)

with col2:
  st.title("John Horn Jr.")
  about_me = """
  Hi, I am John. I am a Python programmer, designer, photographer and artist. I graduated from the University of Phoenix with a degree in Marketing. I have worked as a software engineer in the US and Japan. Though Python is my first love, I can code in many other languages as well. I speak native english and conversational Japanese."""
  st.info(about_me)

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
  # print(f"{title}\n{description}\n{url}\n{image_path}")

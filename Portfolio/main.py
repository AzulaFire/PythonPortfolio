import json
import streamlit as st

# HOME PAGE --------------

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
  st.image("assets/images/photo.png")

with col2:
  st.title("John Horn Jr.")
  content = """Hi, I am John. I am a Python programmer, designer, photographer and artist. I graduated from the University of Phoenix with a degree in Marketing. I have worked as a software engineer in the US and Japan. Though Python is my first love, I can code in many other languages as well. I speak native english and conversational Japanese."""
  st.info(content)  

# Get Data
with open('data.json') as file:
  content = file.read()

apps = json.loads(content)

# Loop through data
for app in apps:
  st.text(app['title'])
  st.text(app['description'])
  st.text(app['url'])
  st.image(app['image'])
  # print(f"{title}\n{description}\n{url}\n{image_path}")

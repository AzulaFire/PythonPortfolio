import json
import streamlit as st


with open('data.json') as file:
  content = file.read()

apps = json.loads(content)

for app in apps:
  st.text(app['title'])
  st.text(app['description'])
  st.text(app['url'])
  st.image(app['image'])
  # print(f"{title}\n{description}\n{url}\n{image_path}")

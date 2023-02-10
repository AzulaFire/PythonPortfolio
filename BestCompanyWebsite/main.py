import streamlit as st
import pandas

st.set_page_config(layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

st.title("The Best Company")

description = """
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
"""

st.write(description)

st.subheader("Our Team")

col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1.5, 1, 1.5])

df = pandas.read_csv("data.csv")

with col1:
  for index, row in df[:4].iterrows():
    name = row["first name"] + " " + row["last name"]
    st.subheader(name.title())
    st.write(row["role"])
    st.image(f"assets/images/{row['image']}")

with col3:
  for index, row in df[4:8].iterrows():
    name = row["first name"] + " " + row["last name"]
    st.subheader(name.title())
    st.write(row["role"])
    st.image(f"assets/images/{row['image']}")

with col5:
  for index, row in df[8:].iterrows():
    name = row["first name"] + " " + row["last name"]
    st.subheader(name.title())
    st.write(row["role"])
    st.image(f"assets/images/{row['image']}")
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
st.subheader("What makes us who we are today…")

description = """
At <b>The Best Company</b>, we develop innovative and creative products and services that provide total communication and information solutions. Among a plethora of services, web design and development, tailor made applications, ERPs, CRMs, e-commerce solutions, business-to-business applications, business-to-client applications, managed hosting and internet portal management are few that we offer. Satisfied clients around the globe bear testimony to the quality of our work.

As a leader in technology exploring, <b>The Best Company</b> is committed to exporting quality software worldwide.
"""

st.write(description, unsafe_allow_html=True)

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
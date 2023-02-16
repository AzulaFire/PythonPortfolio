import requests
from requests.exceptions import HTTPError
import streamlit as st

API_KEY = "woQDIzipYpBzwUKqs70DUs7Wp9bdpo7B7HaJpgdy"

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()
    # access JSON content
    jsonResponse = response.json()

    st.header(jsonResponse['title'])
    st.subheader(jsonResponse['copyright'])
    st.image(jsonResponse['url'])
    st.write(jsonResponse['explanation'])
    st.markdown("<hr />", unsafe_allow_html=True)

except HTTPError as http_err:
    st.error(f'HTTP error occurred: {http_err}')
except Exception as err:
    st.error(f'Other error occurred: {err}')


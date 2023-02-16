import streamlit as st
import requests
from requests.exceptions import HTTPError
from send_email import sendEmail
import os

st.set_page_config(page_title="GAMERS | RISING", initial_sidebar_state="collapsed")

path = os.path.dirname(__file__)
banner = path +'/banner.png'
css = path + '/style.css'

API_KEY = "" #https://newsapi.org/
TOPIC = ""
BLOB = ""

game_domains="""
kotaku.com,
ign.com,
pcgamer.com,
gamesradar,
gamespot,
gematsu.com,
crunchyroll.com,
geektyrant.com,
siliconera.com,
destructoid.com
"""

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css(css)

# Make website using streamlit

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("banner.png")

with col3:
    st.write(' ')

st.text_input(label="Search", placeholder="Enter Game Title", key="-GAME-", label_visibility="hidden")

if st.session_state['-GAME-']:
    query = st.session_state['-GAME-']
    query = query.title()
    TOPIC = query
    url = f"https://newsapi.org/v2/everything?q={query}&searchIn=title&domains={game_domains}&language=en&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        count = len(jsonResponse['articles'])
        st.subheader(f"{count} articles")

        for article in jsonResponse['articles']:
            if article['title'] is not None and article['description'] is not None:
                BLOB = BLOB + article['title'] + '\n' + article['description'] + '\n' + article['url'] + 2*'\n'

            st.subheader(article['title'])
            st.text(article['source']['name'])
            st.write(article['description'])
            st.write(article['url'])
            st.image(article['urlToImage'])
            st.markdown("<hr />", unsafe_allow_html=True)

    except HTTPError as http_err:
        st.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        st.error(f'Other error occurred: {err}')

with st.sidebar:
    with st.form(key="-FORM-"):
        SUBJECT = f"GAMERS RISING | {TOPIC}"
        user_message = 'Subject: ' + SUBJECT + 2*"\n" + BLOB
        user_message = user_message.encode('utf-8')
        st.text("Email Search Results")
        user_email = st.text_input("Email Address", placeholder="Enter your email address", label_visibility="hidden")
        button = st.form_submit_button("Submit")
        if button:
            if len(BLOB) > 0:
                response = sendEmail(toAddress=user_email, msg=user_message)
                st.info(response)
            else:
                st.info("Please search for a game.")
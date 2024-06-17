import streamlit as st
import glob
import requests
from bs4 import BeautifulSoup

# CONFIGURATIONS

st.set_page_config(page_title='DataFinder Application', layout='wide')

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# LOGIC

def check_files(path, s):
    result = {}
    found =  False
    try:
        files = glob.glob(pathname=path)
        for file in files:
            file_name_dict = {}
            with open(file=file, mode='r', encoding='utf-8') as f:
                data = f.readlines()
            count = 0
            for index, line in enumerate(data):
                if s in line:
                    dict_result = {}
                    count += 1
                    found = True
                    dict_result['Line: ' + str(index + 1)] = line.strip()
                    file_name_dict['Result: ' + str(count)] = dict_result
            result[file] = file_name_dict

        if found:
            return result
        else:
            return 'No results found.'
    except:
        return 'Error: Invalid Path'

def check_web(url, s, t):
    print(url, s, t)
    results = []

    page = requests.get(url=url)
    if page.status_code == 200:
        soup = BeautifulSoup(markup=page.text, features="html.parser")
        for item in soup.find_all(s):
            if len(t) > 0:
                results.append(item.get(t))
            else:
                results.append(item)

        if len(results) > 0:
            clean_results = list(dict.fromkeys(results))
            return clean_results
        else:
            return "No results found."
    else:
        return 'Error: Page not found.'
        

# DESIGN

st.header(body='Data Finder Application')

col1, col2 = st.columns([2, 1])
col3, col4 = st.columns([2, 1])

with col1:
    query_string = st.text_input(label='Query String')
    file_path = st.text_input(label='File Path')   
with col2:
    file_ext = st.selectbox(label='File Extention', options=('*', '*.txt', '*.html', '*.css', '*.js', '*.aspx', '*.aspx.vb', '*.vb', '*.jsp'))
    btn_search = st.button(label='File Search')
with col3:
    url_path = st.text_input(label='URL')
    query_tag = st.text_input(label='HTML Tag')
with col4:
    web_ext = st.selectbox(label='HTML Attribute', options=('', 'href', 'form', 'id', 'name', 'onclick', 'src', 'span', 'style', 'type', 'value'))
    btn_web_search = st.button(label='Web Search')


st.divider()

if btn_search:
    if len(file_path) > 0 and len(query_string) > 0:
        result = check_files(file_path + '\\' + file_ext, query_string)
        st.write(result)
    else:
        st.write('File Path and Query String are Required.')

if btn_web_search:
    if len(url_path) > 0 and len(query_tag) > 0:
        result = check_web(url_path, query_tag, web_ext)
        st.write(result)
    else:
        st.write('File Path and Query String are Required.')        


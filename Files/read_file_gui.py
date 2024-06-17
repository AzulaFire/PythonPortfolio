import streamlit as st

st.title(body='File Reader')

# LOGIC

def getFileContents(file):
    try:
        with open(file=file, mode='r') as f:
            data = f.read()
            return data
    except:
        return 'File Not Found'

# DESIGN

file = st.text_input(label='File Path')

my_button = st.button(label='Read File')

if(my_button):
    st.write(getFileContents(file))
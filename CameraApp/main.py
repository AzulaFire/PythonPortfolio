import streamlit as st
from PIL import Image

def convertImage(input_image):
    # Create a Pillow
    img = Image.open(input_image)

    # Conver Image Object to Black and White
    gray_scale = img.convert("L")

    return gray_scale

uploaded_image = st.file_uploader("Upload Image")

if uploaded_image:
  new_photo = convertImage(uploaded_image)
  # Display converted Image
  st.image(new_photo)  

with st.expander("Start Camera"):

  # Take and set Photo to a variable
  user_photo = st.camera_input("")

  if user_photo:
    new_photo = convertImage(user_photo)
    # Display converted Image
    st.image(new_photo) 
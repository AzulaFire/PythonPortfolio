import streamlit as st
import plotly.express as px
from api import get_data
import os

st.set_page_config(page_title="Weather Forecaster")

path = os.path.dirname(__file__)

st.header("Weather Forcaster")

place = st.text_input("Place:", placeholder="Enter a city").title()

if place == "":
    place = "---"

num = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

days = "day"
if num > 1:
    days = "days"

option = st.selectbox("Select data to view", ("Temperature", "Sky View"))
st.subheader(f"Temperture for the next [{num}] {days} in {place}")


if place != "---":

    try:
        # Get the temperature/sky data
        filtered_data = get_data(place, num, option)

        if option == "Temperature":
            temps = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            
            # Create a temperture plot
            figure = px.line(x=dates, y=temps, labels={"x": "Date", "y": "Temperatures"})

            st.plotly_chart(figure)

        if option == "Sky View":
            images = {"Clear": path + "/assets/images/clear.png", "Clouds": path + "/assets/images/cloud.png", "Rain": path + "/assets/images/rain.png", "Snow": path + "/assets/images/snow.png"}

            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]

            image_paths = [images[condition] for condition in sky_conditions] 
                                
            st.image(image_paths, width=115)
    except KeyError:
        st.error("Invalid Request: City not found.")
import streamlit as st
import pandas as pd
import plotly.express as px

st.header("In Search for Happiness")

x_label = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))

y_label = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"))

st.subheader(f"{x_label} and {y_label}")

df = pd.read_csv("happy.csv")

# Short Version but labels will be in lowercase
# figure = px.scatter(df, x=x_label.lower(), y=y_label.lower(), labels={"x":x_label, "y": y_label})
# st.plotly_chart(figure)

if x_label == "Happiness":
    x_axis = df["happiness"]
elif  x_label == "Generosity":
    x_axis = df["generosity"]
else:
    x_axis = df["gdp"]

if y_label == "Happiness":
    y_axis = df["happiness"]
elif  y_label == "Generosity":
    y_axis = df["generosity"]
else:
    y_axis = df["gdp"]

figure = px.scatter(x=x_axis, y=y_axis, labels={"x":x_label.upper(), "y": y_label.upper()})

st.plotly_chart(figure)

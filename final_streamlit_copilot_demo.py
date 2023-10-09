# write streamlit app that takes input as coloumn 
# names: Patient_ID, Weight, Height, and plot BMI

 # import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# set page config
st.set_page_config(layout="wide")

# display an image
st.image("assets/header.png")

# initialize session state to hold the dataframe
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()

# set an app title
st.title("BMI Calculator")

# create a sidebar for input parameters
st.sidebar.title("BMI Calculator")
st.sidebar.markdown("This app calculates BMI based on height and weight")

# create input fields for patient id, weight and height
patient_id = st.sidebar.number_input("Enter patient ID", 0)
weight = st.sidebar.number_input("Enter weight", value=50.4, format="%.2f")
height = st.sidebar.number_input("Enter height", value=5.4, format="%.2f")

# dropdown menu for weight and height units
weight_unit = st.sidebar.selectbox("Select weight unit", ("kg", "pounds"))
height_unit = st.sidebar.selectbox("Select height unit", ("cm", "inches"))

# convert the weight in kg if in pounds
if weight_unit == "pounds":
    weight = float(weight) * 0.45359237

# convert the height to cm if in inches
if height_unit == "inches":
    height = float(height) * 2.54

# calculate the bmi
bmi = float(weight) / (float(height) / 100)**2

# create a dictionary with patient data
data = {
    'Patient_ID': [patient_id],
    'Weight (Kg)': [weight],
    'Height (cm)': [height],
    'BMI': [bmi]
}

# create a submit button
if st.sidebar.button("Submit"):
    # append the data to dataframe
    st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame(data)], ignore_index=True)
    st.dataframe(st.session_state.df)
    # create a bar chart of BMI
    fig = px.bar(st.session_state.df, x='Patient_ID', y='BMI')
    st.plotly_chart(fig)
    # reset the input fields
    patient_id=0
    height=0
    weight=0
else:
    st.dataframe(st.session_state.df)
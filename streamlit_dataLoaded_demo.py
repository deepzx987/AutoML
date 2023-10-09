# write streamlit app that takes input as coloumn names: Patient_ID, Weight, Height, Temperature and calculate and plot BMI histogram

# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")
# Create image
st.image("assets/header.png")

#  Initialize session state to hold the DataFrame
if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv('DummyData.csv')

# Create dataframe
# df = pd.DataFrame()
# df = pd.read_csv('DummyData.csv')

st.title("BMI Calculator")

st.sidebar.title("BMI Calculator")
st.sidebar.markdown("This app calculates BMI based on height and weight")

# Take multiple inputs from user with a dropdown menu for Weight as kg and pounds, for Height as cm and inches
patient_id = st.sidebar.number_input("Enter patient ID",0)
weight = st.sidebar.number_input("Enter weight", value=50.4,format="%.2f")
height = st.sidebar.number_input("Enter height", value=5.4, format="%.2f")

# Create a dropdown menu for Weight as kg and pounds
weight_unit = st.sidebar.selectbox("Select weight unit", ("kg", "pounds"))
# Create a dropdown menu for Height as cm and inches
height_unit = st.sidebar.selectbox("Select height unit", ("cm", "inches"))

# Convert weight to kg
if weight_unit == "pounds":
    weight = float(weight) * 0.45359237

# Convert height to cm
if height_unit == "inches":
    height = float(height) * 2.54


# Calculate BMI
bmi = float(weight) / (float(height) / 100)**2

# Create dataframe
data = {
    'Patient_ID': [patient_id],
    'Weight (Kg)': [weight],
    'Height (cm)': [height],
    'BMI': [bmi]
}

# Create submit button
# submit = st.sidebar.button("Submit")
if st.sidebar.button("Submit"):
    # append the data to dataframe
    # st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame(data)], ignore_index=True)
    st.dataframe(st.session_state.df)
    fig = px.bar(st.session_state.df, x="Patient_ID", y="BMI", color="BMI", title="BMI")
    st.plotly_chart(fig)

    patient_id = 0
    weight = 0
    height = 0
else:
    st.dataframe(st.session_state.df)


import streamlit as st
import requests
import json

st.title("Car price prediction")
API_URL = "http://0.0.0.0:8000/predict"

brand = st.text_input("Name of the car brand", value= "Ford")
model_year = st.number_input("Car launch year", value = 2024)
milage = st.number_input("Milage of the car", value = 51000)
fuel_type = st.selectbox("Type of fuel", options= ["Gasoline","Hybrid","Diesel","Other"])
engine_size = st.number_input("Horsepower", value = 3.7)
horsepower = st.number_input("Horsepower", value = 600.0)
cylinders = st.number_input("Cylinders", value = 6)
transmission = st.selectbox("Transmission", options= ["CVT", "Manual", "Automatic", "Other"])
accident = st.selectbox("Any accident Occur?", options= ["No", "Yes"])

if st.button("predict"):
    data = {
            "brand":brand,
            "model_year": model_year,
            "milage": milage,
            "fuel_type": fuel_type,
            "engine_size": engine_size,
            "horsepower": horsepower,
            "cylinders": cylinders,
            "transmission": transmission,
            "accident": accident
            }

    response = requests.post(API_URL , json = data)
    prediction = response.json()
    st.success(f"Predicted Insurance Premium Category: **{prediction['price']}**")


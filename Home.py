import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
df = pd.read_csv(r"E:\FINAL_PROJECT\Cars.csv")


# Title of the app
st.markdown("<h1 style='text-align: center; color: black;'>Car Sale Simulator</h1>", unsafe_allow_html=True)

# Add an image from the internet
st.image("https://s.cafebazaar.ir/images/upload/screenshot/com.car.sale.simulator.trade.dealership.game-11c44d5e-d9d0-4263-b6d8-470ddbfec2fa.jpeg?x-img=v1/resize,h_600,lossless_false/optimize", caption="Cars prices ", use_column_width=True)

# Data description
st.header("Data Description")
st.markdown("""
This dataset contains information about various car listings, including the brand, model, body type, color, year of manufacture, and other specifications. Below is a brief description of the columns:
- **Brand**: The manufacturer of the car (e.g., Chevrolet, Hyundai).
- **Model**: The specific model of the car (e.g., Optra, Tucson).
- **Body**: The body type of the car (e.g., Sedan, SUV).
- **Color**: The color of the car (e.g., Black, Brown).
- **Year**: The year the car was manufactured.
- **Fuel**: The type of fuel the car uses (e.g., Benzine).
- **Kilometers**: The range of kilometers the car has been driven.
- **Engine**: The engine capacity of the car (e.g., 1600 CC).
- **Transmission**: The type of transmission (e.g., Automatic, Manual).
- **Price**: The price of the car in thousands of currency units.
- **Gov**: The governorate where the car is located (e.g., Cairo, Giza).
""")

# Kaggle data source
st.subheader("Data Source")
st.markdown("[Click here to view the data on Kaggle](https://www.kaggle.com/datasets/abdo977/used-car-price-in-egypt)")

st.subheader("Sample from the dataset")
st.dataframe(df.sample(5))

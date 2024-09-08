import streamlit as st
import pickle
import numpy as np
import pandas as pd


# Load dataset for unique values
df = pd.read_csv("Cars_EDA.csv")

# Load the model and preprocessor from pickle files
model = pickle.load(open('model.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))



# Custom CSS to improve styling
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            font-size: 16px;
            margin-top: 20px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #fff;
        }
    </style>
""", unsafe_allow_html=True)

# Page title and introduction
st.title("🚗 Car Price Prediction")
st.markdown("""
Welcome to the Car Price Prediction app! Fill in the details of the car, and we'll estimate its price based on our model. 
This tool helps you gauge the market value of different car configurations.
""")

# Input fields
st.header("Enter the Car's Details:")

# Organize inputs into two columns for a better layout
col1, col2 = st.columns(2)

with col1:
    # Step 1: Select Brand
    brand = st.selectbox("Brand", df['brand'].unique())

    # Filter the dataset based on the selected brand
    filtered_df = df[df['brand'] == brand]

    # Step 2: Select Model
    Model = st.selectbox("Model", filtered_df['model'].unique())

    # Filter the dataset based on the selected model
    filtered_df = filtered_df[filtered_df['model'] == Model]

    # Step 3: Select Body Type
    body = st.selectbox("Body Type", filtered_df['body'].unique())

    # Step 4: Select Color
    color = st.selectbox("Color", filtered_df['color'].unique())

    # Step 5: Select Year
    year = st.number_input("Year of Manufacture", 
                           min_value=int(filtered_df['year'].min()), 
                           max_value=int(filtered_df['year'].max()), 
                           value=int(filtered_df['year'].min()))

with col2:
    # Step 6: Select Fuel Type
    fuel = st.selectbox("Fuel Type", filtered_df['fuel'].unique())

    # Step 7: Select Kilometers Driven
    kilometers = st.number_input("Kilometers Driven")

    # Step 8: Select Engine Capacity
    engine = st.selectbox("Engine Capacity", filtered_df['engine'].unique())

    # Step 9: Select Transmission
    transmission = st.selectbox("Transmission", filtered_df['transmission'].unique())

    # Step 10: Select Governorate
    gov = st.selectbox("Governorate", df['gov'].unique())

# Section divider
st.markdown("---")

# Create a dictionary of input features
input_data = {
    'brand': brand,
    'model': Model,
    'body': body,
    'color': color,
    'year': year,
    'fuel': fuel,
    'kilometers': kilometers,
    'engine': engine,
    'transmission': transmission,
    'gov': gov,
}

# Convert the input data to a DataFrame
input_df = pd.DataFrame([input_data], dtype='object')

# Add a prediction button
if st.button("Predict Price"):
    # Preprocess the input data
    input_preprocessed = preprocessor.transform(input_df)

    # Make a prediction
    prediction = model.predict(input_preprocessed)

    # Show the prediction result in a formatted way
    st.header("Predicted Price")
    st.metric(label="Estimated Price", value=f"{prediction[0]:,.2f}EGP")

# Add an optional sidebar for additional information or settings
st.sidebar.header("About")
st.sidebar.markdown("""
This app uses machine learning models to predict car prices based on various input features. 
You can adjust the inputs to see how they affect the predicted price.
""")

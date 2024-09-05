import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'> Cars Analysis </h1>", unsafe_allow_html=True)
st.image("https://brightdata.com/wp-content/uploads/2023/07/optimize_pricing_strategy.svg", caption="Cars Analyze ", use_column_width=True)

df_EDA = pd.read_csv(r"E:\FINAL_PROJECT\Cars_EDA.csv")
col1, col2,col3 = st.columns([6,2,6])
with col1:
    model_price = df_EDA.groupby('model')['price'].mean().sort_values(ascending=False)
    fig = px.bar(model_price , color = model_price.index ,title='Top 5 most expensive car models')
    st.plotly_chart(fig, use_container_width=True)

    Transmission_price= df_EDA.groupby('transmission')['price'].count().sort_values(ascending=False)
    fig = px.bar(Transmission_price , color = Transmission_price.index, title='Transmission distribution' )
    st.plotly_chart(fig, use_container_width=True)
    

    #  What is the average price of each body type?
    body_price = df_EDA.groupby('body')['price'].mean().reset_index()
    fig = px.bar(body_price, x='body', y='price', color='body', title='Average price of each body type')
    st.plotly_chart(fig, use_container_width=True)

    fuel_price = df_EDA.groupby('fuel')['price'].mean().sort_values(ascending=False)
    fig = px.bar(fuel_price , color = fuel_price.index , title='Average price of each fuel type')
    st.plotly_chart(fig, use_container_width=True)






with col3:
    fuel_price = df_EDA.groupby('fuel')['price'].mean().sort_values(ascending=False)
    fig = px.bar(fuel_price , color = fuel_price.index , title='Fuel distribution')
    st.plotly_chart(fig, use_container_width=True)



    brand_price = df_EDA.groupby('brand')['price'].mean().reset_index().nlargest(5, 'price')
    fig = px.bar(brand_price, x='brand', y='price', color='brand', title='Top 5 most expensive car brands')
    st.plotly_chart(fig, use_container_width=True)


    brand_price = df_EDA.groupby('brand')['price'].mean().sort_values(ascending=False)
    fig = px.bar(brand_price , color = brand_price.index , title='Top 5 most expensive car brands')
    st.plotly_chart(fig, use_container_width=True)

    year_price = df_EDA.groupby('year')['price'].mean().reset_index()
    fig = px.line(year_price, x='year', y='price', title='Average price of cars over the years')
    st.plotly_chart(fig, use_container_width=True)
    


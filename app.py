import streamlit as st
import pandas as pd

# Title
st.title("Sales Intelligence Dashboard")

# Load data
df = pd.read_csv("data.csv")

# Show dataset
st.subheader("Dataset Preview")
st.write(df)

# Sales by Region
st.subheader("Sales by Region")
region_sales = df.groupby("Region")["Sales"].sum()
st.bar_chart(region_sales)

# Sales by Product
st.subheader("Sales by Product")
product_sales = df.groupby("Product")["Sales"].sum()
st.bar_chart(product_sales)

# Profit stats
st.subheader("Profit Analysis")
st.write("Total Profit:", df["Profit"].sum())
st.write("Average Profit:", df["Profit"].mean())

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('hmodel.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction App")
st.write("Predict the price of a house based on its features.")

# Collect user input
area = st.number_input("Area (sq. ft)", min_value=500, max_value=20000, step=50)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
stories = st.number_input("Number of Stories", min_value=1, max_value=5, step=1)

mainroad = st.selectbox("Main Road Access", ['yes', 'no'])
guestroom = st.selectbox("Guest Room", ['yes', 'no'])
basement = st.selectbox("Basement", ['yes', 'no'])
hotwaterheating = st.selectbox("Hot Water Heating", ['yes', 'no'])
airconditioning = st.selectbox("Air Conditioning", ['yes', 'no'])
parking = st.number_input("Parking Spaces", min_value=0, max_value=5, step=1)
prefarea = st.selectbox("Preferred Area", ['yes', 'no'])

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'stories': [stories],
    'mainroad': [1 if mainroad == 'yes' else 0],
    'guestroom': [1 if guestroom == 'yes' else 0],
    'basement': [1 if basement == 'yes' else 0],
    'hotwaterheating': [1 if hotwaterheating == 'yes' else 0],
    'airconditioning': [1 if airconditioning == 'yes' else 0],
    'parking': [parking],
    'prefarea': [1 if prefarea == 'yes' else 0]
})

# Predict button
if st.button("Predict House Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"🏡 Estimated House Price: ${prediction:,.2f}")

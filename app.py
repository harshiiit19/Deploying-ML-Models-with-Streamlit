import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and columns
model = joblib.load("car_price_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("🚗 Car Price Estimator (MSRP)")

# User inputs
brand = st.selectbox("Brand", ['Acura', 'Audi', 'BMW', 'Buick', 'Cadillac'])
vehicle_class = st.selectbox("Vehicle Class", ['SUV', 'Sedan', 'Wagon', 'Pickup'])
region = st.selectbox("Region", ['Asia', 'Europe', 'USA'])
drivetrain = st.selectbox("Drive Train", ['All', 'Front', 'Rear'])

engine_size = st.slider("Engine Size (L)", 1.0, 6.0, 3.0)
cylinders = st.slider("Cylinders", 3, 12, 6)
horsepower = st.slider("Horse Power", 50, 500, 200)
mpg_city = st.slider("MPG City", 5, 40, 20)
mpg_highway = st.slider("MPG Highway", 5, 50, 30)
weight = st.slider("Weight (lbs)", 1500, 7000, 3500)
wheelbase = st.slider("Wheelbase (in)", 90, 140, 105)
length = st.slider("Length (in)", 140, 250, 180)
dealer_cost = st.number_input("Dealer Cost ($)", min_value=10000.0, value=30000.0)

# Assemble input row
input_dict = {
    'EngineSize': engine_size,
    'Cylinders': cylinders,
    'HorsePower': horsepower,
    'MPG_City': mpg_city,
    'MPG_Highway': mpg_highway,
    'Weight': weight,
    'Wheelbase': wheelbase,
    'Length': length,
    'DealerCost': dealer_cost,
    f'Brand_{brand}': 1,
    f'VehicleClass_{vehicle_class}': 1,
    f'Region_{region}': 1,
    f'DriveTrain_{drivetrain}': 1,
}

# Create a row matching the model's expected input
input_df = pd.DataFrame([input_dict])
input_df = input_df.reindex(columns=model_columns, fill_value=0)

# Prediction
if st.button("Predict MSRP"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated MSRP: ${prediction:,.2f}")

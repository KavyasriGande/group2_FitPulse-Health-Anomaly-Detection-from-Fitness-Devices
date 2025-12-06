import streamlit as st
import pandas as pd
import numpy as np

st.title("💓 FitPulse Data Cleaning & Null Check")

file_path = r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"

data = pd.read_excel(file_path)

st.subheader("📌 Original Data")
st.write(data)

# Null value check
st.subheader("🔍 Null Value Check")
st.write(data.isnull().sum())

# Clean column
data['heart_beat_per_minute'] = pd.to_numeric(data['heart_beat_per_minute'], errors='coerce')
data['heart_beat_per_minute'] = data['heart_beat_per_minute'].fillna(0).astype(int)

st.subheader("🛠 Cleaned Data")
st.write(data)

# Display shapes
st.subheader("📏 Array Shapes")
heart = data['heart_beat_per_minute'].to_numpy()
pulse = data['pulse_rate'].to_numpy()
steps = data['steps'].to_numpy()
gend = data['gender'].to_numpy()

st.write("Heart Shape:", heart.shape)
st.write("Pulse Shape:", pulse.shape)
st.write("Steps Shape:", steps.shape)
st.write("Gender Shape:", gend.shape)

# Plot example
st.subheader("📈 Heartbeat vs Pulse")
st.line_chart(data[['heart_beat_per_minute','pulse_rate']])

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_path = r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"

data=pd.read_excel(file_path)

# Null value check
print(data.isnull().sum(),'\n')

# convert to Numpy array
heart=data['heart_beat_per_minute'].to_numpy()
pulse=data['pulse_rate'].to_numpy()
steps=data['steps'].to_numpy()
gend=data['gender'].to_numpy()
print("Heart Humpy Shape :",heart.shape)
print("Pulse Numpy shape :",pulse.shape)
print("Steps Humpy Shape :",steps.shape)
print("Gender Numpy shape :",gend.shape)

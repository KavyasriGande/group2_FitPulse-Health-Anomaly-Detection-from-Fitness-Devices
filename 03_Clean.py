import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)

#clean steps column
data['heart_beat_per_minute']=pd.to_numeric(data['heart_beat_per_minute'],errors='coerce')
print(data.head())
data['heart_beat_per_minute']=data['heart_beat_per_minute'].fillna(0).astype(int)
print(data.head())
data['pulse_rate'] = pd.to_numeric(data['pulse_rate'], errors='coerce')
print(data.head())
data['pulse_rate'] = data['pulse_rate'].fillna(0).astype(int)
print(data.head())
data['steps'] = pd.to_numeric(data['steps'], errors='coerce')
print(data.head())
data['steps'] = data['steps'].fillna(0).astype(int)
print(data.head())

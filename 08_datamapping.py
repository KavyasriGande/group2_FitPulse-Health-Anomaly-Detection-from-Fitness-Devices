import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# to read excel file data
file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)
print(data.head())

# Convert 'Gender' to numeric, coercing errors to NaN and fill NaN values with 1
# Map 'Male' to 1, 'Female' to 0.
gender_mapping = {'Male': 1, 'Female': 0}

# Apply the mapping. Values not in the mapping (e.g., original NaN, or other strings) will result in NaN.
data['gender'] = data['gender'].map(gender_mapping)

# Fill any remaining NaN values with 2 (or another appropriate integer for 'unknown')
# before converting to integer type.
data['gender'] = data['gender'].fillna(2).astype(int)

data['heart_beat_per_minute'] = pd.to_numeric(data['heart_beat_per_minute'], errors='coerce')
# Corrected: Use 'subset' argument to specify the column for dropping NaN values
data_cleaned = data.dropna(subset=['heart_beat_per_minute'])
print(data_cleaned.head())




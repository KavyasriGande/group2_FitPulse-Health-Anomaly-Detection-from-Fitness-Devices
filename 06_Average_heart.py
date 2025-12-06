import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)

#Calculate average heart beat by gender
avg_male_heart_beat = data.loc[data['gender'].str.lower().str.strip().isin(['male', 'm']), 'heart_beat_per_minute'].mean()
avg_female_heart_beat = data.loc[data['gender'].str.lower().str.strip().isin(['female', 'f']), 'heart_beat_per_minute'].mean()
plt.figure(figsize=(8,8))
plt.bar(['Male', 'Female'], [avg_male_heart_beat, avg_female_heart_beat], color=['green', 'yellow'],width=0.6)
plt.title("Average Heart Beat Per Minute by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Heart Beat Per Minute")
plt.show()

print(f"Average Male Heart Beat : {avg_male_heart_beat:.2f}")
print(f"Average Female Heart Beat : {avg_female_heart_beat:.2f}")


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)

#Charts
plt.bar(data['Customer_ID'], data['steps'], color='purple')
plt.title('Steps Taken by Each Customer')
plt.xlabel('Customer ID')
plt.ylabel('Steps')
plt.show()

#  Scatter plot to check correlation between steps and heart rate
plt.figure(figsize=(8,6))
plt.scatter(data['steps'], data['heart_beat_per_minute'], color='red', alpha=0.6, edgecolor='black')
plt.title('Correlation between Steps and Heart Rate', fontsize=14)
plt.xlabel('Steps', fontsize=12)
plt.ylabel('Heart Beat per Minute', fontsize=12)
plt.grid(True)
plt.show()
correlation=data['steps'].corr(data['heart_beat_per_minute'])

#### correlation
print(f"Correlation between Steps and Heart Rate :{correlation:.3f}")
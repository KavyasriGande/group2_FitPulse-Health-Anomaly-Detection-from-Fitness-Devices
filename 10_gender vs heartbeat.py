import pandas as pd
import matplotlib.pyplot as plt
file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)
print(data.head())

# Step 1: Clean and standardize the 'Gender' column
data['gender'] = data['gender'].astype(str).str.strip().str.lower().replace({'m': 'male', 'f': 'female', 'nan': 'unknown'})

# Step 2: Convert 'Heart_Beat_Per_Minute' to numeric, coercing errors to NaN
data['heart_beat_per_minute'] = pd.to_numeric(data['heart_beat_per_minute'], errors='coerce')

# Step 3: Drop rows where 'Heart_Beat_Per_Minute' is NaN
data_cleaned = data.dropna(subset=['heart_beat_per_minute'])

# Step 4: Calculate average heart rate by gender
avg_hr_by_gender=data_cleaned.groupby('gender')['heart_beat_per_minute'].mean()
print(avg_hr_by_gender)

# Step 5: Create bar plot
plt.figure(figsize=(8, 5))
plt.bar(avg_hr_by_gender.index, avg_hr_by_gender.values, color=['skyblue', 'lightcoral', 'lightgreen'])
plt.xlabel('gender')
plt.ylabel('Average Heart Rate')
plt.title('Average Heart Rate by Gender')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
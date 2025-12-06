import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np



file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
df=pd.read_excel(file_path)
# print(df.head())

# Convert 'Heart_Beat_Per_Minute' and 'Steps' to numeric, coercing errors to NaN
df['heart_beat_per_minute'] = pd.to_numeric(df['heart_beat_per_minute'], errors='coerce')
df['steps'] = pd.to_numeric(df['steps'], errors='coerce')

# Clean and create 'Gender_code' based on previous cell's logic
df['gender'] = df['gender'].astype(str).str.strip().str.replace(r'[\u200b\u200c\u200d\u200a0]','',regex=True).str.lower()
gender_mapping = {'male': 1, 'm':1,'female': 0,'f':0}
df['gender_code'] = df['gender'].map(gender_mapping).fillna(2).astype(int) # Fill NaNs for unknown genders with 2

# Drop rows where essential features for the model are NaN
df_cleaned = df.dropna(subset=['heart_beat_per_minute', 'steps'])

# Features and labels
X = df_cleaned[["steps", "heart_beat_per_minute"]]
y = df_cleaned["gender_code"]




X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)




scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train model

model = LogisticRegression()
model.fit(X_train_scaled, y_train)



y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))




new_person = pd.DataFrame({"steps": [8000],
                           "heart_beat_per_minute": [76]})

new_scaled = scaler.transform(new_person)
prediction = model.predict(new_scaled)

print("Predicted gender:", prediction[0])
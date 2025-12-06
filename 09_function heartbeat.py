import pandas as pd
file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)
print(data.head())

def heartbeat_status(hb):
    if pd.isna(hb):
        return "unknown"
    elif hb < 60:
        return "low"
    elif 60 <= hb <=100:
        return "Normal"
    else:
        return "high"

# Convert 'Heart_Beat_Per_Minute' to numeric, coercing errors to NaN
data['heart_beat_per_minute'] = pd.to_numeric(data['heart_beat_per_minute'], errors='coerce')

data["Heartbeat_status"] = data["heart_beat_per_minute"].apply(heartbeat_status)


print(data[["heart_beat_per_minute","Heartbeat_status"]].head(10))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)

#checking the heart status
def heart_status(rate):
    if rate < 60:
        return 'Low'
    elif 60 <= rate <= 100:
        return 'Normal'
    else:
        return 'High'
data['Heart_Status'] = data['heart_beat_per_minute'].apply(heart_status)
print(data[['heart_beat_per_minute', 'Heart_Status']].head(15))
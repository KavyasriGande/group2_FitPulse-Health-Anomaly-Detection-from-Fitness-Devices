import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)

# create a column and create a gender code
gender_map={'male':1,'female':0,'m':1,'f':0}
data['gender_code']=data['gender'].astype(str).str.strip().str.lower().map(gender_map).fillna(2).astype(int)
print(data[['gender','gender_code']].head(10))

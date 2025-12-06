import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"

# Read the excel file
data = pd.read_excel(file_path)
print(data)

# Open the excel file directly
os.startfile(file_path)

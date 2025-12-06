import pandas as pd
import matplotlib.pyplot as plt
file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)
print(data.head())

# Step 2 — Convert to numeric (to avoid string errors)
data["heart_beat_per_minute"] = pd.to_numeric(data["heart_beat_per_minute"], errors="coerce")
data["steps"] = pd.to_numeric(data["steps"], errors="coerce")

# Step 3 — Drop missing values in both columns
data_clean = data.dropna(subset=["heart_beat_per_minute", "steps"])

# Step 4 — Create scatter plot
plt.figure(figsize=(8,5))
plt.scatter(data_clean["steps"], data_clean["heart_beat_per_minute"], alpha=0.7)

# Step 5 — Add titles and labels
plt.title("Scatter Plot: Steps vs Heart Beat per Minute")
plt.xlabel("Steps")
plt.ylabel("Heart Beat per Minute")
plt.grid(True)

# Step 6 — Show plot
plt.show()


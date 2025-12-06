import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)
print(data.head())

# Convert 'Heart_Beat_Per_Minute' to numeric, coercing errors to NaN
data['heart_beat_per_minute'] = pd.to_numeric(data['heart_beat_per_minute'], errors='coerce')

# Drop rows where 'Heart_Beat_Per_Minute' is NaN
data_cleaned = data.dropna(subset=['heart_beat_per_minute'])

# Prepare data for K-Means
heartbeat_data = data_cleaned['heart_beat_per_minute'].to_numpy().reshape(-1, 1)

# Apply KMeans clustering
km = KMeans(n_clusters=3, init='k-means++', random_state=42, n_init=10)
km.fit(heartbeat_data)

clusters = km.predict(heartbeat_data)

# Plotting the clusters
plt.figure(figsize=(8, 4))
plt.scatter(heartbeat_data, np.zeros_like(heartbeat_data), c=clusters, cmap='viridis')
plt.title('K-Means Clustering of Heart Beat Per Minute')
plt.xlabel('Heart Beat Per Minute')
plt.yticks([]) # Hide y-axis ticks for a 1D scatter plot
plt.grid(True)
plt.show()

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
file_path=r"C:\Users\manka\OneDrive\Desktop\infosys project\Fitpulse_data.xlsx"
data=pd.read_excel(file_path)
print(data.head())

# Step 1: Clean and standardize the 'gender' column
data['gender'] = data['gender'].astype(str).str.strip().str.lower().replace({'m': 'male', 'f': 'female', 'nan': 'unknown'})

# Step 2: Convert 'heart_beat_per_minute' to numeric, coercing errors to NaN
data['heart_beat_per_minute'] = pd.to_numeric(data['heart_beat_per_minute'], errors='coerce')

# Step 3: Drop rows where 'heart_beat_per_minute' is NaN
data_cleaned = data.dropna(subset=['heart_beat_per_minute'])

# Step 4: Calculate average heart rate by gender
avg_hr_by_gender=data_cleaned.groupby('gender')['heart_beat_per_minute'].mean()
print(avg_hr_by_gender)

# Sample data
df = pd.DataFrame({
    "gender": avg_hr_by_gender.index,
    "avg_heart_rate": avg_hr_by_gender.values,
    "size": [20] * len(avg_hr_by_gender),
    "color": list(range(len(avg_hr_by_gender)))
})


# ---------------------------------------------
# 1. Scatter plot with colored markers 
fig1 = px.scatter(
    df,
    x="gender",
    y="avg_heart_rate",
    size="size",
    color="color",
    color_continuous_scale="Viridis",
    title="Scatter Plot with Color Scale"
)
fig1.show()

# ---------------------------------------------
# 2. Line chart with markers 
fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=df["gender"],
    y=df["avg_heart_rate"],
    mode="lines+markers",
    name="Line with points"
))
fig2.update_layout(title="Line Chart with Points")
fig2.show()

# ---------------------------------------------
# 3. Second line chart 
fig3 = px.line(
    df,
    x="gender",
    y="avg_heart_rate",
    markers=True,
    title="Simple Line Chart"
)
fig3.show()
import streamlit as st
import pandas as pd

st.title("👤 Gender Code Generation App")

# Upload Excel File
uploaded_file = st.file_uploader("Upload FitPulse Data Excel File", type=["xlsx"])

if uploaded_file is not None:
    # Read data
    data = pd.read_excel(uploaded_file)
    st.subheader("📄 Original Data")
    st.dataframe(data)

    # Create gender map
    gender_map = {'male': 1, 'female': 0, 'm': 1, 'f': 0}

    # Clean gender column and create gender_code
    data['gender_code'] = (
        data['gender']
        .astype(str)
        .str.strip()
        .str.lower()
        .map(gender_map)
        .fillna(2)
        .astype(int)
    )

    st.subheader("🧠 Gender Code Mapping Applied")
    st.write("Mapping used: **Male → 1**, **Female → 0**, **Unknown → 2**")

    # Show processed data
    st.subheader("📊 Data with Gender Code")
    st.dataframe(data[['gender', 'gender_code']])

    # Count of gender codes
    st.subheader("📈 Gender Code Distribution")
    gender_counts = data['gender_code'].value_counts().sort_index()

    st.bar_chart(gender_counts)

    st.success("Gender code processing completed!")

else:
    st.info("⬆ Please upload your FitPulse Excel file to continue")

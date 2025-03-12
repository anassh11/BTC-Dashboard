import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Bitcoin Dashboard")

# Bitcoin Metrics Data
data = {
    "Metric": [
        "Current Price ($)", "Market Cap ($B)", "24h Volume ($B)",
        "Bitcoin Dominance (%)", "Fear & Greed Index", "Estimated Cycle Top ($)",
        "2025 Price Prediction ($)", "200-Day EMA ($)"
    ],
    "Value": [
        83520, 1620, 48.5, 54.3, 30, 150000, 150000, 82000
    ]
}

df = pd.DataFrame(data)

# Display Dataframe
st.dataframe(df)

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df["Metric"], df["Value"], color='blue', alpha=0.7)
ax.set_xlabel("Value")
ax.set_title("Bitcoin Key Metrics Dashboard")
ax.invert_yaxis()  # Invert y-axis for better readability
st.pyplot(fig)

# Deployment Instructions
st.markdown("### How to Deploy")
st.markdown("1. Save this script as `app.py`")
st.markdown("2. Install dependencies: `pip install streamlit pandas matplotlib`")
st.markdown("3. Run locally: `streamlit run app.py`")
st.markdown("4. Deploy to Streamlit Cloud or Render for public access.")

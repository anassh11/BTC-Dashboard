import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Fetch real-time Bitcoin data from CoinGecko API
API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true"
data = requests.get(API_URL).json()["bitcoin"]

# Fetch Fear & Greed Index
greed_index = requests.get("https://api.alternative.me/fng/").json()["data"][0]["value"]

# Title
st.title("Enhanced Bitcoin Dashboard")

# Bitcoin Metrics Data
df = pd.DataFrame({
    "Metric": [
        "Current Price ($)", "Market Cap ($B)", "24h Volume ($B)", "24h Change (%)",
        "Bitcoin Dominance (%)", "Fear & Greed Index", "Estimated Cycle Top ($)",
        "2025 Price Prediction ($)", "200-Day EMA ($)"
    ],
    "Value": [
        data["usd"], data["usd_market_cap"] / 1e9, data["usd_24h_vol"] / 1e9, data["usd_24h_change"],
        54.3, greed_index, 150000, 150000, 82000
    ]
})

# Display Dataframe
st.dataframe(df)

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df["Metric"], df["Value"], color='blue', alpha=0.7)
ax.set_xlabel("Value")
ax.set_title("Bitcoin Key Metrics Dashboard")
ax.invert_yaxis()
st.pyplot(fig)

# Deployment Instructions
st.markdown("### How to Deploy")
st.markdown("1. Save this script as `app.py`")
st.markdown("2. Install dependencies: `pip install streamlit pandas matplotlib requests`")
st.markdown("3. Run locally: `streamlit run app.py`")
st.markdown("4. Deploy to Streamlit Cloud for public access.")

import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    layout="wide"
)

st.title("📊 Mutual Fund Analytics Dashboard")

st.markdown("Capstone Project - Bluestock Fintech Internship")

# -------------------------
# Dataset Overview
# -------------------------

funds = pd.read_csv("data/raw/01_fund_master.csv")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Funds", len(funds))

with col2:
    st.metric("Columns", len(funds.columns))

st.divider()

# -------------------------
# Charts
# -------------------------

st.subheader("AUM by Fund House")

img1 = Image.open("reports/charts/aum_by_fundhouse.png")
st.image(img1)

st.subheader("Monthly SIP Inflows")

img2 = Image.open("reports/charts/monthly_sip_inflows.png")
st.image(img2)

st.subheader("Category Inflows")

img3 = Image.open("reports/charts/category_inflows.png")
st.image(img3)

st.subheader("Top Sharpe Ratio Funds")

img4 = Image.open("reports/charts/top_sharpe_funds.png")
st.image(img4)

st.success("Dashboard Loaded Successfully")
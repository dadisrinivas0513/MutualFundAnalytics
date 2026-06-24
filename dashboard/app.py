import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Mutual Fund Analytics Platform",
    layout="wide"
)

# =========================
# Load Data
# =========================

funds = pd.read_csv("data/raw/01_fund_master.csv")
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

# =========================
# Sidebar
# =========================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "Overview",
        "Performance",
        "Risk Analysis"
    ]
)

# =========================
# Overview Page
# =========================

if page == "Overview":

    st.title("📊 Mutual Fund Analytics Platform")

    st.markdown("Bluestock Fintech Capstone Project")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Funds", len(funds))

    with col2:
        st.metric("Total Columns", len(funds.columns))

    with col3:
        st.metric(
            "Avg Sharpe Ratio",
            round(performance["sharpe_ratio"].mean(), 2)
        )

    st.divider()

    st.subheader("AUM by Fund House")

    st.image(
        "reports/charts/aum_by_fundhouse.png",
        use_container_width=True
    )

    st.subheader("Monthly SIP Inflows")

    st.image(
        "reports/charts/monthly_sip_inflows.png",
        use_container_width=True
    )

# =========================
# Performance Page
# =========================

elif page == "Performance":

    st.title("📈 Fund Performance")

    st.image(
        "reports/charts/top_sharpe_funds.png",
        use_container_width=True
    )

# =========================
# Risk Page
# =========================

elif page == "Risk Analysis":

    st.title("⚠ Risk & Benchmark Analysis")

    st.image(
        "reports/charts/category_inflows.png",
        use_container_width=True
    )

st.success("Dashboard Loaded Successfully")
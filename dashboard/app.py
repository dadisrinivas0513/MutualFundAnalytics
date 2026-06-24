import streamlit as st
import pandas as pd

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

st.sidebar.title("📊 Dashboard Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "Overview",
        "Performance",
        "Risk Analysis"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Quick Statistics")

st.sidebar.metric("Funds", len(funds))
st.sidebar.metric(
    "Avg Sharpe",
    round(performance["sharpe_ratio"].mean(), 2)
)

# =========================
# Overview Page
# =========================

if page == "Overview":

    st.title("📊 Mutual Fund Analytics Platform")

    st.markdown("Bluestock Fintech Capstone Project")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Funds", len(funds))

    with col2:
        st.metric("Total Columns", len(funds.columns))

    with col3:
        st.metric(
            "Avg Sharpe Ratio",
            round(performance["sharpe_ratio"].mean(), 2)
        )

    with col4:
        st.metric(
            "Avg 1Y Return",
            f"{performance['return_1yr_pct'].mean():.2f}%"
        )

    st.divider()

    st.subheader("AUM by Fund House")

    st.image(
        "reports/charts/aum_by_fundhouse.png",
        width="stretch"
    )

    st.subheader("Monthly SIP Inflows")

    st.image(
        "reports/charts/monthly_sip_inflows.png",
        width="stretch"
    )

# =========================
# Performance Page
# =========================

elif page == "Performance":

    st.title("📈 Fund Performance Analysis")

    st.metric(
        "Average Alpha",
        round(performance["alpha"].mean(), 2)
    )

    st.image(
        "reports/charts/top_sharpe_funds.png",
        width="stretch"
    )

# =========================
# Risk Analysis Page
# =========================

elif page == "Risk Analysis":

    st.title("⚠ Risk & Benchmark Analysis")

    st.metric(
        "Average Beta",
        round(performance["beta"].mean(), 2)
    )

    st.image(
        "reports/charts/category_inflows.png",
        width="stretch"
    )

st.success("Dashboard Loaded Successfully")
# Mutual Fund Analytics Platform

## Bluestock Fintech Internship Capstone Project

### Project Overview

This project focuses on analyzing Mutual Fund industry datasets using Python, SQL, and data analytics techniques. The objective is to build an end-to-end analytics platform that performs data ingestion, ETL processing, exploratory data analysis, risk analysis, benchmark comparison, and dashboard visualization.

---

## Project Objectives

* Perform data ingestion from multiple mutual fund datasets
* Build ETL pipelines for data transformation
* Store processed data in SQLite database
* Design Star Schema for analytics
* Conduct Exploratory Data Analysis (EDA)
* Analyze fund performance and risk metrics
* Compare fund performance against benchmarks
* Develop an interactive Streamlit dashboard

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQL
* Matplotlib
* Seaborn
* Streamlit
* Git & GitHub

---

## Project Structure

```text
MutualFundAnalytics
│
├── dashboard
├── data
├── database
├── notebooks
├── reports
├── scripts
├── screenshots
├── sql
├── README.md
└── requirements.txt
```

---

## Features Implemented

### Data Engineering

* Data Ingestion Pipeline
* ETL Processing
* SQLite Database Integration
* Star Schema Design

### Analytics

* AUM Analysis
* Monthly SIP Analysis
* Category Inflow Analysis
* Fund Performance Analysis
* Sharpe Ratio Ranking
* Benchmark Comparison
* Risk Metrics Analysis

### Visualization

* AUM by Fund House Chart
* Monthly SIP Inflows Chart
* Category Inflows Chart
* Top Sharpe Ratio Funds Chart

### Dashboard

* Streamlit Dashboard
* KPI Metrics
* Sidebar Navigation
* Analytics Visualization

---

## Generated Reports

* benchmark_comparison.csv
* fund_sharpe_ranks.csv
* var_drawdown_summary.csv

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

### Generate Analytics Reports

```bash
python notebooks/metrics_analysis.py
```

### Launch Dashboard

```bash
python -m streamlit run dashboard/app.py
```

---

## Future Enhancements

* Live NAV API Integration
* Interactive Plotly Visualizations
* Portfolio Optimization Module
* Mutual Fund Recommendation System
* Automated Report Generation

---

## Author

Srinivas Dadi

Bluestock Fintech Internship Capstone Project

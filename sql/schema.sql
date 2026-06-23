-- Mutual Fund Analytics Schema

CREATE TABLE dim_fund(
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT
);

CREATE TABLE fact_nav(
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL
);

CREATE TABLE fact_aum(
    fund_house TEXT,
    aum_cr REAL
);

CREATE TABLE fact_sip(
    month TEXT,
    sip_inflow_cr REAL
);

CREATE TABLE fact_transactions(
    investor_id INTEGER,
    amount REAL,
    transaction_type TEXT
);
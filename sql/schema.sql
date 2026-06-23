CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT
);

CREATE TABLE fact_nav (
    nav_date DATE,
    amfi_code INTEGER,
    nav REAL
);

CREATE TABLE fact_aum (
    report_date DATE,
    fund_house TEXT,
    aum_cr REAL
);

CREATE TABLE fact_sip (
    report_month DATE,
    sip_inflow_cr REAL
);

CREATE TABLE fact_transactions (
    transaction_date DATE,
    amount REAL,
    transaction_type TEXT
);
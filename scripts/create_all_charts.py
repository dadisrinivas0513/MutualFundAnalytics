import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("reports/charts", exist_ok=True)

# ==========================
# Chart 1 : SIP Inflows
# ==========================
df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

plt.figure(figsize=(10,5))
plt.plot(df["month"], df["sip_inflow_crore"])
plt.xticks(rotation=45)
plt.title("Monthly SIP Inflows")
plt.tight_layout()

plt.savefig("reports/charts/monthly_sip_inflows.png")
plt.close()


# ==========================
# Chart 2 : Category Inflows
# ==========================
df = pd.read_csv("data/raw/05_category_inflows.csv")

top_categories = (
    df.groupby("category")["net_inflow_crore"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_categories.plot(kind="bar")

plt.title("Top Category Inflows")
plt.tight_layout()

plt.savefig("reports/charts/category_inflows.png")
plt.close()


# ==========================
# Chart 3 : Sharpe Ratio
# ==========================
df = pd.read_csv("data/raw/07_scheme_performance.csv")

top_funds = (
    df.sort_values("sharpe_ratio", ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))
plt.bar(top_funds["scheme_name"], top_funds["sharpe_ratio"])

plt.xticks(rotation=90)
plt.title("Top 10 Funds by Sharpe Ratio")
plt.tight_layout()

plt.savefig("reports/charts/top_sharpe_funds.png")
plt.close()

print("All Charts Generated Successfully")
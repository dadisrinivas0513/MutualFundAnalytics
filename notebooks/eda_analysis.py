import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print(df.columns.tolist())
print(df.head())

latest = df.sort_values("date").groupby("fund_house").tail(1)

latest.plot(
    x="fund_house",
    y="aum_crore",
    kind="bar",
    figsize=(12,6)
)

plt.title("AUM by Fund House")
plt.tight_layout()

plt.savefig("reports/charts/aum_by_fundhouse.png")

print("Chart Saved Successfully")
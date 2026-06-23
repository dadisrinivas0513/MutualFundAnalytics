import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print(df.head())

df.plot(
    x=df.columns[0],
    y=df.columns[1],
    kind="bar"
)

plt.tight_layout()
plt.savefig("reports/aum_chart.png")

print("Chart Saved")
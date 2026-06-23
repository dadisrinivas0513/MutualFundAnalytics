import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print(df.head())

df.plot(
    x="fund_house",
    y="aum_cr",
    kind="bar",
    figsize=(12,6)
)

plt.title("AUM by Fund House")
plt.tight_layout()
plt.show()
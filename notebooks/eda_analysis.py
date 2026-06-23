import pandas as pd

funds = pd.read_csv("data/raw/01_fund_master.csv")

print("Rows:", funds.shape[0])
print("Columns:", funds.shape[1])

print(funds.head())
import pandas as pd
import os

raw_path = "data/raw"

for file in os.listdir(raw_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(raw_path, file))

        print("\n" + "=" * 50)
        print(f"File: {file}")
        print("Shape:", df.shape)
        print("\nColumns:")
        print(df.dtypes)
        print("\nFirst 5 Rows:")
        print(df.head())
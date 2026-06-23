import pandas as pd
from sqlalchemy import create_engine
import os

DATABASE_PATH = "database/mutualfund.db"

engine = create_engine(f"sqlite:///{DATABASE_PATH}")

raw_path = "data/raw"

for file in os.listdir(raw_path):

    if file.endswith(".csv"):

        table_name = file.replace(".csv","")

        file_path = os.path.join(raw_path,file)

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded {file} -> {table_name}")

print("ETL Completed Successfully")
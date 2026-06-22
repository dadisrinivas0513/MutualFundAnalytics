import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

scheme_codes = [
    125497,  # HDFC Top 100 Direct
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if "data" in data:
                df = pd.DataFrame(data["data"])

                filename = f"data/raw/{code}.csv"
                df.to_csv(filename, index=False)

                print(f"Saved {filename}")

    except Exception as e:
        print(f"Error for {code}: {e}")
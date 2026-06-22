import requests
import pandas as pd

scheme_codes = [
    125497,
    119551,
    120503,
    118632,
    119092,
    120841
]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        pd.DataFrame(data["data"]).to_csv(
            f"data/raw/{code}.csv",
            index=False
        )

        print(f"{code} saved")
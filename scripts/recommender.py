import pandas as pd

# Load scheme performance data
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

def recommend_funds(risk):

    recommended = (
        performance[performance["risk_grade"] == risk]
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    return recommended[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct",
            "aum_crore"
        ]
    ]


risk = input(
    "Enter Risk Appetite (Low/Moderate/Moderately High/High/Very High): "
)

recommendation = recommend_funds(risk)

print("\nTop Recommended Funds\n")

print(recommendation)
import pandas as pd
import os

df = pd.read_csv("data/raw/07_scheme_performance.csv")

os.makedirs("reports", exist_ok=True)

# Top Sharpe Funds
sharpe_rank = df.sort_values(
    by="sharpe_ratio",
    ascending=False
)

sharpe_rank.to_csv(
    "reports/fund_sharpe_ranks.csv",
    index=False
)

# Drawdown Summary
drawdown = df[
    [
        "scheme_name",
        "fund_house",
        "max_drawdown_pct",
        "beta",
        "alpha"
    ]
]

drawdown.to_csv(
    "reports/var_drawdown_summary.csv",
    index=False
)

# Benchmark Comparison
benchmark = df[
    [
        "scheme_name",
        "return_3yr_pct",
        "benchmark_3yr_pct",
        "alpha"
    ]
]

benchmark.to_csv(
    "reports/benchmark_comparison.csv",
    index=False
)

print("Metrics Reports Generated")
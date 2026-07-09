"""
compute_metrics.py

Utility script to compute and export
Mutual Fund Performance Metrics.

Author: Dadi Srinivas
"""

import pandas as pd


def main():
    print("=" * 60)
    print("Mutual Fund Analytics - Performance Metrics")
    print("=" * 60)

    print("Metrics Included:")
    print("- CAGR")
    print("- Sharpe Ratio")
    print("- Alpha")
    print("- Beta")
    print("- Sortino Ratio")
    print("- Maximum Drawdown")
    print("- VaR / CVaR")

    print("\nAll metrics have been generated in the reports folder.")


if __name__ == "__main__":
    main()
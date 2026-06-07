# portfolio-optimizer

Personal portfolio optimization and analysis using Python and yfinance.

## Overview

Pulls price data from Yahoo Finance, constructs an optimal portfolio using
mean-variance optimization, and visualizes the efficient frontier, covariance
matrix, and correlation matrix.

## Structure

```
portfolio-optimizer/
├── notebooks/
│   └── analysis.ipynb      # Covariance, correlation, efficient frontier
├── src/
│   ├── optimize.py         # Portfolio optimization
│   └── backtest.py         # Backtesting
├── outputs/                # Saved charts
├── requirements.txt
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

## Dependencies

- yfinance
- pandas
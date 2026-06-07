# Portfolio Optimizer

Personal portfolio optimization and analysis using Python and yfinance.

## Overview

Pulls price data from Yahoo Finance, constructs an optimal portfolio using
mean-variance optimization, and visualizes the efficient frontier, covariance
matrix, and correlation matrix.

## Structure
├── notebooks/
│   └── analysis.ipynb   # covariance, correlation, efficient frontier
├── src/
│   ├── optimize.py      # portfolio optimization
│   └── backtest.py      # backtesting
├── outputs/             # saved charts
├── requirements.txt
└── README.md

## Setup

```bash
pip install -r requirements.txt
```

## Dependencies

- yfinance
- pandas
- seaborn
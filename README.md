# Portfolio Optimizer

Personal portfolio optimization and analysis using Python and yfinance.

## Overview

Pulls price data from Yahoo Finance, constructs an optimal portfolio using
mean-variance optimization, and visualizes the efficient frontier, covariance
matrix, and correlation matrix.

## Structure

    quant-portfolio/
    notebooks/
        analysis.ipynb
    src/
        optimize.py
        backtest.py
    outputs/
    requirements.txt
    README.md

## Setup
```bash
pip install -r requirements.txt
```

## Dependencies

- yfinance
- pandas
- seaborn
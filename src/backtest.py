import numpy as np
import pandas as pd

def backtest(returns, weights, risk_free_rate=0.04, rebalance='monthly'):
    tickers = returns.columns
    weights = pd.Series(weights, index=tickers)

    if rebalance == 'monthly':
        freq = 'ME'
    elif rebalance == 'quarterly':
        freq = 'QE'
    elif rebalance == 'yearly':
        freq = 'YE'
    else:
        freq = None

    if freq:
        rebalance_dates = returns.resample(freq).last().index
    
    portfolio_returns = []
    current_weights = weights.copy()

    for date, row in returns.iterrows():
        if freq and date in rebalance_dates:
            current_weights = weights.copy()
        
        daily_return = (current_weights * row).sum()
        portfolio_returns.append((date, daily_return))

        current_weights = current_weights * (1 + row)
        current_weights = current_weights / current_weights.sum()

    portfolio_returns = pd.Series(
        [r for _, r in portfolio_returns],
        index=[d for d, _ in portfolio_returns]
    )

    cumulative_returns = (1 + portfolio_returns).cumprod()
    total_days = len(portfolio_returns)
    cagr = cumulative_returns.iloc[-1] ** (252 / total_days) - 1
    volatility = portfolio_returns.std() * np.sqrt(252)
    sharpe = (portfolio_returns.mean() * 252 - risk_free_rate) / volatility
    rolling_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns - rolling_max) / rolling_max
    max_drawdown = drawdown.min()

    metrics = {
        'CAGR': round(cagr, 4),
        'Volatility': round(volatility, 4),
        'Sharpe Ratio': round(sharpe, 4),
        'Max Drawdown': round(max_drawdown, 4),
        'Final Value': round(cumulative_returns.iloc[-1], 4)
    }

    return portfolio_returns, cumulative_returns, metrics
import numpy as np
from scipy.optimize import minimize

def max_sharpe(expected_returns, cov_matrix, risk_free_rate=0.04):
    n = len(expected_returns)
    initial_weights = np.ones(n) / n

    def neg_sharpe_ratio(weights):
        portfolio_return = weights @ expected_returns.values
        portfolio_volatility = np.sqrt(weights @ cov_matrix.values @ weights)
        return -(portfolio_return - risk_free_rate) / portfolio_volatility
    
    constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1}]
    bounds = [(0, 1)] * n
    result = minimize(neg_sharpe_ratio, 
                      initial_weights,
                      method='SLSQP',
                      constraints=constraints, 
                      bounds=bounds)
    
    if not result.success:
        raise ValueError(f"Optimizer failed: {result.message}")
    return result.x
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# chose mix of toronto stocks
# the whole market, TD bank usually stable, and shop which is more volatile
tickers = ["XIU.TO", "TD.TO", "SHOP.TO"]

data = yf.download(tickers, start="2020-01-01", end="2026-01-01")["Close"]

print(data.head())

# observe which grows earlier, one might be most volatile (standard deviation) and look for smooth
data.plot(title="Toronto Stocks Price Comparison (2020–2025)")
plt.show()

normalized_data = data / data.iloc[0]

# converted everything to begin at 1
normalized_data.plot(title="Normalized Prices (Start = 1)")
plt.show()

returns = data.pct_change().dropna()
print(returns.head())

# the correlation between them all
sns.heatmap(returns.corr(), annot=True)
plt.title("The Correlation Between Stocks")
plt.show()

# Portfolio Simulation

# we will simulate 5000 portfolios
num_portfolios = 5000
results = []

for i in range(num_portfolios):
    weights = np.random.random(len(tickers))
    weights /= np.sum(weights)

    # portfolio return
    portfolio_return = np.sum(returns.mean() * weights) * 252

    # portfolio risk (volatility)
    portfolio_volatility = np.sqrt(
        np.dot(weights.T, np.dot(returns.cov() * 252, weights))
    )

    results.append((portfolio_return, portfolio_volatility))

results = np.array(results)

# plotting the random portfolios we generated
plt.scatter(results[:,1], results[:,0])
plt.xlabel("Volatility (Risk)")
plt.ylabel("Return")
plt.title("Portfolio Risk vs Return")
plt.show()

# now we want the best portfolio which is highest return but with the lowest risk possible for that return
sharpe_ratios = results[:,0] / results[:,1]

best_index = np.argmax(sharpe_ratios)

best_return = results[best_index, 0]
best_volatility = results[best_index, 1]

print("Best Portfolio Return:", best_return)
print("Best Portfolio Volatility:", best_volatility)

plt.scatter(results[:,1], results[:,0], alpha=0.3)
plt.scatter(best_volatility, best_return, color='red', s=100)

plt.xlabel("Volatility (Risk)")
plt.ylabel("Return")
plt.title("Portfolio Optimization")
plt.show()
# Toronto Stock Market Analysis

## Overview

This project analyzes historical stock data from three Toronto-listed assets to compare performance, volatility, and diversification. The goal is to understand how different types of stocks behave over time and how combining them can affect overall portfolio risk.

The assets included are:

* XIU.TO (TSX Composite Index ETF)
* TD.TO (Toronto-Dominion Bank)
* SHOP.TO (Shopify)

---

## Data

Data was collected using the `yfinance` library for the period from January 2020 to January 2026. Daily closing prices were used for all analysis.

---

## Method

The analysis was done in several steps:

1. **Price Comparison**
   Raw prices were plotted to observe general trends and relative performance.

2. **Normalization**
   Prices were scaled to start at 1 to make growth comparable across assets.

3. **Returns**
   Daily returns were calculated using percentage change to analyze volatility.

4. **Correlation**
   A correlation matrix was computed to understand relationships between assets.

5. **Risk vs Return**
   Average returns and standard deviations were compared to evaluate trade-offs between risk and reward.

---

## Results

### Price Comparison

![Price Comparison](images/price_comparison.png)

This shows that Shopify had the largest price movements over time, while TD and XIU were more stable.

---

### Normalized Prices

![Normalized Prices](images/normalized_prices_graph.png)

After normalization, Shopify shows the strongest growth, but also more fluctuation compared to the other two assets.

---

### Correlation Heatmap

![Correlation Heatmap](images/correlation_graph.png)

TD and XIU are more strongly correlated, while Shopify is less correlated with both, suggesting it may provide diversification benefits.

---

### Risk vs Return

![Risk vs Return](images/risk_vs_return_graph.png)

Shopify has the highest return but also the highest volatility. TD and XIU offer lower risk but also lower returns.

---

### Portfolio Insight

![Portfolio Optimization](images/optimization.png)

Combining assets with lower correlation can improve diversification and reduce overall portfolio risk.

---

## Tools Used

* Python
* pandas
* numpy
* matplotlib
* seaborn
* yfinance

---

## How to Run

Install required packages:

```id="c2wn4y"
pip install yfinance pandas matplotlib seaborn numpy
```

Run the script:

```id="p2d4yq"
python stock_analysis.py
```

---

## Notes

This project was completed as part of practicing data analysis and applying basic financial concepts using Python.

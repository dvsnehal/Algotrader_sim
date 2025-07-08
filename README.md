# Algorithmic Trading Simulator

The project is a Streamlit-based interactive stock trading simulator that allows you to backtest various algorithmic trading strategies on real historical stock data fetched from Yahoo Finance.

---

## Features

-  Fetches real-time stock data using Yahoo Finance
-  Implements 3 key trading strategies:
     - Moving Average Crossover
     -   Momentum (3-Day Trend)
     -   Drop-Recovery (Dip Buying)
-  Simulates trading using full capital allocation (no fractional shares)
-  Interactive visualisations of buy/sell decisions using Matplotlib
-  Performance comparison across strategies with metrics like:
   - Final cash
   - Net profit
   - % Return
   - Number of trades

---
## Strategy Overview

1. Moving Average Crossover
   - Buys when the short-term moving average crosses above the long-term average
   - Sells when it crosses below the long-term average

2. Momentum (3-Day Trend)
   - Buys after 3 consecutive price increases
   - 	Sells after 3 consecutive decreases

3. Drop-Recovery Strategy
   - Buys after a multi-day price drop.
   - Sells when a multi-day price increase is observed and the price exceeds the buy price

## Note on Discarded Strategies

Originally, the project included **Greedy** and **Greedy with Cooldown** based strategies. These were removed from the final version because they relied on future price information to make present decisions — an approach that isn't applicable to real-world trading. 

We aim to keep all strategies realistic and causal, using only past and current data for decision-making.

## Project Structure
<pre><code>
├── main.py             # Streamlit frontend and Strategy execution
├── plotter.py          # Visualises buy/sell trades on stock chart
├── strategies/         # Strategy implementations
│   ├── ma_crossover.py
│   ├── momentum.py
│   └── drop_recovery.py
├── utils/              # Utility functions
│   └── summary.py      # Displays strategy comparison table
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
</code></pre>

## Future Improvement Opportunities

A key enhancement planned is the integration of a stock price prediction model using machine learning or time series forecasting.
This would allow us to apply the current strategies (like Moving Average Crossover, Momentum, Drop-Recovery, etc.) on predicted future prices instead of historical data.
Such a setup would simulate more realistic forward-looking trading and help evaluate strategy performance under predicted market behaviour.

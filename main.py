import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from strategies.greedy import run_greedy_strategy
from strategies.dp_strategy import run_dp_strategy
from strategies.ma_crossover import run_ma_crossover_strategy
from utils.summary import show_summary
from strategies.momentum import run_momentum_strategy
from strategies.drop_recover import run_drop_recovery_strategy
from plotter import show_trade_chart

st.set_page_config(page_title="Algorithmic Trading Simulator", layout="wide")
st.title("Algo-Trading Simulator")
st.info("This will let you know how different algorithms work on the selected stock")
st.markdown("Enter a stock ticker (e.g.`AAPL`,`TSLA`,`INFY.NS`) to simulate trading strategies on recent data.")

# Taking stock symbol as input
ticker=st.text_input("Enter Stock Ticker:", value="AAPL")
initial_cash=st.number_input("Initial Cash (₹)", min_value=1000, value=10000, step=1000)

# Backtest period selector
period_option=st.selectbox(
    "Select Backtest Period:",
    options=["6 months", "1 year", "2 years", "3 years", "5 years", "Max"],
    index=4  # default set to "5 years"
)

# Mapping option to yfinance-compatible period
period_mapping={
    "6 months": "6mo",
    "1 year": "1y",
    "2 years": "2y",
    "3 years": "3y",
    "5 years": "5y",
    "Max": "max"
}

selected_period=period_mapping[period_option]

if st.button("📈 Fetch Data & Run Simulation"):
    with st.spinner("Fetching data from Yahoo Finance..."):
        try:
            data=yf.download(ticker, period=selected_period, interval="1d")
            if len(data) < 60:
                st.warning("Insufficient data for chosen backtest period or strategy window. Try a longer time range or a different stock.")
            data=data[['Close']].dropna()
            data.reset_index(inplace=True)

            if data.empty:
                st.error("No data found. Please enter a valid ticker.")
            else:
                st.success(f"Data loaded successfully for {ticker}!")
                st.write(data.head())

                ma_results=run_ma_crossover_strategy(data, initial_cash)
                st.subheader("🫮 Moving Average Crossover Results")
                st.metric("Final Cash", f"₹ {ma_results['final_cash']}")
                st.metric("Total Profit", f"₹ {ma_results['profit']}")
                st.metric("Number of Trades", ma_results['trades'])
                show_trade_chart(data, ma_results["buy_signals"], ma_results["sell_signals"], ma_results["strategy"])

                momentum_results=run_momentum_strategy(data, initial_cash)
                st.subheader(" Momentum Strategy Results")
                st.metric("Final Cash", f"₹ {momentum_results['final_cash']}")
                st.metric("Total Profit", f"₹ {momentum_results['profit']}")
                st.metric("Number of Trades", momentum_results['trades'])
                show_trade_chart(data, momentum_results["buy_signals"], momentum_results["sell_signals"], momentum_results["strategy"])

                dr_results=run_drop_recovery_strategy(data, initial_cash, drop_days=3, rise_days=2)
                st.subheader(" Drop-Recovery Strategy Results")
                st.metric("Final Cash", f"₹ {dr_results['final_cash']}")
                st.metric("Total Profit", f"₹ {dr_results['profit']}")
                st.metric("Number of Trades", dr_results['trades'])
                show_trade_chart(data, dr_results["buy_signals"], dr_results["sell_signals"], dr_results["strategy"])

                all_results=[
                    ma_results,
                    momentum_results,
                    dr_results
                ]

                show_summary(all_results, initial_cash)

        except Exception as e:
            st.error(f"Error fetching data: {e}")

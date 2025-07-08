import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def show_trade_chart(data, buy_signals, sell_signals, strategy_name):
    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(data["Date"], data["Close"], label="Price", color='blue', linewidth=2)

    if buy_signals:
        buy_dates = [pd.to_datetime(b[0]) for b in buy_signals]
        buy_prices = [b[1] for b in buy_signals]
        ax.scatter(buy_dates, buy_prices, color='green', label='Buy', marker='^', s=100)

    if sell_signals:
        sell_dates = [pd.to_datetime(s[0]) for s in sell_signals]
        sell_prices = [s[1] for s in sell_signals]
        ax.scatter(sell_dates, sell_prices, color='red', label='Sell', marker='v', s=100)

    ax.set_title(f"{strategy_name} - Buy/Sell Signals")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (₹)")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
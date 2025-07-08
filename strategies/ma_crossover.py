def run_ma_crossover_strategy(data,initial_cash,short_window=20,long_window=50):
    prices=data["Close"].squeeze().tolist()
    dates=data["Date"].tolist()
    n=len(prices)

    if n<long_window:
        return {
            "strategy":"MA Crossover",
            "final_cash":initial_cash,
            "profit":0,
            "trades":0,
            "buy_signals":[],
            "sell_signals":[]
        }

    cash=initial_cash
    position=0
    num_shares=0
    trades=0
    buy_signals=[]
    sell_signals=[]

    for i in range(long_window,n):
        short_avg=sum(prices[i-short_window:i])/short_window
        long_avg=sum(prices[i-long_window:i])/long_window

        if short_avg>long_avg and position==0:
            buy_price=prices[i]
            num_shares=cash//buy_price
            cash-=num_shares*buy_price
            position=1
            trades+=1
            buy_signals.append((dates[i],prices[i]))

        elif short_avg<long_avg and position==1:
            sell_price=prices[i]
            cash+=num_shares*sell_price
            position=0
            sell_signals.append((dates[i],prices[i]))

    if position==1:
        cash+=num_shares*prices[-1]
        sell_signals.append((dates[-1],prices[-1]))

    return {
        "strategy":"MA Crossover",
        "final_cash":round(cash,2),
        "profit":round(cash-initial_cash,2),
        "trades":trades,
        "buy_signals":buy_signals,
        "sell_signals":sell_signals
    }
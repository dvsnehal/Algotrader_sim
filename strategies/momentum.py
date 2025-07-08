def run_momentum_strategy(data,initial_cash):
    prices=data["Close"].squeeze().tolist()
    dates=data["Date"].tolist()
    n=len(prices)

    cash=initial_cash
    position=0
    num_shares=0
    trades=0
    buy_signals=[]
    sell_signals=[]

    for i in range(3,n):
        up_trend=all(prices[j]>prices[j-1] for j in range(i-2,i+1))
        down_trend=all(prices[j]<prices[j-1] for j in range(i-2,i+1))

        if up_trend and position==0:
            buy_price=prices[i]
            num_shares=cash//buy_price
            cash-=num_shares*buy_price
            position=1
            trades+=1
            buy_signals.append((dates[i],prices[i]))

        elif down_trend and position==1:
            sell_price=prices[i]
            cash+=num_shares*sell_price
            position=0
            sell_signals.append((dates[i],prices[i]))

    if position==1:
        cash+=num_shares*prices[-1]
        sell_signals.append((dates[-1],prices[-1]))

    return {
        "strategy":"Momentum (3-Day Trend)",
        "final_cash":round(cash,2),
        "profit":round(cash-initial_cash,2),
        "trades":trades,
        "buy_signals":buy_signals,
        "sell_signals":sell_signals
    }
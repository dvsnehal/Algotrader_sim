def run_drop_recovery_strategy(data, initial_cash, drop_days=3, rise_days=2):
    prices=data["Close"].squeeze().tolist()
    n=len(prices)

    cash=initial_cash
    position=0
    num_shares=0
    buy_price=0
    trades=0

    buy_signals=[]
    sell_signals=[]

    i=max(drop_days, rise_days)

    while i<n:
        if position==0:
            drop=all(prices[j] < prices[j-1] for j in range(i-drop_days+1, i+1))
            if drop:
                buy_price=prices[i]
                num_shares=cash//buy_price
                if num_shares>0:
                    cash-=num_shares*buy_price
                    position=1
                    trades+=1
                    buy_signals.append((str(data["Date"][i]), buy_price))
                i+=1
                continue

        elif position==1:
            rise=all(prices[j]>prices[j-1] for j in range(i-rise_days+1, i+1))
            if rise and prices[i]>buy_price:
                sell_price=prices[i]
                cash+=num_shares*sell_price
                position=0
                sell_signals.append((str(data["Date"][i]), sell_price))
                i+=1
                continue

        i+=1

    if position==1:
        final_sell_price=prices[-1]
        cash+=num_shares*final_sell_price
        sell_signals.append((str(data["Date"].iloc[-1]), final_sell_price))

    return {
        "strategy": f"Drop-Recovery (↓{drop_days} ↑{rise_days})",
        "final_cash": round(cash, 2),
        "profit": round(cash - initial_cash, 2),
        "trades": trades,
        "buy_signals": buy_signals,
        "sell_signals": sell_signals
    }
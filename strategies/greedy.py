def run_greedy_strategy(data, initial_cash):
    prices = data["Close"].squeeze().tolist()
    n = len(prices)

    cash = initial_cash
    position = 0
    num_shares = 0
    trades = 0

    for i in range(n - 1):
        if prices[i + 1] > prices[i] and position == 0:
            buy_price = prices[i]
            num_shares = cash // buy_price
            cash -= num_shares * buy_price
            position = 1
            trades += 1

        elif prices[i + 1] < prices[i] and position == 1:
            sell_price = prices[i]
            cash += num_shares * sell_price
            position = 0

    if position == 1:
        cash += num_shares * prices[-1]

    return {
        "strategy": "Greedy (Future Price)",
        "final_cash": round(cash, 2),
        "profit": round(cash - initial_cash, 2),
        "trades": trades
    }
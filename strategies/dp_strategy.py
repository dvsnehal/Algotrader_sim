def run_dp_strategy(data, initial_cash):
    prices=data["Close"].squeeze().tolist()
    n = len(prices)
    if n == 0:
        return {"strategy": "DP", "final_cash": initial_cash, "profit": 0, "trades": 0}

    dp = [0] * n
    action = [0] * n

    dp[0] = 0

    for i in range(1, n):
        skip = dp[i - 1]
        trade = prices[i] - prices[i - 1]
        if i > 1:
            trade += dp[i - 2]

        if trade > skip:
            dp[i] = trade
            action[i] = 1
        else:
            dp[i] = skip

    # simulate trades
    cash = initial_cash
    num_shares = 0
    position = 0
    trades = 0
    i = n - 1

    while i >= 1:
        if action[i] == 1 and position == 0:
            buy_price = prices[i - 1]
            num_shares = cash // buy_price
            cash -= num_shares * buy_price
            position = 1
            trades += 1
            i -= 2
        elif action[i] == 1 and position == 1:
            sell_price = prices[i]
            cash += num_shares * sell_price
            position = 0
            i -= 2
        else:
            i -= 1

    if position == 1:
        cash += num_shares * prices[-1]

    return {
        "strategy": "DP",
        "final_cash": round(cash, 2),
        "profit": round(cash - initial_cash, 2),
        "trades": trades
    }
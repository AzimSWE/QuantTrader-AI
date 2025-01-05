def place_order(symbol, quantity, signal):
    action = "BUY" if signal == 1 else "SELL"
    print(f"{action} {quantity} shares of {symbol}")

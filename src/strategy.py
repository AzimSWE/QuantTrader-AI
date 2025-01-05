def mean_reversion_strategy(data):
    signals = []
    rolling_mean = data['close'].rolling(window=5).mean()
    for i in range(len(data)):
        if data['close'][i] < rolling_mean[i] * 0.95:
            signals.append(1)  # Buy
        elif data['close'][i] > rolling_mean[i] * 1.05:
            signals.append(-1)  # Sell
        else:
            signals.append(0)  # Hold
    return signals

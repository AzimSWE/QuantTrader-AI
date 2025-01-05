import csv
from datetime import datetime

def log_trade(symbol, signal):
    action = "BUY" if signal == 1 else "SELL"
    price = 100  # Mock price
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('data/trade_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, symbol, action, price])

from src.data_fetcher import fetch_stock_data
from src.strategy import mean_reversion_strategy
from src.trade_execution import place_order
from src.logger import log_trade

SYMBOL = "AAPL"
QUANTITY = 1

def main():
    data = fetch_stock_data(SYMBOL)
    signals = mean_reversion_strategy(data)
    latest_signal = signals[-1]
    if latest_signal != 0:
        place_order(SYMBOL, QUANTITY, latest_signal)
        log_trade(SYMBOL, latest_signal)

if __name__ == "__main__":
    main()

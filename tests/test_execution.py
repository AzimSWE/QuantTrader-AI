from src.trade_execution import place_order

def test_place_order():
    place_order("AAPL", 10, 1)  # Expected output: "BUY 10 shares of AAPL"

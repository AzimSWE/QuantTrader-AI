import pandas as pd

def fetch_stock_data(symbol):
    # Mock data
    data = {
        'close': [100, 102, 98, 97, 105, 110, 108, 107],
    }
    return pd.DataFrame(data)

from src.strategy import mean_reversion_strategy
import pandas as pd

def test_mean_reversion():
    data = pd.DataFrame({'close': [100, 102, 98, 97, 105]})
    signals = mean_reversion_strategy(data)
    assert len(signals) == len(data), "Signal length mismatch!"

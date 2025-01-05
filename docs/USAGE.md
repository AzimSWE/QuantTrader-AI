Here’s the **`USAGE.md`** file in a simpler, non-AI-like, GitHub-friendly format:

---

# **Usage Guide: QuantTrader**

This guide explains how to set up, run, and use the QuantTrader bot.

---

## **1. Setup**

### **Install Dependencies**
1. Make sure Python 3.8+ is installed.
2. Install required libraries:
   - `pandas`: For data handling.
   - `matplotlib`: For optional performance visualization.
   - `alpaca-trade-api`: For stock data and trading API (if applicable).

   Run the following commands in your Python environment:
   ```plaintext
   pip install pandas matplotlib alpaca-trade-api
   ```

---

## **2. Running the Bot**

### **Locate and Run the Script**
1. Go to the `src/` folder and open `main.py`.
2. Run the script in Python:
   - Use Python IDLE, VS Code, or any other editor.
   - Press **F5** (or the equivalent Run button) to start the program.

### **What to Expect**
- The bot will analyze the data and print trading signals like this:
  ```
  BUY 1 shares of AAPL
  SELL 1 shares of AAPL
  ```

---

## **3. Logs and Results**

### **Trade Logs**
- The bot saves trades in `data/trade_log.csv`.
- Open the file in Excel or Google Sheets to review:
  | Timestamp           | Symbol | Signal | Price |
  |---------------------|--------|--------|-------|
  | 2023-01-01 10:00:00 | AAPL   | BUY    | 150   |
  | 2023-01-02 14:00:00 | AAPL   | SELL   | 155   |

---

## **4. Customize the Bot**

### **Set Your Stock and Quantity**
- Open `main.py` and change:
  - **Stock Symbol**:
    ```python
    SYMBOL = "AAPL"  # Replace "AAPL" with the stock you want to trade.
    ```
  - **Trade Quantity**:
    ```python
    QUANTITY = 1  # Number of shares to trade.
    ```

### **Optional: Add API Credentials**
- If using live trading, open `data_fetcher.py` and update:
  ```python
  API_KEY = 'your_api_key'
  SECRET_KEY = 'your_secret_key'
  ```

---

## **5. Optional: Visualize Performance**

### **Enable Graphs**
1. Open `logger.py` and add this function:
   ```python
   import pandas as pd
   import matplotlib.pyplot as plt

   def plot_performance(log_file='data/trade_log.csv'):
       data = pd.read_csv(log_file)
       data['Timestamp'] = pd.to_datetime(data['Timestamp'])
       data.set_index('Timestamp', inplace=True)
       data['Cumulative Profit'] = data['Price'].cumsum()
       data['Cumulative Profit'].plot(title="Trading Performance")
       plt.xlabel("Time")
       plt.ylabel("Cumulative Profit")
       plt.show()
   ```

2. Call the function in `main.py`:
   ```python
   from src.logger import plot_performance
   plot_performance()
   ```

---

## **6. Troubleshooting**

### **Common Issues**
- **Missing Libraries**: Install missing libraries by running:
  ```plaintext
  pip install pandas matplotlib alpaca-trade-api
  ```
- **No Trade Logs**: Check `main.py` to ensure the strategy is generating buy/sell signals.

---

## **7. Contribute or Report Issues**
- For questions, feedback, or to contribute, visit the repository: [QuantTrader GitHub](https://github.com/yourusername/QuantTrader).

---

This version is clean, concise, and fits well in a GitHub repository. Would you like further edits or to create matching `README.md` content?
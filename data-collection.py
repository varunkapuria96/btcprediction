import yfinance as yf
import datetime
import pandas as pd
import os

def fetch_and_store_data(ticker_symbol):
    # Fetching data from Monday to Friday of the current week
    today = datetime.datetime.now()
    start_date = (today - datetime.timedelta(days=today.weekday())).strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')

    # Fetch the stock data
    data = yf.download(ticker_symbol, start=start_date, end=end_date)
    
    # Define the CSV file path
    file_path = f"{ticker_symbol}.csv"
    
    # Check if the file already exists
    if os.path.exists(file_path):
        # If the file exists, append without writing the header
        data.to_csv(file_path, mode='a', header=False)
        print(f"Data appended to {file_path}")
    else:
        # If the file does not exist, write with the header
        data.to_csv(file_path, mode='w', header=True)

if __name__ == "__main__":
    if datetime.datetime.today().weekday() == 4:  # Check if today is Friday
        fetch_and_store_data('BTC-USD')  # For BTC data
        fetch_and_store_data('AAPL')  # For AAPL data
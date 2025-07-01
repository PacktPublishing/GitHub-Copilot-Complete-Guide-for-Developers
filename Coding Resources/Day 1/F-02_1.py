import requests
import pandas as pd
from datetime import datetime

import matplotlib.pyplot as plt

# Function to fetch Bitcoin price data
def fetch_bitcoin_data():
    url = "https://api.coindesk.com/v1/bpi/historical/close.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['bpi']
    else:
        print("Failed to fetch data")
        return None

# Function to visualize Bitcoin price data
def visualize_bitcoin_prices(data):
    dates = list(data.keys())
    prices = list(data.values())

    # Convert string dates to datetime objects
    dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]

    # Create a DataFrame for better handling
    df = pd.DataFrame({'Date': dates, 'Price': prices})
    df.sort_values('Date', inplace=True)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Price'], label='Bitcoin Price', color='blue')
    plt.title('Bitcoin Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Main script
if __name__ == "__main__":
    bitcoin_data = fetch_bitcoin_data()
    if bitcoin_data:
        visualize_bitcoin_prices(bitcoin_data)
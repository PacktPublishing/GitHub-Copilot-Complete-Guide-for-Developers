from flask import Flask, jsonify
import requests
import csv
from datetime import datetime  # Import datetime for timestamp

app = Flask(__name__)

@app.route('/crypto-prices', methods=['GET'])
def get_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,  # Updated to fetch 100 cryptocurrencies
        'page': 1,
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        prices = [
            {'symbol': coin['symbol'], 'price': coin['current_price']}
            for coin in data
        ]
        
        # Save to CSV with timestamp
        with open('crypto_prices.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Symbol', 'Price', 'Timestamp'])  # Write header
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current timestamp
            for coin in prices:
                writer.writerow([coin['symbol'], coin['price'], current_time])  # Write data rows with timestamp
        
        return jsonify(prices)
    else:
        return jsonify({'error': 'Failed to fetch cryptocurrency prices'}), 500

if __name__ == '__main__':
    app.run(debug=True)
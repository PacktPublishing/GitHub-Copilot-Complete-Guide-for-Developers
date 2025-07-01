from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/crypto-prices', methods=['GET'])
def get_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        prices = [
            {'name': coin['name'], 'symbol': coin['symbol'], 'price': coin['current_price']}
            for coin in data
        ]
        return jsonify(prices)
    else:
        return jsonify({'error': 'Failed to fetch cryptocurrency prices'}), 500

if __name__ == '__main__':
    app.run(debug=True)
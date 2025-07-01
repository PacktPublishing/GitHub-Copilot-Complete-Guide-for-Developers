import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Function to fetch live cryptocurrency prices
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,binancecoin,cardano,solana,polkadot,shiba-inu,litecoin&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:  # Fixed typo here
        return response.json()
    else:
        return {crypto: "Error fetching price" for crypto in ["Bitcoin", "Ethereum", "Dogecoin", "BinanceCoin", "Cardano", "Solana", "Polkadot", "Tron", "Shiba Inu", "Litecoin"]}

# Function to fetch live gold price
def fetch_gold_price():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {"x-access-token": "goldapi-free-access"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {"gold": data["price"]}
    else:
        return {"gold": "Error fetching price"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/prices')
def get_prices():
    crypto_prices = fetch_crypto_prices()
    gold_price = fetch_gold_price()
    return jsonify({**crypto_prices, **gold_price})

if __name__ == '__main__':
    app.run(debug=True)
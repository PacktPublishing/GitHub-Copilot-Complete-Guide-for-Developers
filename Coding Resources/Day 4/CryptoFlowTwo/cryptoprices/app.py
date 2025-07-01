import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Function to fetch live cryptocurrency prices
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,binancecoin,cardano,solana,polkadot,shiba-inu,litecoin&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {crypto: {"usd": "Error fetching price"} for crypto in ["Bitcoin", "Ethereum", "Dogecoin", "BinanceCoin", "Cardano", "Solana", "Polkadot", "Shiba Inu", "Litecoin"]}

# Function to fetch the price of gold
def fetch_gold_price():
    url = "https://metals-api.com/api/latest?access_key=your_api_key&base=USD&symbols=XAU"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {"Gold": {"usd": data["rates"]["XAU"]}}
    else:
        return {"Gold": {"usd": "Error fetching price"}}

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
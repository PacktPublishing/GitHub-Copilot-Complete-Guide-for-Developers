import requests
from datetime import datetime
import schedule
import time

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token_here'
CHAT_ID = 'your_chat_id_here'

# Weather API Key and URL
WEATHER_API_KEY = 'your_weather_api_key_here'
WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'

# Function to get weather data
def get_weather():
    params = {
        'key': WEATHER_API_KEY,
        'q': 'Paris',
        'aqi': 'no'
    }
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return f"Weather in Paris: {data['current']['condition']['text']}, " \
               f"Temperature: {data['current']['temp_c']}°C"
    else:
        return "Failed to fetch weather data."

# Function to send message via Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, json=payload)

# Scheduled task
def scheduled_task():
    weather_message = get_weather()
    send_telegram_message(weather_message)

# Schedule the task at 9 AM daily
schedule.every().day.at("09:00").do(scheduled_task)

print("Bot is running and will send weather updates daily at 9 AM.")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
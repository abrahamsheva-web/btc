import time
import requests
from telegram import Bot

# Replace with your Telegram bot token and channel chat ID
TELEGRAM_TOKEN = "your Telegram bot token"
CHANNEL_CHAT_ID = "Use channel name"  # Use channel name or chat ID

# Function to get the current Bitcoin price using Blockchair's API
def get_btc_price():
    url = "https://api.blockchair.com/bitcoin/stats"
    response = requests.get(url)
    data = response.json()
    # The price is located in the "market_price_usd" field
    return data['data']['market_price_usd']

# Function to send the message to Telegram channel
def send_message_to_telegram(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHANNEL_CHAT_ID, text=message)

# Main loop to send BTC price every 1 minute
while True:
    price = get_btc_price()
    message = f"Current Bitcoin Price: ${price}"
    send_message_to_telegram(message)
    print(f"Sent message: {message}")
    time.sleep(60)  # Wait for 1 minute before sending again

import os
import time
import requests

# Telegram bot token and chat ID from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_CHAT_ID = os.getenv("CHANNEL_CHAT_ID")

# Function to get the current Bitcoin price using Blockchair's API
def get_btc_price():
    try:
        url = "https://api.blockchair.com/bitcoin/stats"
        response = requests.get(url, timeout=10)
        data = response.json()
        return data["data"]["market_price_usd"]
    except Exception as e:
        print("Error fetching BTC price:", e)
        return None

# Function to send the message to Telegram channel
def send_telegram_message(text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHANNEL_CHAT_ID,
            "text": text
        }

        response = requests.post(url, json=payload)
        print("Telegram response:", response.text)  # Log the Telegram response for debugging
    except Exception as e:
        print("Error sending Telegram message:", e)

# Main loop to send BTC price every 1 minute
while True:
    price = get_btc_price()

    if price:
        message = f"🚀 BTC Price: ${price}"
        send_telegram_message(message)
        print("Sent:", message)
    else:
        print("Skipping send due to error.")

    time.sleep(60)  # Wait for 1 minute before sending again

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

# Function to get the current Ethereum price using CoinGecko's API
def get_eth_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        response = requests.get(url, timeout=10)
        data = response.json()
        return data["ethereum"]["usd"]
    except Exception as e:
        print("Error fetching ETH price:", e)
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

# Main loop to send BTC and ETH prices every 5 minutes
while True:
    # Fetch Bitcoin and Ethereum prices
    btc_price = get_btc_price()
    eth_price = get_eth_price()

    if btc_price and eth_price:
        message = f"🚀 BTC Price: ${btc_price}\n💎 ETH Price: ${eth_price}"
        send_telegram_message(message)
        print("Sent:", message)
    else:
        print("Skipping send due to error.")

    time.sleep(300)  # Wait for 5 minutes before sending again (300 seconds)

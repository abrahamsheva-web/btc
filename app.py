import os
import time
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_CHAT_ID = os.getenv("CHANNEL_CHAT_ID")


def get_btc_price():
    try:
        url = "https://api.blockchair.com/bitcoin/stats"
        response = requests.get(url, timeout=10)
        data = response.json()
        return data["data"]["market_price_usd"]
    except Exception as e:
        print("Error fetching BTC price:", e)
        return None
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_CHAT_ID,
        "text": text
    }

    response = requests.post(url, json=payload)
    print("Telegram response:", response.text)

while True:
    price = get_btc_price()

    if price:
        message = f"🚀 BTC Price: ${price}"
        send_telegram_message(message)
        print("Sent:", message)
    else:
        print("Skipping send due to error.")

    time.sleep(60)

        "text": text
    }

    response = requests.post(url, json=payload)
    print("Telegram response:", response.text)

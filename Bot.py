import requests
import os
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/')
def home():
    return "Bot Running ✅"

@app.route('/send')
def send_signal():
    message = (
        "📈 Signal Alert: LONG\n"
        "🪙 Coin: BTCUSDT\n"
        "🎯 Entry: 66800\n"
        "💰 Targets: 67200 | 67500 | 68000\n"
        "🛑 Stoploss: 66300\n"
        "#Binance #Futures #CryptoSignal"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=data)
    return "Signal Sent ✅"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
  

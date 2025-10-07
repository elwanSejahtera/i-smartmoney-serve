from flask import Flask, request
import requests
import os
from smc_detector import analyze_smc   # 🔗 import modul analisa AI

app = Flask(__name__)

# 🔐 Ambil token dari environment Render
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ZAI_API_KEY = os.getenv("ZAI_API_KEY")

@app.route('/')
def home():
    return "✅ MrWan AI SMC Server is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '').strip()

        if text == '/start':
            reply = (
                "👋 Halo! Saya *Mr.Wan Smart Money AI Bot* 💰\n\n"
                "Kirim data *OHLC* atau *pair + timeframe* untuk analisa otomatis.\n\n"
                "Contoh:\n"
                "`XAUUSD H1`\n"
                "`Open 2400, High 2420, Low 2390, Close 2410`\n\n"
                "Saya akan menganalisa memakai strategi *Smart Money Concepts* 🧠✨"
            )
        else:
            reply = "⏳ Sedang menganalisa dengan Chat.Z.Ai..."
            send_message(chat_id, reply)

            # 🔍 Panggil analisa AI
            ai_result = analyze_smc(text)

            reply = f"📊 *Analisa Smart Money Concepts*\n\n{ai_result}"

        send_message(chat_id, reply)

    return 'ok', 200


def send_message(chat_id, text):
    """Kirim pesan balik ke user via Telegram"""
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}
    requests.post(url, json=payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

from flask import Flask, request
import requests
import os

app = Flask(__name__)

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
        text = data['message'].get('text', '')

        if text == '/start':
            reply = "👋 Halo! Saya Asisten *Smart Money AI* 💰✨\nKirim data XAU/USD atau timeframe untuk analisa."
        else:
            reply = f"📊 Kamu kirim: {text}"

        send_message(chat_id, reply)
    return 'ok', 200

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

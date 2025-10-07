from flask import Flask, request, jsonify
import smc_detector
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "✅ MrWan AI SMC Server is running!"

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return "📡 Webhook endpoint aktif!"

    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({"error": "No data received"}), 400

        message = data.get('message', {}).get('text', '')
        chat_id = data.get('message', {}).get('chat', {}).get('id')

        if not message or not chat_id:
            return jsonify({"status": "no message"}), 200

        # Analisis OHLC
        prediction = smc_detector.analyze_smc(message)

        # Kirim balasan ke Telegram
        import requests
        TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
        send_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": chat_id, "text": prediction}
        requests.post(send_url, json=payload)

        return jsonify({"status": "ok"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

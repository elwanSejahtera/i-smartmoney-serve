from flask import Flask, request, jsonify
import smc_detector
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ MrWan AI SMC Server is running!"

# ✅ pastikan ini namanya "/"
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400
    
    message = data.get('message', {}).get('text', '')
    if message:
        prediction = smc_detector.analyze_smc(message)
        return jsonify({"reply": prediction})
    
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

def analyze_smc(message):
    try:
        prices = [float(x) for x in message.replace(',', ' ').split()]
        if len(prices) < 4:
            return "Masukkan format: Open, High, Low, Close"
        
        o, h, l, c = prices[:4]
        bias = "Bullish" if c > o else "Bearish"
        strength = round(abs(c - o) / (h - l + 1e-6) * 100, 2)
        
        return f"📊 Smart Money Bias: {bias}\n🔥 Kekuatan: {strength}%"
    except:
        return "Format tidak dikenali. Gunakan: 1923.5,1930.2,1918.4,1925.7"

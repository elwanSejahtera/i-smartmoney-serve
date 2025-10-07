import os
import requests

ZAI_API_KEY = os.getenv("ZAI_API_KEY")

def analyze_smc(text):
    """
    Mengirim teks ke API Chat.Z.Ai untuk analisa Smart Money Concepts
    """
    url = "https://api.z.ai/api/paas/v4/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept-Language": "en-US,en",
        "Authorization": f"Bearer {ZAI_API_KEY}"
    }

    payload = {
        "model": "glm-4.6",
        "messages": [
            {"role": "system", "content": "You are an AI trained to analyze Smart Money Concepts and institutional flow in Forex markets."},
            {"role": "user", "content": text}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        # Ambil hasil analisa dari respons
        result = data["choices"][0]["message"]["content"]
        return result
    except Exception as e:
        return f"❌ Gagal memproses analisa: {e}"

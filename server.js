// ===============================
// AI Smart Money Server v1.0 🚀
// ===============================

import express from "express";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

// 🧠 Root route (cek server)
app.get("/", (req, res) => {
  res.send("✅ AI Smart Money Server aktif 🚀");
});

// 🧩 Route test
app.get("/test", (req, res) => {
  res.json({ message: "✅ /test endpoint aktif & siap digunakan" });
});

// 🔮 Route analisa utama
app.post("/analyze", (req, res) => {
  const { open, high, low, close, pair, timeframe } = req.body;

  if (!open || !high || !low || !close) {
    return res.status(400).json({ error: "Data OHLC tidak lengkap" });
  }

  const trend =
    close > open
      ? "Bullish (Smart Money Buy Pressure)"
      : "Bearish (Smart Money Sell Pressure)";

  const strength = Math.abs(close - open) / (high - low);
  const bias =
    strength > 0.7
      ? "Strong Institutional Activity"
      : "Normal Retail Flow";

  const result = {
    pair,
    timeframe,
    trend,
    strength: strength.toFixed(2),
    bias,
    message: `AI mendeteksi pola ${trend} dengan bias ${bias}`,
  };

  res.json(result);
});

// ⚡ Jalankan server
const PORT = process.env.PORT || 10000;
app.listen(PORT, () => console.log(`🚀 Server berjalan di port ${PORT}`));

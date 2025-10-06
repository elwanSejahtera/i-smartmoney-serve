
import express from "express";
import axios from "axios";
import cors from "cors";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Endpoint utama analisa AI
app.post("/analyze", async (req, res) => {
  try {
    const { pair = "XAU/USD", ohlc = [] } = req.body;

    const prompt = `
Analisa Smart Money Concepts untuk ${pair} berdasarkan data harga berikut:
${JSON.stringify(ohlc)}

Berikan:
1. Arah tren utama (bullish/bearish)
2. Order Block penting
3. Potensi Liquidity Sweep
4. Bias Smart Money
5. Rekomendasi posisi entry
`;

    const response = await openai.responses.create({
      model: "gpt-5-mini",
      input: prompt,
    });

    res.json({
      status: "success",
      analysis: response.output_text,
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Endpoint test koneksi
app.get("/", (req, res) => {
  res.send("AI Smart Money Server aktif 🚀");
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

import express from "express";
const app = express();
app.get("/", (req, res) => res.send("✅ n8n Server Ready!"));
app.listen(process.env.PORT || 3000);

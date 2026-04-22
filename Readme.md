# 🎙️ KothaAI — Bangla Voice Chat AI

End-to-end Bangla voice assistant: **Speech → Text → AI → Voice**
---
## [Live Demo](https://bangla-voice-chat-ai.onrender.com/)
---

## 🏗️ Architecture

```
User Voice → [Whisper ASR] → [Llama 3.1 8B] → [Bangla VITS TTS] → Audio Response
```

**Frontend:** Django + Django Channels (WebSocket)  
**Backend AI:** FastAPI on Kaggle (GPU) + Ngrok tunnel

---

## 🤖 Models

| Role | Model |
|------|-------|
| 🎙️ STT (Speech-to-Text) | [whisper-bengali-final-1.3](https://huggingface.co/kazol196295/whisper-bengali-final-1.3) |
| 🧠 LLM | meta-llama/Meta-Llama-3.1-8B-Instruct |
| 🔊 TTS (Text-to-Speech) | [bangla-vits-female-1.2](https://huggingface.co/kazol196295/bangla-vits-female-1.2) |

---

## 🚀 Quick Start

### 1. Run the Backend (Kaggle)

1. Open the notebook on Kaggle
2. Add secrets: `HF_TOKEN` and `NGROK_TOKEN` in **Add-ons → Secrets**
3. Run all cells — you'll get a public Ngrok URL

### 2. Run the Frontend (Local / Render)

```bash
pip install -r requirements.txt
python manage.py runserver
```

Open `http://localhost:8000` → paste your Ngrok URL in ⚙️ Settings

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/transcribe` | Audio file → Bangla text |
| POST | `/api/chat` | Text + history → AI response |
| POST | `/api/synthesize` | Text → WAV audio (base64) |

Swagger docs available at: `{ngrok-url}/docs`

---

## 📁 Project Structure

```
bangla_voice_chat/       # Django project config
voice_chat/
  consumers.py           # WebSocket handler
  services/api_clients.py # Kaggle API client
  views.py
templates/voice_chat/
  index.html             # Chat UI
backend-bangla-voice-ai-api.ipynb  # Kaggle backend
```

---

## 👤 Author

**Kawsar Ahmed Kazol** — [GitHub](https://github.com/kazol196295)

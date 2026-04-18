import base64
import requests
import logging

logger = logging.getLogger(__name__)



# Use standard HTML anchor tag instead of Markdown
CONNECTION_ERROR_MSG = 'কানেকশন ব্যর্থ হয়েছে! দয়া করে <a href="https://www.kaggle.com/code/kawsarahmedkazol/backend-bangla-voice-ai-api" target="_blank" style="color: #ffcccc; text-decoration: underline; font-weight: bold;">Kaggle backend</a> চেক করুন এবং নতুন Ngrok URL সাইডবারে পেস্ট করুন।'
# (Translation: Connection failed! Please check the Kaggle backend and paste the new Ngrok URL in the sidebar.)

class UnifiedAIClient:
    
    def transcribe(self, base_url: str, audio_data: bytes) -> str:
        try:
            url = base_url.rstrip('/')
            files = {
                "file": ("audio.wav", audio_data, "audio/wav")
            }
            response = requests.post(f"{url}/transcribe", files=files)
            response.raise_for_status()
            return response.json().get("transcription", "")
        except requests.exceptions.RequestException:
            # This triggers if Ngrok is down or the URL is wrong
            raise Exception(CONNECTION_ERROR_MSG)
        except Exception as e:
            logger.error(f"STT Error: {e}")
            return ""

    def chat(self, base_url: str, text: str, history: list = None) -> str:
        try:
            url = base_url.rstrip('/')
            payload = {"text": text, "history": history or []}
            response = requests.post(f"{url}/api/chat", json=payload)
            response.raise_for_status()
            return response.json().get("text", "")
        except requests.exceptions.RequestException:
            raise Exception(CONNECTION_ERROR_MSG)
        except Exception as e:
            logger.error(f"LLM Error: {e}")
            return "দুঃখিত, সার্ভারের সাথে সংযোগ করা যাচ্ছে না।"

    def synthesize(self, base_url: str, text: str) -> bytes:
        try:
            url = base_url.rstrip('/')
            payload = {"text": text}
            response = requests.post(f"{url}/api/synthesize", json=payload)
            response.raise_for_status()
            b64_audio = response.json().get("audio_base64", "")
            return base64.b64decode(b64_audio) if b64_audio else b""
        except requests.exceptions.RequestException:
            raise Exception(CONNECTION_ERROR_MSG)
        except Exception as e:
            logger.error(f"TTS Error: {e}")
            return b""

unified_ai_client = UnifiedAIClient()
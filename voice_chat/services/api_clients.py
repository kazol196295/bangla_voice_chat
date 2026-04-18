# import base64
# import requests
# from django.conf import settings
# import logging

# logger = logging.getLogger(__name__)


# class UnifiedAIClient:
#     def __init__(self):
#         self.base_url = settings.KAGGLE_API_URL

#     def transcribe(self, audio_data: bytes) -> str:
#         try:
#             payload = {"audio_base64": base64.b64encode(audio_data).decode("utf-8")}
#             response = requests.post(f"{self.base_url}/api/transcribe", json=payload)
#             response.raise_for_status()
#             return response.json().get("text", "")
#         except Exception as e:
#             logger.error(f"STT Error: {e}")
#             return ""

#     def chat(self, text: str, history: list = None) -> str:
#         try:
#             payload = {"text": text, "history": history or []}
#             response = requests.post(f"{self.base_url}/api/chat", json=payload)
#             response.raise_for_status()
#             return response.json().get("text", "")
#         except Exception as e:
#             logger.error(f"LLM Error: {e}")
#             return "দুঃখিত, সার্ভারের সাথে সংযোগ করা যাচ্ছে না।"

#     def synthesize(self, text: str) -> bytes:
#         try:
#             payload = {"text": text}
#             response = requests.post(f"{self.base_url}/api/synthesize", json=payload)
#             response.raise_for_status()
#             b64_audio = response.json().get("audio_base64", "")
#             return base64.b64decode(b64_audio) if b64_audio else b""
#         except Exception as e:
#             logger.error(f"TTS Error: {e}")
#             return b""


# unified_ai_client = UnifiedAIClient()


import base64
import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class UnifiedAIClient:
    def __init__(self):
        # Make sure to update KAGGLE_API_URL in your settings.py with the new Ngrok link
        self.base_url = settings.KAGGLE_API_URL.rstrip("/")

    def transcribe(self, audio_data: bytes) -> str:
        try:
            # 1. Package the raw bytes into a file-like tuple for the multipart upload
            # Format: ("filename", data_bytes, "mime_type")
            files = {"file": ("audio.wav", audio_data, "audio/wav")}

            # 2. Send as multipart/form-data to the /transcribe endpoint
            response = requests.post(f"{self.base_url}/transcribe", files=files)
            response.raise_for_status()

            # 3. Extract the 'transcription' key from your new Kaggle response
            return response.json().get("transcription", "")
        except Exception as e:
            logger.error(f"STT Error: {e}")
            return ""

    def chat(self, text: str, history: list = None) -> str:
        try:
            payload = {"text": text, "history": history or []}
            response = requests.post(f"{self.base_url}/api/chat", json=payload)
            response.raise_for_status()
            return response.json().get("text", "")
        except Exception as e:
            logger.error(f"LLM Error: {e}")
            return "দুঃখিত, সার্ভারের সাথে সংযোগ করা যাচ্ছে না।"

    def synthesize(self, text: str) -> bytes:
        try:
            payload = {"text": text}
            response = requests.post(f"{self.base_url}/api/synthesize", json=payload)
            response.raise_for_status()
            b64_audio = response.json().get("audio_base64", "")
            return base64.b64decode(b64_audio) if b64_audio else b""
        except Exception as e:
            logger.error(f"TTS Error: {e}")
            return b""


unified_ai_client = UnifiedAIClient()

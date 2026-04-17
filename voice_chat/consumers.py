import json
import base64
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

logger = logging.getLogger(__name__)


class VoiceChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history = []

    async def connect(self):
        await self.accept()
        await self.send(json.dumps({"type": "status", "message": "সংযুক্ত"}))

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if data.get("type") == "audio":
            await self.handle_pipeline(base64.b64decode(data["audio"]), is_audio=True)
        elif data.get("type") == "text":
            await self.handle_pipeline(data["text"], is_audio=False)

    async def handle_pipeline(self, input_data, is_audio):
        try:
            # 1. STT Phase
            if is_audio:
                await self.send(json.dumps({"type": "status", "message": "শুনছি..."}))
                text = await self.run_api("transcribe", input_data)
                if not text:
                    await self.send(
                        json.dumps({"type": "status", "message": "কথা বুঝতে পারিনি"})
                    )
                    return
                await self.send(json.dumps({"type": "transcription", "text": text}))
            else:
                text = input_data

            # 2. LLM Phase
            await self.send(json.dumps({"type": "status", "message": "ভাবছি..."}))
            response = await self.run_api("chat", text, self.history)
            await self.send(json.dumps({"type": "response", "text": response}))

            # 3. TTS Phase
            await self.send(json.dumps({"type": "status", "message": "বলছি..."}))
            audio_bytes = await self.run_api("synthesize", response)

            if audio_bytes:
                await self.send(
                    json.dumps(
                        {
                            "type": "audio_response",
                            "audio": base64.b64encode(audio_bytes).decode("utf-8"),
                            "is_last": True,
                        }
                    )
                )

            await self.send(json.dumps({"type": "status", "stage": "complete"}))

            # Keep context short
            self.history.append({"role": "user", "content": text})
            self.history.append({"role": "assistant", "content": response})
            if len(self.history) > 6:
                self.history = self.history[-6:]

        except Exception as e:
            await self.send(
                json.dumps({"type": "error", "message": f"সার্ভার ত্রুটি: {str(e)}"})
            )

    @database_sync_to_async
    def run_api(self, action, *args):
        from .services.api_clients import unified_ai_client

        if action == "transcribe":
            return unified_ai_client.transcribe(*args)
        if action == "chat":
            return unified_ai_client.chat(*args)
        if action == "synthesize":
            return unified_ai_client.synthesize(*args)

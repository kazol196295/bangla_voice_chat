"""
ASGI config for bangla_voice_chat project.
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import voice_chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bangla_voice_chat.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(voice_chat.routing.websocket_urlpatterns)
        ),
    }
)

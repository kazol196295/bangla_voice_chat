"""
ASGI config for bangla_voice_chat project.
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator  # <-- ADDED THIS

import voice_chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bangla_voice_chat.settings")

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before setting up the WebSocket router.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(  # <-- WRAPPED THE SOCKET IN THE VALIDATOR
            AuthMiddlewareStack(URLRouter(voice_chat.routing.websocket_urlpatterns))
        ),
    }
)

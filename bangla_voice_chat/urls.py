"""
URL configuration for bangla_voice_chat project.
"""

from django.contrib import admin
from django.urls import path, include
from voice_chat.views import voice_chat_view, health_check

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", voice_chat_view, name="voice_chat"),
    path("health/", health_check, name="health_check"),
]

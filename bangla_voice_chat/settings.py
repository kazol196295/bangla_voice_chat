"""
Django settings for bangla_voice_chat project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-your-secret-key-change-this-in-production"

# ==========================================
# SMART ENVIRONMENT SETTINGS
# ==========================================
# Automatically turns off DEBUG when deployed to Render
DEBUG = "RENDER" not in os.environ

# Allows your local PC and Render to host the app
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".onrender.com"]
CSRF_TRUSTED_ORIGINS = ["https://*.onrender.com"]
# Application definition
INSTALLED_APPS = [
    "daphne",  # Must be at the top for Channels
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "channels",
    "voice_chat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bangla_voice_chat.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bangla_voice_chat.wsgi.application"
ASGI_APPLICATION = "bangla_voice_chat.asgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Channels Configuration
CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==========================================
# SMART KAGGLE API CONNECTION
# ==========================================
# It will look for the Render Environment Variable first.
# If you are testing locally, it falls back to your current Ngrok link.
KAGGLE_API_URL = os.environ.get(
    "KAGGLE_API_URL", "https://peremptory-fourthly-argelia.ngrok-free.dev"
)

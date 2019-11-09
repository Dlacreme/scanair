from django.conf import settings
from os import environ
from django.urls import path
from telegram_bot import views

urlpatterns = [
    path(environ.get('TELEGRAM_BOT_KEY', None), views.webhook, name='webhook'),
]

if settings.DEBUG:
    print(f'Listening on http://127.0.0.1:8000/{environ.get("TELEGRAM_BOT_KEY", None)}')

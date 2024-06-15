"""
the updates path
"""
from app.bot.presentation import handler

from app.bot.settings.internal.conf.port import SERVICE_NAME


path = {
    "path": f"/{SERVICE_NAME}/v1/bot/webhook/",
    "endpoint": handler.webhook.updates_hander,
    "methods": [
        "POST"
    ]
}

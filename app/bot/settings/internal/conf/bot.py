"""
the entry point model
"""
from app.bot.settings.external.environs import env

IS_WEBHOOK_ENABLED = env.bool("IS_WEBHOOK_ENABLED", False)
NOTIFICATION_ID = env.int("NOTIFICATION_ID")

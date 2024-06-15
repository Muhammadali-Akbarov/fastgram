"""
init configuration module
"""
from app.bot.settings.external.environs import env


CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", "redis://redis:6379/1")
CELERY_RESULT_BACKEND = env.str("CELERY_RESULT_BACKEND", "redis://redis:6379/1")

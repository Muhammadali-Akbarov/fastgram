"""
the redis configuration
"""
from app.bot.settings.external.environs import env

REDIS_HOST = env.str("REDIS_HOST", default="localhost")
REDIS_PORT = env.int("REDIS_PORT", default=6379)
REDIS_DATABASE = env.str("REDIS_DATABASE", default=0)

"""
initialize redis client for caching
"""
import redis

from app.bot.settings.external.redis import REDIS_HOST

redis_client = redis.Redis(host=REDIS_HOST, port=6379, db=0)

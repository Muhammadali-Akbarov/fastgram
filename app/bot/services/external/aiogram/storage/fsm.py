"""
fsm storage module
"""
from redis.asyncio.client import Redis
from aiogram.fsm.storage.redis import RedisStorage

from app.bot.settings import REDIS_HOST, REDIS_PORT, REDIS_DATABASE


storage = RedisStorage(
    redis=Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DATABASE
    )
)

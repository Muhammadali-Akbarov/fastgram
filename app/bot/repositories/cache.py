"""
implementation of caching interface
"""
import typing

from app.bot.repositories.abstract import ICache


class Cache(ICache):
    """
    implementation of caching interface
    """
    def __init__(self, cache_client: ICache):
        self.cache_client = cache_client

    async def get(self, key: str) -> typing.Any:
        return self.cache_client.get(key)

    async def set(self, key: str, value: typing.Any, expire=60):
        return self.cache_client.set(key, value, expire)

    async def delete(self, key: str):
        return self.cache_client.delete(key)

"""
init repository layer
"""
from app.bot.models.client import Client
from app.bot.repositories import abstract
from app.bot.repositories.cache import Cache

from app.bot.services.external.redis import redis_client
from app.bot.services.external.alchemy.repository import AlchemyRepository


class Repository(abstract.IRepository):
    """
    repository layer implementation
    """
    def __init__(
        self,
        repo: abstract.IRepository,
        cache: abstract.ICache,
    ):
        self.repository = repo
        self.cache = cache

    async def create_or_update_client(self, client) -> None:
        return await self.repository.create_or_update_client(client=client)

    async def set_user_lang(self, client: Client, lang: str):
        return await self.repository.set_user_lang(
            client=client,
            lang=lang
        )

    async def get_user_lang(self, client: Client) -> str:
        return await self.repository.get_user_lang(
            client=client
        )


repository = Repository(
    repo=AlchemyRepository(),
    cache=Cache(cache_client=redis_client)
)

"""
implementation of controller interface
"""
import logging

from app.bot import models
from app.bot import repositories

from app.bot.controllers import IAppController


logger = logging.getLogger(__name__)


class AppController(IAppController):
    """
    implementation of controller interface
    """
    def __init__(
        self,
        repository: repositories.IRepository,
    ):
        self.repository = repository

    async def create_or_update_client(
        self,
        client: models.Client
    ) -> models.Client:
        try:
            await self.repository.create_or_update_client(client)

        # pylint: disable=W0718
        except Exception as exc:
            logger.error("create_or_update_client - %s", exc)
            return

    async def set_user_lang(
        self,
        client: models.Client,
        lang: str
    ) -> None:
        try:
            await self.repository.set_user_lang(
                client=client,
                lang=lang
            )
        # pylint: disable=W0718
        except Exception as exc:
            logger.error("set_user_lang - %s", exc)
            return

    async def get_user_lang(self, client: models.Client) -> str:
        return await self.repository.get_user_lang(
            client=client
        )

    async def set_user_info(self, user_id, chat_id, phone, lat, long):
        return await self.repository.set_user_info(
            user_id=user_id,
            chat_id=chat_id,
            phone=phone,
            lat=lat,
            long=long
        )

    async def swich_state(self, chat_id, state):
        return await self.repository.swich_state(chat_id, state)


controller = AppController(
    repository=repositories.repository
)

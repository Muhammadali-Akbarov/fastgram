"""
application controller abstraction
"""
import abc

from app.bot import models


class IAppController(abc.ABC):
    """
    application controller abstraction
    """
    @abc.abstractmethod
    async def create_or_update_client(
        self,
        client: models.Client
    ) -> models.Client:
        """
        create or update client interface
        """
        raise NotADirectoryError("create_or_update_client not implemented")

    @abc.abstractmethod
    async def set_user_lang(
        self,
        client: models.Client,
        lang: str
    ) -> None:
        """
        set user language interface
        """
        raise NotImplementedError("set_user_lang not implemented")

    @abc.abstractmethod
    async def get_user_lang(
        self,
        client: models.Client
    ) -> str:
        """
        get user language interface
        """
        raise NotImplementedError("set_user_lang not implemented")

    @abc.abstractmethod
    async def swich_state(self, chat_id, state):
        """
        set swich_state interface
        """
        raise NotImplementedError("register_to_system not implemented")

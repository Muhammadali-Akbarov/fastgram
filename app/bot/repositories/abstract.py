"""
init repository abstraction
"""
import abc

import typing
from app.bot import models


class IRepository(abc.ABC):
    """
    repository abstraction
    """
    @abc.abstractmethod
    async def create_or_update_client(
        self,
        client: models.Client,
    ) -> None:
        """
        create or update user
        """
        raise NotImplementedError("create_or_update_user not implemented!")

    @abc.abstractmethod
    async def set_user_lang(
        self,
        client: models.Client,
        lang: str
    ):
        """
        set user language
        """
        raise NotImplementedError("set_user_lang not implemented!")

    @abc.abstractmethod
    async def get_user_lang(
        self,
        client: models.Client
    ) -> str:
        """
        get user language from user database
        """
        raise NotImplementedError("get_user_lang not implemented!")


class ICache(abc.ABC):
    """"
    thats used for caching interfaces
    """
    @abc.abstractmethod
    async def get(self, key: str) -> typing.Any:
        """
        the get data from cache
        """
        raise NotImplementedError("notimplemented yet!")

    @abc.abstractmethod
    async def set(self, key: str, value: typing.Any, expire=60):
        """
        the data setter for cache
        """
        raise NotImplementedError("notimplemented yet!")

    @abc.abstractmethod
    async def delete(self, key: str):
        """
        the data deleter for cache
        """
        raise NotImplementedError("notimplemented yet!")

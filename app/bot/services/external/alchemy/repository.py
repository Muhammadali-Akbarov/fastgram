"""
the alchemy repository
"""
from app.bot.repositories import abstract
from app.bot.services.external.alchemy import models


class AlchemyRepository(abstract.IRepository):
    """
    the alchemy repository
    """
    async def create_or_update_client(self, client):
        await models.create_or_update_client(client)

    async def set_user_lang(self, client, lang):
        await models.set_user_lang(client, lang)

    async def get_user_lang(self, client: models.Client):
        return await models.get_user_lang(client)

    async def swich_state(self, chat_id, state):
        return await models.swich_state(chat_id, state)

    async def set_user_verify_code(self, chat_id, code):
        raise NotImplementedError("set_user_verify_code does not support")

    async def check_user_verify_code(self, chat_id, code):
        raise NotImplementedError("check_user_verify_code does not support")

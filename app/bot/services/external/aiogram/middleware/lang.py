"""
language middlewares
"""
from aiogram.types import Message

from app.bot.models import Client
from app.bot.controllers import controller
from app.bot.services.external.aiogram.shortcut.action import send_action


LANGUAGES = {
    "🇺🇿 O'zbek tili": "uz",
    "🇷🇺 Русский язык": "ru",
}


async def language_middleware(handler, event: Message, data):
    """
    Middleware for language selection
    """
    text = event.text
    user = event.from_user

    await send_action(event)

    client = Client(
        chat_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name
    )

    if text in LANGUAGES:
        lang_code = LANGUAGES[text]
        await controller.set_user_lang(client=client, lang=lang_code)

    data["lang"] = await controller.get_user_lang(client=client)
    return await handler(event, data)

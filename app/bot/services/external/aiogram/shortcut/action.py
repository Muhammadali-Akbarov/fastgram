"""
init actions utils
"""
from aiogram.types import Message


async def send_action(event: Message):
    """
    send action shortcut
    """
    chat_id = event.chat.id
    await event.bot.send_chat_action(
        chat_id=chat_id,
        action="typing"
    )

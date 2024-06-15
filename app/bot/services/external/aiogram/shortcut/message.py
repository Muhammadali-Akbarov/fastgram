"""
init message shortcuts
"""
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest


async def delete_message(message: Message):
    """
    delete message shortcut
    """
    try:
        await message.bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id
        )
    except TelegramBadRequest:
        return

"""
init aiogram
"""
from aiogram.types import Message

from app.bot.services.external.aiogram import dispatcher as dp


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    await message.send_copy(chat_id=message.chat.id)

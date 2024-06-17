"""
init aiogram
"""
from aiogram.types import Message


async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    await message.send_copy(chat_id=message.chat.id)

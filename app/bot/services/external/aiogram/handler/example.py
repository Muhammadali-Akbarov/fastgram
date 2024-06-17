"""
init aiogram
"""
from aiogram.types import Message


async def example_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    chat_id = message.chat.id
    await message.bot.send_message(chat_id, "It's example message")

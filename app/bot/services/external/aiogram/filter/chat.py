"""
the chat type filter implementation
"""

import typing

from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    """
    chat type filter class responsible for filtering messages
    """
    def __init__(self, chat_type: str | typing.Sequence[str]):
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type

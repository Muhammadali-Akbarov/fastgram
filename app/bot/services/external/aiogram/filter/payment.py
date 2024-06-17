"""
the payment filter implementation
"""
from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message


class SuccessfullyPayment(BaseFilter):
    """
    successfully payment filter implementation
    """
    async def __call__(self, obj: Message | CallbackQuery) -> bool:
        if isinstance(obj, Message):
            return bool(obj.successful_payment)

        return False

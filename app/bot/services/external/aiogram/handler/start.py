"""
init aiogram
"""
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.bot.services.external.aiogram.keyboard import markup


btns: list[str] = ["🇺🇿 O'zbek tili", "🇷🇺 Русский язык"]
buttons = markup.genmarkup(btns=btns, schema=[2])


async def start_handler(message: Message, state: FSMContext, lang) -> None:
    """
    handler will forward receive a message back to the sender
    """
    user = message.from_user
    await message.answer(
        text=f"Hello {user.first_name}",
        reply_markup=buttons
    )
    await state.update_data(lang=lang)

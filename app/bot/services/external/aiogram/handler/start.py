"""
init aiogram
"""
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.bot.services.external.aiogram.button import markup
from app.bot.services.external.aiogram import dispatcher as dp


btns: list[str] = ["🇺🇿 O'zbek tili", "🇷🇺 Русский язык"]
buttons = markup.genmarkup(btns=btns, schema=[2])


@dp.message(
    (F.text == "/start") |
    (F.text == "🌐 Выбрать язык")
)
async def start(message: Message, state: FSMContext, lang) -> None:
    """
    handler will forward receive a message back to the sender
    """
    user = message.from_user
    await message.answer(
        text=f"Hello {user.first_name}",
        reply_markup=buttons
    )
    await state.update_data(lang=lang)

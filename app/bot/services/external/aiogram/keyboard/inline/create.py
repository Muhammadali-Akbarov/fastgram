"""
inline button creator
"""
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.services.external.aiogram.keyboard.inline.default import constructor # noqa


def genmarkup(keyboard_data: dict):
    """
    inline button creator

    use case:
        keyboard_data = [
            ("Button 1", "button1_callback"),
            ("Button 2", "button2_callback"),
            ("Button 3", "button3_callback"),
        ]
        markup = inline.genmarkup(keyboard_data=keyboard_data)
    """
    builder = InlineKeyboardBuilder()
    for i in keyboard_data:
        button = InlineKeyboardButton(
            text=i[0],
            callback_data=i[1]
        )
        builder.add(button)

    return builder.as_markup()


def generate_inline(actions: list[dict], schema):
    """
    generate inline keyboard buttons

    constructor.create_kb(
        actions=[
            {
                "text": "Button 1",
                "callback_data": "button1_callback",
            },
            {
                "text": "Button 2",
                "callback_data": "button2_callback",
            },
            {
                "text": "Button 3",
                "callback_data": "button3_callback",
            },
        ],
        schema=[1, 1, 1]
    )
    """
    return constructor.create_kb(
        actions=actions,
        schema=schema
    )

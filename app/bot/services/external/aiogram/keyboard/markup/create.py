"""
create markup utility function
"""
from app.bot.services.external.aiogram.keyboard.markup.default import constructor # noqa


def genmarkup(btns: list[str], schema):
    """
    markup keyboard generator function
    """
    return constructor.create_kb(btns, schema)

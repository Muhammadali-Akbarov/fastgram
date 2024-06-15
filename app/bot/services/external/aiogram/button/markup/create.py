"""
create markup utility function
"""
from app.bot.services.external.aiogram.button.markup.default import constructor # noqa


def genmarkup(btns: list[str], schema):
    """
    markup keyboard generator function
    """
    return constructor.create_kb(btns, schema)

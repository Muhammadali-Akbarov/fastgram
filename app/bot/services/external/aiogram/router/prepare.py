"""
init router
"""
from aiogram import Router
from aiogram.filters import CommandStart

from app.bot.services.external.aiogram import handler
from app.bot.services.external.aiogram import filter as custom_filter


def prepare_router() -> Router:
    """
    prepare routing
    """
    user_router = Router()
    user_router.message.filter(custom_filter.ChatTypeFilter("private"))
    user_router.message.register(handler.start_handler, CommandStart())
    user_router.message.register(handler.echo_handler)

    return user_router

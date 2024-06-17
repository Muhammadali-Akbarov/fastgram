"""
init router
"""
from aiogram import Router
from aiogram.filters import CommandStart

from app.bot.services.external.aiogram import handler
from app.bot.services.external.aiogram import filter as custom_filter


start_handler_filters = CommandStart()
example_handler_filters = custom_filter.TextFilter(["example", "sample"])


def prepare_router() -> Router:
    """
    prepare routing
    """
    user_router = Router()
    user_router.message.filter(custom_filter.ChatTypeFilter("private"))
    user_router.message.register(handler.start_handler, start_handler_filters)
    user_router.message.register(handler.example_handler, example_handler_filters)
    user_router.message.register(handler.echo_handler)

    return user_router

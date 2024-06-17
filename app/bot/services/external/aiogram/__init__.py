"""
start handler
"""
import aiogram

from app.bot.settings.external.aiogram import conf
from app.bot.services.external.aiogram import router
from app.bot.services.external.aiogram import middleware
from app.bot.services.external.aiogram.storage import storage


bot = aiogram.Bot(**conf.bot)
dispatcher = aiogram.Dispatcher(storage=storage)
dispatcher.include_router(router.prepare_router())
dispatcher.message.middleware(middleware=middleware.language)

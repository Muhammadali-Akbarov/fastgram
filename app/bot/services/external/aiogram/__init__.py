"""
start handler
"""
import aiogram

from app.bot.settings.external.aiogram import conf
from app.bot.services.external.aiogram import middleware
from app.bot.services.external.aiogram.storage import storage


bot = aiogram.Bot(**conf.bot)
dispatcher = aiogram.Dispatcher(storage=storage)
dispatcher.message.middleware(middleware=middleware.language)

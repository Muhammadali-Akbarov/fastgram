"""
the webhook handler for getting bot updates
"""
from app.bot.services.external.aiogram import bot
from app.bot.services.external.aiogram import aiogram
from app.bot.services.external.aiogram import dispatcher as dp


async def updates_hander(request: dict):
    """
    the update handler for getting bot updates
    """
    update = aiogram.types.Update.model_validate(request)

    await dp.feed_update(
        bot=bot,
        update=update
    )

    return {
        "succeeded": request,
    }

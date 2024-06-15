"""
entry point of the application where
FastAPI app is created and routes are defined.
"""
import sys
import logging

import fastapi

from app.bot.presentation import router
from app.bot.settings.internal.conf import port
from app.bot.services.external.aiogram import bot
from app.bot.services.external.alchemy import models
from app.bot.services.external.aiogram import handler
from app.bot.services.external.alchemy import engine
from app.bot.settings.internal.conf.bot import NOTIFICATION_ID
from app.bot.settings.internal.conf.bot import IS_WEBHOOK_ENABLED


app = fastapi.FastAPI()


async def main() -> None:
    """
    entrypoint of running bot operations
    """
    # run migrations
    if IS_WEBHOOK_ENABLED is False:
        await bot.delete_webhook(drop_pending_updates=True)
        await handler.dp.start_polling(bot)


@app.on_event("startup")
async def startup_event():
    """
    startup events.
    """
    # run migrations
    models.Base.metadata.create_all(bind=engine)
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    if IS_WEBHOOK_ENABLED:
        current_webhook = await bot.get_webhook_info()
        service_webhook = f"{port.SERVICE_ADDRESS}/{port.SERVICE_NAME}/v1/bot/webhook/" # noqa

        if current_webhook.url != service_webhook:
            await bot.delete_webhook()
            await bot.set_webhook(
                url=service_webhook,
                drop_pending_updates=True
            )
            await bot.send_message(
                chat_id=NOTIFICATION_ID,
                text=f"✅ Webhook URL has been reset to - {service_webhook}"
            )
            await bot.send_message(
                chat_id=NOTIFICATION_ID,
                text="✅ Bot has been started with webhook mode"
            )
            return

    if IS_WEBHOOK_ENABLED is False:
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.send_message(
            chat_id=NOTIFICATION_ID,
            text="✅ Bot has been started with polling mode"
        )
        await handler.dp.start_polling(bot)


@app.on_event("shutdown")
async def on_shutdown():
    """
    shutdown events.
    """
    await bot.send_message(
        chat_id=NOTIFICATION_ID,
        text="🔥️️️️️️ Bot has been down"
    )
    await bot.session.close()


app.add_api_route(**router.updates_route)

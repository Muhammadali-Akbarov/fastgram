"""
init configuration module
"""
from app.bot.settings.external.environs import env

bot = {
    "token": env.str("BOT_TOKEN"),
}

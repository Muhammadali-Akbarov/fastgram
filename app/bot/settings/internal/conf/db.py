"""
init database configuration
"""
from app.bot.settings.external.environs import env


DB_ENGINE = env.str("DB_ENGINE")
DB_NAME = env.str("DB_NAME")
DB_USERNAME = env.str("DB_USERNAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_HOST = env.str("DB_HOST")
DB_PORT = env.str("DB_PORT")


DB_URL = f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" # noqa

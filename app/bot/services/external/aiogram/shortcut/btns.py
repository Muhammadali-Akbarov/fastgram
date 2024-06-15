"""
init buttons shortcuts
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


ASK_CONTACT = {
    "uz": "📲 Kontaktni yuborish",
    "ru": "📲 Отправить контакт",
    "en": "📲 Send contact",
}

ASK_LOCATION = {
    "uz": "📌 Lokatsiya yuborish",
    "ru": "📌 Отправить местоположение",
    "en": "📌 Send location",
}

MENU_TEXT = {
    "uz": "Menu",
    "ru": "Меню",
    "en": "Menu",
}

CHANNEL = {
    "uz": "Kanal",
    "ru": "Канал",
    "en": "Channel",
}


async def get_ask_contact(lang):
    """
    getting ask contact button for given language
    """
    text = ASK_CONTACT[lang]

    keyboard = [
        [KeyboardButton(text=text, request_contact=True)],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    return keyboard


async def get_ask_location(lang):
    """
    getting ask location button for given language
    """
    text = ASK_LOCATION[lang]

    keyboard = [
        [KeyboardButton(text=text, request_location=True)],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    return keyboard


async def get_open_web_app(lang, chat_id):
    """
    getting open web app button for given language
    """
    url = f"https://master-kebab-webapp-bot.vercel.app/?chat_id={chat_id}"
    btn = KeyboardButton(
        text=MENU_TEXT[lang],
        web_app=WebAppInfo(url=url)
    )

    keyboard = [[btn],]

    keyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    return keyboard

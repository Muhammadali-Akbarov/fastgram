"""
default constructor
"""
from typing import Sequence, TypeVar, Dict

from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButtonPollType


T = TypeVar("T")


class DefaultConstructor:
    """
    default constructor.
    """
    aliases = {
        "contact": "request_contact",
        "location": "request_location",
        "poll": "request_poll",
    }
    available_properities = [
        "text",
        "request_contact",
        "request_location",
        "request_poll",
        "request_user",
        "request_chat",
        "web_app",
    ]
    properties_amount = 1

    def create_kb(
        self,
        actions: Sequence[str | Dict[str, str | bool | KeyboardButtonPollType]], # noqa
        schema: Sequence[int],
        resize_keyboard: bool = True,
        selective: bool = False,
        one_time_keyboard: bool = False,
        is_persistent: bool = True,
    ) -> ReplyKeyboardMarkup:
        """
        button creator
        """
        btns: list[KeyboardButton] = []

        for a in actions:
            if isinstance(a, str):
                a = {"text": a}
            data: Dict[str, str | bool | KeyboardButtonPollType] = {}

            for k, v in DefaultConstructor.aliases.items():
                if k in a:
                    a[v] = a[k]
                    del a[k]
            for k in a:
                if k in DefaultConstructor.available_properities:
                    if len(data) < DefaultConstructor.properties_amount:
                        data[k] = a[k]
                    else:
                        break
            if len(data) != DefaultConstructor.properties_amount:
                raise ValueError("Недостаточно данных для создания кнопки")

            # pylint: disable=E1125
            btns.append(KeyboardButton(**data))

        kb = ReplyKeyboardMarkup(
            resize_keyboard=resize_keyboard,
            selective=selective,
            one_time_keyboard=one_time_keyboard,
            is_persistent=is_persistent,
            keyboard=self.create_keyboard_layout(btns, schema),
        )
        return kb

    def create_keyboard_layout(
        self,
        buttons: Sequence[T],
        count: Sequence[int]
    ) -> list[list[T]]:
        """
        create markup buttons
        """
        if sum(count) != len(buttons):
            raise ValueError("Количество кнопок не совпадает со схемой")
        tmplist: list[list[T]] = []
        btn_number = 0

        for a in count:
            tmplist.append([])
            for _ in range(a):
                tmplist[-1].append(buttons[btn_number])
                btn_number += 1

        return tmplist


constructor = DefaultConstructor()

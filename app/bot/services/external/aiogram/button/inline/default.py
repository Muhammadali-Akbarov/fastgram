"""
default constructor for inline keyboard
"""
from typing import Sequence, TypeVar, Type

from aiogram.types import LoginUrl
from aiogram.types import CallbackGame
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

T = TypeVar("T")
A = TypeVar("A", bound=Type[CallbackData])


class InlineConstructor:
    """
    inline constructor
    """
    aliases = {"cb": "callback_data"}
    available_properities = [
        "text",
        "callback_data",
        "url",
        "login_url",
        "switch_inline_query",
        "switch_inline_query_current_chat",
        "callback_game",
        "pay",
    ]
    properties_amount = 2

    def create_kb(
        self,
        actions: list[
            dict[
                str,
                str | bool | A | LoginUrl | CallbackGame,
            ]
        ],
        schema: list[int],
    ) -> InlineKeyboardMarkup:
        """
        generate inline buttons
        """
        btns: list[InlineKeyboardButton] = []

        for a in actions:
            data: dict[
                str,
                str | bool | A | LoginUrl | CallbackGame,
            ] = {}
            for k, v in InlineConstructor.aliases.items():
                if k in a:
                    a[v] = a[k]
                    del a[k]
            for k in a:
                if k in InlineConstructor.available_properities:
                    if len(data) < InlineConstructor.properties_amount:
                        data[k] = a[k]
                    else:
                        break

            if "callback_data" in data:
                if isinstance(data["callback_data"], CallbackData):
                    data["callback_data"] = data["callback_data"].pack()
            if "pay" in data:
                if len(btns) != 0 and data["pay"]:
                    raise ValueError("Платежная кнопка должна идти первой в клавиатуре") # noqa

                data["pay"] = a["pay"]

            if len(data) != InlineConstructor.properties_amount:
                raise ValueError("Недостаточно данных для создания кнопки")

            # pylint: disable=E1125
            btns.append(InlineKeyboardButton(**data))
        kb = InlineKeyboardMarkup(
            inline_keyboard=self.create_keyboard_layout(btns, schema)
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


constructor = InlineConstructor()

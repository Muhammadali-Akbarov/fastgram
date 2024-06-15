"""
process state
"""
from aiogram.fsm.state import State, StatesGroup


class IntroState(StatesGroup):
    """
    the message editor state class
    """
    get_contact = State()
    get_verify_code = State()
    get_location = State()

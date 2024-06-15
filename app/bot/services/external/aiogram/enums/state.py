"""
the enumeration of delivery
"""
from enum import Enum


class StateEnum(str, Enum):
    """
    The enumeration of telegram user state.
    """
    ON_START = "on_start"
    NOT_STARTED = "not_started"
    GET_CONTACT = "get_contact"
    GET_LOCATION = "get_location"
    ON_VERIFICATION = "on_verification"
    REJECTED = "rejected"
    ON_MENU = "on_menu"

    def __str__(self):
        return str(self.value)

    @classmethod
    def choices(cls):
        """
        Returns a list of tuples containing the enum values and their labels.
        """
        return [(member.value, member.value.replace('_', ' ').capitalize()) for member in cls] # noqa

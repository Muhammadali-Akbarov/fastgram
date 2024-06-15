"""
schema shortcuts
"""


def get_schema(num_buttons):
    """
    get the schema of the items
    """
    if num_buttons == 1:
        return [1]

    if num_buttons == 2:
        return [1, 1]

    if num_buttons > 2:
        num_rows = (num_buttons - 1) // 2 + 1
        return [2] * (num_rows - 1) + [num_buttons % 2 or 2]

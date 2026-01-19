from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class TextRole:
    """
    Defines visual roles for all texts in the app.
    These are independent of themes.
    """

    TITLE = {
        "size": 24,
        "weight": QFont.Bold,
        "family": "Inter",
        "alignment": Qt.AlignCenter,
        "padding": "8px 16px"
    }

    PLAYER_NAME = {
        "size": 18,
        "weight": QFont.Medium,
        "family": "Inter",
        "alignment": Qt.AlignCenter,
        "padding": "4px 8px"
    }

    LABEL = {
        "size": 14,
        "weight": QFont.Normal,
        "family": "Inter",
        "alignment": Qt.AlignLeft,
        "padding": "2px 6px"
    }

    SMALL = {
        "size": 12,
        "weight": QFont.Normal,
        "family": "Inter",
        "alignment": Qt.AlignLeft,
        "padding": "2px 4px"
    }


    
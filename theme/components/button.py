from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Property, QPropertyAnimation
from theme.tokens import Tokens


class AppButton(QPushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.setMinimumHeight(32)
        self._hover_opacity = 0.0

        self.anim = QPropertyAnimation(self, b"hoverOpacity")
        self.anim.setDuration(Tokens.ANIMATION_FAST)

    def enterEvent(self, event):
        self.anim.setEndValue(1.0)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.anim.setEndValue(0.0)
        self.anim.start()
        super().leaveEvent(event)

    def get_opacity(self):
        return self._hover_opacity

    def set_opacity(self, value):
        self._hover_opacity = value
        self.update()

    hoverOpacity = Property(float, get_opacity, set_opacity)

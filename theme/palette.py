from PySide6.QtGui import QPalette, QColor


def create_palette(colors) -> QPalette:
    p = QPalette()

    p.setColor(QPalette.Window, QColor(colors.BACKGROUND))
    p.setColor(QPalette.WindowText, QColor(colors.TEXT_PRIMARY))
    p.setColor(QPalette.Base, QColor(colors.SURFACE))
    p.setColor(QPalette.Text, QColor(colors.TEXT_PRIMARY))
    p.setColor(QPalette.Button, QColor(colors.SURFACE))
    p.setColor(QPalette.ButtonText, QColor(colors.TEXT_PRIMARY))
    p.setColor(QPalette.Highlight, QColor(colors.PRIMARY))

    return p

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from pathlib import Path

from theme.palette import create_palette
from theme.colors_dark import DarkColors
from theme.colors_light import LightColors
from theme.desing.button import ButtonSizes
from theme.desing.text import TextRole
from theme.state import ThemeState

MODE = ["dark", "light"]
STYLE = ["modern", "classic"]


def apply_theme(app: QApplication, mode="dark", style="modern"):
    """Apply theme to the application.
    
    Args:
        app (QApplication): The application instance
        mode (str): Theme mode ('dark' or 'light')
        style (str): Theme style ('modern' or 'classic')
        
    Raises:
        ValueError: If mode or style is not valid
    """
    # Check mode
    if mode not in MODE:
        raise ValueError("Mode must be {MODE}")
    colors = DarkColors if mode == "dark" else LightColors

    app.setStyle("Fusion")
    app.setPalette(create_palette(colors))
    # Check style
    if style not in STYLE:
        raise ValueError("Style must be {STYLE}")
    qss = Path(__file__).parent / "qss" / f"{style}.qss"
    app.setStyleSheet("")
    app.setStyleSheet(qss.read_text())


def setup_theme(ui):
    """Set up the theme for the UI.
    
    Args:
        ui: UI object to apply theme to
    """
    # Setup roles
    _setup_roles(ui=ui)
    # Setup theme actions
    _setup_theme_actions(ui=ui)
    # Apply button sizes
    _apply_button_sizes(ui=ui)
    # Apply text design
    _apply_text_desing(ui=ui)


def _setup_roles(ui):
    """Set up role properties for UI elements.
    
    Args:
        ui: UI object
    """
    # Local team buttons
    ui.add_local.setProperty("role", "local")
    ui.subtract_local.setProperty("role", "local")

    # Visitor team buttons
    ui.add_visitor.setProperty("role", "visitor")
    ui.subtrac_visitor.setProperty("role", "visitor")

    # Set button
    ui.next_set.setProperty("role", "set")
    ui.previous_set.setProperty("role", "set")

    # Reset button
    ui.reset.setProperty("role", "danger")


def _setup_theme_actions(ui):
    """Connect theme action signals.
    
    Args:
        ui: UI object
    """
    ui.actionDark.triggered.connect(
        lambda: _set_mode("dark")
    )
    ui.actionLight.triggered.connect(
        lambda: _set_mode("light")
    )
    ui.actionModern.triggered.connect(
        lambda: _set_style("modern")
    )
    ui.actionClassic.triggered.connect(
        lambda: _set_style("classic")
    )


def _set_mode(mode):
    """Change the theme mode.
    
    Args:
        mode (str): Theme mode ('dark' or 'light')
    """
    ThemeState.mode = mode
    apply_theme(QApplication.instance(), ThemeState.mode, ThemeState.style)


def _set_style(style):
    """Change the theme style.
    
    Args:
        style (str): Theme style ('modern' or 'classic')
    """
    ThemeState.style = style
    apply_theme(QApplication.instance(), ThemeState.mode, ThemeState.style)


def _apply_button_sizes(ui):
    """Apply sizes to UI buttons.
    
    Args:
        ui: UI object
    """
    _apply(ui.add_local, ButtonSizes.LOCAL)
    _apply(ui.subtract_local, ButtonSizes.LOCAL)

    _apply(ui.add_visitor, ButtonSizes.VISITOR)
    _apply(ui.subtrac_visitor, ButtonSizes.VISITOR)

    _apply(ui.next_set, ButtonSizes.SET)
    _apply(ui.previous_set, ButtonSizes.SET)
    _apply(ui.reset, ButtonSizes.RESET)

    apply_theme(QApplication.instance(), ThemeState.mode, ThemeState.style)


def _apply_text_desing(ui):
    """Apply text design to UI labels.
    
    Args:
        ui: UI object
    """
    apply_text_role(ui.local_label, TextRole.TITLE)
    apply_text_role(ui.visitor_label, TextRole.TITLE)
    apply_text_role(ui.set_label, TextRole.TITLE)

    apply_text_role(ui.local_points_label, TextRole.SMALL)
    apply_text_role(ui.visitor_points_label, TextRole.SMALL)
    apply_text_role(ui.set_number_label, TextRole.SMALL)


def _apply(button, config):
    """Apply size and font configuration to a button.
    
    Args:
        button: QPushButton to configure
        config (dict): Configuration dictionary with 'width', 'height', 'font' keys
    """
    button.setFixedSize(config["width"], config["height"])
    font = button.font()
    font.setPointSize(config["font"])
    button.setFont(font)


def apply_text_role(label, role):
    """Apply text role configuration to a label.
    
    Args:
        label: QLabel to configure
        role (dict): Role configuration dictionary
    """
    font = QFont(role["family"])
    font.setPointSize(role["size"])
    font.setWeight(role["weight"])
    label.setFont(font)
    label.setAlignment(role["alignment"])
    label.setStyleSheet(f"padding: {role['padding']};")
    label.setSizePolicy(
        label.sizePolicy().horizontalPolicy(),
        label.sizePolicy().verticalPolicy()
    )

    label.adjustSize()
    label.setMinimumHeight(label.sizeHint().height())

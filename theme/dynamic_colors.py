from PySide6.QtWidgets import QApplication
from theme.state import ThemeState


def apply_dynamic_colors(ui):
    """Apply dynamic colors to UI elements.
    
    Args:
        ui: UI object with button references
    """
    _apply_button_colors(ui)


def _apply_button_colors(ui):
    """Apply dynamic colors to buttons based on their role.
    
    Args:
        ui: UI object with button references
    """
    # Local team buttons
    _set_button_color(ui.add_local, ThemeState.local_color)
    _set_button_color(ui.subtract_local, ThemeState.local_color)
    
    # Visitor team buttons
    _set_button_color(ui.add_visitor, ThemeState.visitor_color)
    _set_button_color(ui.subtrac_visitor, ThemeState.visitor_color)
    
    # Set button
    _set_button_color(ui.next_set, ThemeState.set_color)
    
    # Reset button
    _set_button_color(ui.reset, ThemeState.reset_color)


def _set_button_color(button, color):
    """Apply color to a specific button.
    
    Args:
        button: QPushButton to apply color to
        color (str): Hex color code
    """
    button.setStyleSheet(f"""
        QPushButton {{
            background-color: {color};
        }}
        QPushButton:hover {{
            background-color: {_lighten_color(color, 20)};
        }}
        QPushButton:pressed {{
            background-color: {_darken_color(color, 20)};
        }}
    """)


def _lighten_color(hex_color, amount):
    """Lighten a hex color.
    
    Args:
        hex_color (str): Hex color code
        amount (int): Amount to lighten (0-100)
        
    Returns:
        str: Lightened hex color code
    """
    from PySide6.QtGui import QColor
    color = QColor(hex_color)
    color = color.lighter(100 + amount)
    return color.name()


def _darken_color(hex_color, amount):
    """Darken a hex color.
    
    Args:
        hex_color (str): Hex color code
        amount (int): Amount to darken (0-100)
        
    Returns:
        str: Darkened hex color code
    """
    from PySide6.QtGui import QColor
    color = QColor(hex_color)
    color = color.darker(100 + amount)
    return color.name()


def update_colors_from_dialog(ui, colors_dict, file_writer=None):
    """Update colors from dialog and apply changes.
    
    Args:
        ui: UI object to update
        colors_dict (dict): Dictionary with 'local' and 'visitor' colors
        file_writer: FileWriter instance to persist colors (optional)
    """
    ThemeState.local_color = colors_dict["local"]
    ThemeState.visitor_color = colors_dict["visitor"]
    apply_dynamic_colors(ui)
    
    # Update the JSON state file if FileWriter is provided
    if file_writer:
        file_writer.set_local_color(ThemeState.local_color)
        file_writer.set_visitor_color(ThemeState.visitor_color)

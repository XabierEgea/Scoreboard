from PySide6.QtWidgets import QDialog, QColorDialog
from PySide6.QtGui import QColor
from theme.state import ThemeState
from theme.language_manager import language_manager

from gui_files.color_selector_wrapper import Ui_ColorSelectorWrapper


class ColorPickerDialog(QDialog):
    """Dialog for selecting team colors (local and visitor)."""
    
    def __init__(self, parent=None):
        """Initialize the color picker dialog.
        
        Args:
            parent: Parent widget
        """
        super(ColorPickerDialog, self).__init__(parent)
        self.ui = Ui_ColorSelectorWrapper()
        self.ui.setupUi(self)
                
        # Local color button - connect to color picker
        self._update_button_color(self.ui.local_color_button, ThemeState.local_color)
        self.ui.local_color_button.clicked.connect(self._pick_local_color)
        
        # Visitor color button - connect to color picker
        self._update_button_color(self.ui.visitor_color_button, ThemeState.visitor_color)
        self.ui.visitor_color_button.clicked.connect(self._pick_visitor_color)

        # Connect Apply and Cancel buttons to dialog (not to UI)
        self.ui.apply_button.clicked.connect(self.accept)
        self.ui.cancel_button.clicked.connect(self.reject)
            
    def _update_button_color(self, button, color_hex):
        """Update button background color.
        
        Args:
            button: QPushButton to update
            color_hex (str): Hex color code
        """
        button.setStyleSheet(f"background-color: {color_hex}; border: 1px solid #333;")
    
    def _pick_local_color(self):
        """Open color picker dialog to select local team color."""
        dialog_title = language_manager.get("color_picker.select_local", "Select Local Color")
        color = QColorDialog.getColor(QColor(ThemeState.local_color), self, dialog_title)
        if color.isValid():
            ThemeState.local_color = color.name()
            self._update_button_color(self.ui.local_color_button, ThemeState.local_color)
    
    def _pick_visitor_color(self):
        """Open color picker dialog to select visitor team color."""
        dialog_title = language_manager.get("color_picker.select_visitor", "Select Visitor Color")
        color = QColorDialog.getColor(QColor(ThemeState.visitor_color), self, dialog_title)
        if color.isValid():
            ThemeState.visitor_color = color.name()
            self._update_button_color(self.ui.visitor_color_button, ThemeState.visitor_color)
    
    def get_colors(self):
        """Return the selected colors.
        
        Returns:
            dict: Dictionary with 'local' and 'visitor' color codes
        """
        return {
            "local": ThemeState.local_color,
            "visitor": ThemeState.visitor_color
        }

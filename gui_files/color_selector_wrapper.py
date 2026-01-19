"""
Wrapper for Ui_Dialog (color selector) that applies translations.
This file is NOT overwritten by Qt Designer.
"""

from gui_files.ui_color_selector import Ui_Dialog
from theme.language_manager import language_manager


class Ui_ColorSelectorWrapper(Ui_Dialog):
    """Extends Ui_Dialog with dynamic translation support."""
    
    def setupUi(self, Dialog):
        """Set up the UI and apply translations.
        
        Args:
            Dialog: The dialog widget
        """
        super().setupUi(Dialog)
        self._apply_translations(Dialog)
    
    def retranslateUi(self, Dialog):
        """Override retranslateUi to apply translations from the language manager.
        
        Args:
            Dialog: The dialog widget
        """
        self._apply_translations(Dialog)
    
    def _apply_translations(self, Dialog):
        """Apply all translations to dialog elements.
        
        Args:
            Dialog: The dialog widget
        """
        Dialog.setWindowTitle(language_manager.get("color_picker.title", "Configure Colors"))
        self.local_label.setText(language_manager.get("color_picker.local_color", "Local Color:"))
        self.visitor_label.setText(language_manager.get("color_picker.visitor_color", "Visitor Color:"))
        self.apply_button.setText(language_manager.get("color_picker.apply", "Apply"))
        self.cancel_button.setText(language_manager.get("color_picker.cancel", "Cancel"))

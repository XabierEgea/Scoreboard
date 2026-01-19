"""
Wrapper for Ui_MainWindow that applies translations and custom logic.
This file is NOT overwritten by Qt Designer.
"""

from gui_files.ui_scoreboard import Ui_MainWindow
from theme.language_manager import language_manager


class Ui_ScoreboardWrapper(Ui_MainWindow):
    """Extends Ui_MainWindow with dynamic translation support."""
    
    def setupUi(self, MainWindow):
        """Set up the UI and apply translations.
        
        Args:
            MainWindow: The main window widget
        """
        super().setupUi(MainWindow)
        self._apply_translations(MainWindow)
    
    def retranslateUi(self, MainWindow):
        """Override retranslateUi to apply translations from the language manager.
        
        Args:
            MainWindow: The main window widget
        """
        self._apply_translations(MainWindow)
    
    def _apply_translations(self, MainWindow):
        """Apply all translations to UI elements.
        
        Args:
            MainWindow: The main window widget
        """
        MainWindow.setWindowTitle("Scoreboard")
        self.actionDark.setText(language_manager.get("menu.dark", "Dark"))
        self.actionLight.setText(language_manager.get("menu.light", "Light"))
        self.actionModern.setText(language_manager.get("menu.modern", "Modern"))
        self.actionClassic.setText(language_manager.get("menu.classic", "Classic"))
        self.actionColors.setText(language_manager.get("menu.colors", "Colors"))
        
        self.local_label.setText(language_manager.get("scoreboard.local", "LOCAL"))
        self.add_local.setText(language_manager.get("scoreboard.add", "+1"))
        self.subtract_local.setText(language_manager.get("scoreboard.subtract", "-1"))
        
        self.set_label.setText(language_manager.get("scoreboard.set", "SET"))
        self.next_set.setText(language_manager.get("scoreboard.next_set", "NEXT SET"))
        
        self.visitor_label.setText(language_manager.get("scoreboard.visitor", "VISITOR"))
        self.add_visitor.setText(language_manager.get("scoreboard.add", "+1"))
        self.subtrac_visitor.setText(language_manager.get("scoreboard.subtract", "-1"))
        
        self.reset.setText(language_manager.get("scoreboard.reset", "RESET"))
        
        self.menuOptions.setTitle(language_manager.get("menu.options", "Options"))
        self.menuMode.setTitle(language_manager.get("menu.mode", "Mode"))
        self.menuStyle.setTitle(language_manager.get("menu.style", "Style"))

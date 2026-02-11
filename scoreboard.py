from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog
from PySide6 import QtUiTools
from PySide6.QtGui import QFont
from pyparsing import Path

from theme.theme import apply_theme
from theme.state import ThemeState
from theme.theme import apply_theme, setup_theme
from theme.dynamic_colors import apply_dynamic_colors, update_colors_from_dialog
from theme.language_manager import language_manager
from filewriter import FileWriter
from gui_files.scoreboard_wrapper import Ui_ScoreboardWrapper
from secondary_windows.color_picker_dialog import ColorPickerDialog



class GUIScoreBoard(QMainWindow):
    """Main scoreboard window that manages the game interface and logic."""
    
    def __init__(self, root_path):
        """Initialize the scoreboard window with UI setup and event connections.
        
        Args:
            root_path (str): Root path for file operations
        """
        super(GUIScoreBoard, self).__init__()
        # Load UI file
        self.ui = Ui_ScoreboardWrapper()
        self.ui.setupUi(self)
        self._local_points = 0
        self._visiting_points = 0
        self._set = 1
        self._max_points_per_set = 15
        self._max_sets = 3
        self.scoreboard = FileWriter(root_path)
        self._theme_state = ThemeState()

        self.ui.add_local.clicked.connect(self.add_local_point)
        self.ui.add_visitor.clicked.connect(self.visitor_points)
        self.ui.subtract_local.clicked.connect(self.subtract_local_points)
        self.ui.subtrac_visitor.clicked.connect(self.subtract_visiting_points)
        self.ui.next_set.clicked.connect(self.pass_next_set)
        self.ui.previous_set.clicked.connect(self.previous_set)
        self.ui.actionColors.triggered.connect(self.open_color_picker)
        self.ui.local_team_name_input.textChanged.connect(
            lambda text: self.scoreboard.set_local_name(text)
        )
        self.ui.visitor_team_name_input.textChanged.connect(
            lambda text: self.scoreboard.set_visitor_name(text)
        )
        self.ui.reset.clicked.connect(self.reset_scores)

        self.ui.local_points_label.setText(f'{self._local_points}')
        self.scoreboard.set_local_value(set_number=self._set, points=self._local_points)
        self.ui.visitor_points_label.setText(f'{self._visiting_points}')
        self.scoreboard.set_visiting_value(set_number=self._set, points=self._visiting_points)
        self.ui.set_number_label.setText(f'{self._set}')

        # Setup theme
        setup_theme(self.ui)
        # Apply dynamic colors
        apply_dynamic_colors(self.ui)

        self.scoreboard.reset_scores(values="all")
       
    # ==============================================================================
    # Scoreboard Logic Methods
    # ==============================================================================

    def add_local_point(self):
        """Increment local team points by 1 if under max points per set."""
        if self._local_points >= self._max_points_per_set:
            return
        self._local_points += 1
        self.scoreboard.set_local_value(set_number=self._set, points=self._local_points)
        self.ui.local_points_label.setText(f'{self._local_points}')

    def visitor_points(self):
        """Increment visitor team points by 1 if under max points per set."""
        if self._visiting_points >= self._max_points_per_set:
            return
        self._visiting_points += 1
        self.scoreboard.set_visiting_value(set_number=self._set, points=self._visiting_points)
        self.ui.visitor_points_label.setText(f'{self._visiting_points}')

    def subtract_local_points(self):
        """Decrement local team points by 1 if not negative."""
        if self._local_points <= 0:
            return
        self._local_points -= 1
        self.scoreboard.set_local_value(set_number=self._set, points=self._local_points)
        self.ui.local_points_label.setText(f'{self._local_points}')

    def subtract_visiting_points(self):
        """Decrement visitor team points by 1 if not negative."""
        if self._visiting_points <= 0:
            return
        self._visiting_points -= 1
        self.scoreboard.set_visiting_value(set_number=self._set, points=self._visiting_points)
        self.ui.visitor_points_label.setText(f'{self._visiting_points}')

    def pass_next_set(self):
        """Reset scores and advance to the next set."""
        # self._local_points = 0
        # self._visiting_points = 0
        self._set += 1

        self.scoreboard.change_set(self._set)
        self._local_points = self.scoreboard.get_local_set_score(self._set)
        self._visiting_points = self.scoreboard.get_visitor_set_score(self._set)
        # self.scoreboard.set_local_value(set_number=self._set, points=self._local_points)
        # self.scoreboard.set_visiting_value(set_number=self._set, points=self._visiting_points)
        self.ui.local_points_label.setText(f'{self._local_points}')
        self.ui.visitor_points_label.setText(f'{self._visiting_points}')
        self.ui.set_number_label.setText(f'{self._set}')

    def previous_set(self):
        """Go back to the previous set if not the first set."""
        if self._set <= 1:
            return
        self._set -= 1

        self.scoreboard.change_set(self._set)
        self._local_points = self.scoreboard.get_local_set_score(self._set)
        self._visiting_points = self.scoreboard.get_visitor_set_score(self._set)
        self.ui.local_points_label.setText(f'{self._local_points}')
        self.ui.visitor_points_label.setText(f'{self._visiting_points}')
        self.ui.set_number_label.setText(f'{self._set}')

    def set_local_points(self, points: int) -> None:
        """Set local team points with validation.
        
        Args:
            points (int): Points to set (0 to max_points_per_set)
        """
        if points < 0:
            points = 0
        elif points > self._max_points_per_set:
            points = self._max_points_per_set
        
        self._local_points = points
        self.scoreboard.set_local_value(set_number=self._set, points=points)
        self.ui.local_points_label.setText(f'{self._local_points}')

    def set_visitor_points(self, points: int) -> None:
        """Set visitor team points with validation.
        
        Args:
            points (int): Points to set (0 to max_points_per_set)
        """
        if points < 0:
            points = 0
        elif points > self._max_points_per_set:
            points = self._max_points_per_set
        
        self._visiting_points = points
        self.scoreboard.set_visiting_value(set_number=self._set, points=points)
        self.ui.visitor_points_label.setText(f'{self._visiting_points}')

    def set_set_number(self, set_num: int) -> None:
        """Set the current set number with validation.
        
        Args:
            set_num (int): Set number to set (1 to max_sets)
        """
        if set_num < 1:
            set_num = 1
        elif set_num > self._max_sets:
            set_num = self._max_sets
        
        self._set = set_num
        self.scoreboard.change_set(self._set)
        self.ui.set_number_label.setText(f'{self._set}')
    
    # ==============================================================================
    # Color Picker Methods
    # ==============================================================================

    def open_color_picker(self):
        """Open the color picker dialog to select team colors."""
        dialog = ColorPickerDialog(self)
        if dialog.exec() == QDialog.Accepted:
            colors = dialog.get_colors()
            # Pass FileWriter instance to persist colors to JSON
            update_colors_from_dialog(self.ui, colors, self.scoreboard)
    
    def set_language(self, language_code: str):
        """Change the application language and update the UI.
        
        Args:
            language_code (str): Language code (e.g., 'es', 'en')
        """
        if language_manager.set_language(language_code):
            # Retranslate UI elements
            self.ui.retranslateUi(self)

    def reset_scores(self):
        """Reset scores for both teams and all sets."""
        self._local_points = 0
        self._visiting_points = 0
        self._set = 1
        self.scoreboard.reset_scores(values="scores")
        self.ui.local_points_label.setText(f'{self._local_points}')
        self.ui.visitor_points_label.setText(f'{self._visiting_points}')
        self.ui.set_number_label.setText(f'{self._set}')
    

if __name__ == '__main__':
    import sys

    root_path = Path(__file__).resolve().parent
    app = QApplication(sys.argv)
    apply_theme(app, mode="dark", style="classic")
    
    window = GUIScoreBoard(root_path / "overlay")
    window.show()
    app.exec_()

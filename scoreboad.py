from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog
from PySide6 import QtUiTools
from PySide6.QtGui import QFont
from qt_material import apply_stylesheet

from filewriter import FileWriter
from gui_files.scoreboard import Ui_MainWindow


class GUIScoreBoard(QMainWindow, Ui_MainWindow):
    def __init__(self, root_path):
        super(GUIScoreBoard, self).__init__()
        # Load Ui file
        self.setupUi(self)
        self._local_points = 0
        self._visiting_points = 0
        self._set = 1
        self.scoreboard = FileWriter(root_path)

        # Conect Ui elements to this class
        self.add_local = self.findChild(QtWidgets.QPushButton, 'add_local')
        self.add_visitante = self.findChild(QtWidgets.QPushButton, 'add_visitante')
        self.subtract_local = self.findChild(QtWidgets.QPushButton, 'subtract_local')
        self.subtrac_visitante = self.findChild(QtWidgets.QPushButton, 'subtrac_visitante')
        self.next_set = self.findChild(QtWidgets.QPushButton, 'next_set')
        self.local_text = self.findChild(QtWidgets.QLineEdit, 'Local_points')
        self.visiting_text = self.findChild(QtWidgets.QLineEdit, 'Visiting_points')
        self.set_text = self.findChild(QtWidgets.QLineEdit, 'Set')

        self.add_local.clicked.connect(self.add_local_point)
        self.add_visitante.clicked.connect(self.add_visiting_point)
        self.subtract_local.clicked.connect(self.subtract_local_point)
        self.subtrac_visitante.clicked.connect(self.subtract_visiting_point)
        self.next_set.clicked.connect(self.pass_next_set)

        self.local_text.setText(f'{self._local_points}')
        self.scoreboard.set_local_value(self._local_points)
        self.visiting_text.setText(f'{self._visiting_points}')
        self.scoreboard.set_visiting_value(self._visiting_points)
        self.set_text.setText(f'{self._set}')

    def add_local_point(self):
        self._local_points += 1
        self.scoreboard.set_local_value(self._local_points)
        self.scoreboard.set_visiting_value(self._visiting_points)
        self.local_text.setText(f'{self._local_points}')

    def add_visiting_point(self):
        self._visiting_points += 1
        self.scoreboard.set_visiting_value(self._visiting_points)
        self.visiting_text.setText(f'{self._visiting_points}')

    def subtract_local_point(self):
        self._local_points -= 1
        self.scoreboard.set_local_value(self._local_points)
        self.local_text.setText(f'{self._local_points}')

    def subtract_visiting_point(self):
        self._visiting_points -= 1
        self.scoreboard.set_visiting_value(self._visiting_points)
        self.visiting_text.setText(f'{self._visiting_points}')

    def pass_next_set(self):
        self._local_points = 0
        self._visiting_points = 0
        self._set += 1

        self.scoreboard.change_set(self._set)
        self.scoreboard.set_local_value(self._local_points)
        self.scoreboard.set_visiting_value(self._visiting_points)
        self.local_text.setText(f'{self._local_points}')
        self.visiting_text.setText(f'{self._visiting_points}')
        self.set_text.setText(f'{self._set}')


if __name__ == '__main__':
    import sys

    root_path = '/home/xabier/Scoreboard'
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    apply_stylesheet(app, theme='dark_teal.xml', extra={'primaryColor': '#ffffff'})
    app.setFont(QFont('Robot', 10))
    app.setStyleSheet(app.styleSheet() + """
    QLineEdit {
            color: white; /*set text color*/
    }
    """
    )
    window = GUIScoreBoard(root_path)
    window.show()
    app.exec_()

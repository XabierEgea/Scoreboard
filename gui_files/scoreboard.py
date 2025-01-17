# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Scoreboard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.add_local = QPushButton(self.centralwidget)
        self.add_local.setObjectName(u"add_local")
        self.add_local.setGeometry(QRect(90, 150, 191, 91))
        self.add_local.setStyleSheet(u"background-color:red")
        self.add_visitante = QPushButton(self.centralwidget)
        self.add_visitante.setObjectName(u"add_visitante")
        self.add_visitante.setGeometry(QRect(530, 150, 191, 91))
        self.add_visitante.setStyleSheet(u"background-color:blue\n"
"")
        self.subtract_local = QPushButton(self.centralwidget)
        self.subtract_local.setObjectName(u"subtract_local")
        self.subtract_local.setGeometry(QRect(90, 310, 191, 91))
        self.subtract_local.setStyleSheet(u"background-color:red")
        self.subtrac_visitante = QPushButton(self.centralwidget)
        self.subtrac_visitante.setObjectName(u"subtrac_visitante")
        self.subtrac_visitante.setGeometry(QRect(530, 310, 191, 91))
        self.subtrac_visitante.setStyleSheet(u"background-color:blue\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 100, 181, 51))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(570, 100, 181, 61))
        self.label_2.setFont(font)
        self.Local_points = QLineEdit(self.centralwidget)
        self.Local_points.setObjectName(u"Local_points")
        self.Local_points.setGeometry(QRect(130, 260, 113, 25))
        self.Visiting_points = QLineEdit(self.centralwidget)
        self.Visiting_points.setObjectName(u"Visiting_points")
        self.Visiting_points.setGeometry(QRect(570, 260, 113, 25))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 210, 81, 41))
        self.label_3.setFont(font)
        self.Set = QLineEdit(self.centralwidget)
        self.Set.setObjectName(u"Set")
        self.Set.setGeometry(QRect(340, 260, 113, 25))
        self.Restart = QPushButton(self.centralwidget)
        self.Restart.setObjectName(u"Restart")
        self.Restart.setGeometry(QRect(610, 540, 131, 31))
        self.Restart.setStyleSheet(u"background-color:red")
        self.next_set = QPushButton(self.centralwidget)
        self.next_set.setObjectName(u"next_set")
        self.next_set.setGeometry(QRect(300, 500, 181, 61))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.add_local.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ed333b;\">+1</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.add_local.setText(QCoreApplication.translate("MainWindow", u"+1", None))
#if QT_CONFIG(whatsthis)
        self.add_visitante.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ed333b;\">+1</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.add_visitante.setText(QCoreApplication.translate("MainWindow", u"+1", None))
#if QT_CONFIG(whatsthis)
        self.subtract_local.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ed333b;\">+1</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.subtract_local.setText(QCoreApplication.translate("MainWindow", u"-1", None))
#if QT_CONFIG(whatsthis)
        self.subtrac_visitante.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ed333b;\">+1</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.subtrac_visitante.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOCAL", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"VISITANTE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SET", None))
#if QT_CONFIG(whatsthis)
        self.Restart.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ed333b;\">+1</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Restart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.next_set.setText(QCoreApplication.translate("MainWindow", u"Siguiente set", None))
    # retranslateUi


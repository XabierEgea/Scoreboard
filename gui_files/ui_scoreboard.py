# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scoreboardanRakp.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(939, 552)
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionModern = QAction(MainWindow)
        self.actionModern.setObjectName(u"actionModern")
        self.actionClassic = QAction(MainWindow)
        self.actionClassic.setObjectName(u"actionClassic")
        self.actionColors = QAction(MainWindow)
        self.actionColors.setObjectName(u"actionColors")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.Local_layout = QVBoxLayout()
        self.Local_layout.setObjectName(u"Local_layout")
        self.local_label = QLabel(self.centralwidget)
        self.local_label.setObjectName(u"local_label")
        self.local_label.setMaximumSize(QSize(16777215, 30))

        self.Local_layout.addWidget(self.local_label)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.Local_layout.addItem(self.verticalSpacer)

        self.add_local = QPushButton(self.centralwidget)
        self.add_local.setObjectName(u"add_local")

        self.Local_layout.addWidget(self.add_local)

        self.local_points_label = QLineEdit(self.centralwidget)
        self.local_points_label.setObjectName(u"local_points_label")

        self.Local_layout.addWidget(self.local_points_label)

        self.subtract_local = QPushButton(self.centralwidget)
        self.subtract_local.setObjectName(u"subtract_local")

        self.Local_layout.addWidget(self.subtract_local)


        self.horizontalLayout_3.addLayout(self.Local_layout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.set_label = QLabel(self.centralwidget)
        self.set_label.setObjectName(u"set_label")
        self.set_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.set_label)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.set_number_label = QLineEdit(self.centralwidget)
        self.set_number_label.setObjectName(u"set_number_label")

        self.verticalLayout_2.addWidget(self.set_number_label)

        self.next_set = QPushButton(self.centralwidget)
        self.next_set.setObjectName(u"next_set")

        self.verticalLayout_2.addWidget(self.next_set)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.visitor_label = QLabel(self.centralwidget)
        self.visitor_label.setObjectName(u"visitor_label")
        self.visitor_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.visitor_label)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.add_visitor = QPushButton(self.centralwidget)
        self.add_visitor.setObjectName(u"add_visitor")

        self.verticalLayout.addWidget(self.add_visitor)

        self.visitor_points_label = QLineEdit(self.centralwidget)
        self.visitor_points_label.setObjectName(u"visitor_points_label")

        self.verticalLayout.addWidget(self.visitor_points_label)

        self.subtrac_visitor = QPushButton(self.centralwidget)
        self.subtrac_visitor.setObjectName(u"subtrac_visitor")

        self.verticalLayout.addWidget(self.subtrac_visitor)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.reset = QPushButton(self.centralwidget)
        self.reset.setObjectName(u"reset")

        self.horizontalLayout_2.addWidget(self.reset)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 939, 33))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuMode = QMenu(self.menuOptions)
        self.menuMode.setObjectName(u"menuMode")
        self.menuStyle = QMenu(self.menuOptions)
        self.menuStyle.setObjectName(u"menuStyle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.menuMode.menuAction())
        self.menuOptions.addAction(self.menuStyle.menuAction())
        self.menuOptions.addAction(self.actionColors)
        self.menuMode.addAction(self.actionDark)
        self.menuMode.addAction(self.actionLight)
        self.menuStyle.addAction(self.actionModern)
        self.menuStyle.addAction(self.actionClassic)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Scoreboard", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.actionModern.setText(QCoreApplication.translate("MainWindow", u"Modern", None))
        self.actionClassic.setText(QCoreApplication.translate("MainWindow", u"Classic", None))
        self.actionColors.setText(QCoreApplication.translate("MainWindow", u"Colors", None))
        self.local_label.setText(QCoreApplication.translate("MainWindow", u"LOCAL", None))
        self.add_local.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.subtract_local.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.set_label.setText(QCoreApplication.translate("MainWindow", u"SET", None))
        self.next_set.setText(QCoreApplication.translate("MainWindow", u"NEXT SET", None))
        self.visitor_label.setText(QCoreApplication.translate("MainWindow", u"VISITOR", None))
        self.add_visitor.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.subtrac_visitor.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.reset.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuMode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.menuStyle.setTitle(QCoreApplication.translate("MainWindow", u"Style", None))
    # retranslateUi


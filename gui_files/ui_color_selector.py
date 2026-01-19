# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_selectormrGNrE.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.local_layout = QHBoxLayout()
        self.local_layout.setObjectName(u"local_layout")
        self.local_label = QLabel(Dialog)
        self.local_label.setObjectName(u"local_label")

        self.local_layout.addWidget(self.local_label)

        self.local_color_button = QPushButton(Dialog)
        self.local_color_button.setObjectName(u"local_color_button")
        self.local_color_button.setMaximumSize(QSize(50, 50))
        self.local_color_button.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.local_layout.addWidget(self.local_color_button)


        self.verticalLayout.addLayout(self.local_layout)

        self.visitor_layout = QHBoxLayout()
        self.visitor_layout.setObjectName(u"visitor_layout")
        self.visitor_label = QLabel(Dialog)
        self.visitor_label.setObjectName(u"visitor_label")

        self.visitor_layout.addWidget(self.visitor_label)

        self.visitor_color_button = QPushButton(Dialog)
        self.visitor_color_button.setObjectName(u"visitor_color_button")
        self.visitor_color_button.setMaximumSize(QSize(50, 50))
        self.visitor_color_button.setStyleSheet(u"background-color: rgb(0, 85, 255);")

        self.visitor_layout.addWidget(self.visitor_color_button)


        self.verticalLayout.addLayout(self.visitor_layout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_layout.addItem(self.horizontalSpacer)

        self.apply_button = QPushButton(Dialog)
        self.apply_button.setObjectName(u"apply_button")

        self.buttons_layout.addWidget(self.apply_button)

        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.buttons_layout.addWidget(self.cancel_button)


        self.verticalLayout_2.addLayout(self.buttons_layout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.local_label.setText(QCoreApplication.translate("Dialog", u"Local Color:", None))
        self.local_color_button.setText("")
        self.visitor_label.setText(QCoreApplication.translate("Dialog", u"Visitor Color:", None))
        self.visitor_color_button.setText("")
        self.apply_button.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi


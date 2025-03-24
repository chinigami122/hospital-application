# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finaleXVlJEu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame
import res1_rc

class LoginPage(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 584)
        MainWindow.setStyleSheet("*{\n"
"  font-family: Roboto ;\n"
"  font-size:24px;\n"
"}\n"
"#MainWindow{\n"
"	background-image: url(:/img1/11_18_2021_A_waifu2x_photo_noise6_scale);\n"
"}\n"
"QFrame\n"
"{\n"
"  background:rgba(0,0,0,0.8);\n"
"  border-radius:15px;\n"
"}\n"
"QFrame#Frame_2{\n"
"    background: rgba(0, 0, 0, 0.9);\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"QToolButton{\n"
"background:blue;\n"
"border-radius:60px;\n"
"}\n"
"QPushButton{\n"
"color:white;\n"
"border-radius:15px;\n"
"background:#007BFF;\n"
"}\n"
"QPushButton:hover{\n"
"color:red;\n"
"border-radius:15px;\n"
"background:#0056b3;\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setMinimumSize(QSize(400, 500))
        self.frame.setMaximumSize(QSize(800, 400))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName("label_4")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(500, 100))
        self.frame_2.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.label.setMaximumSize(QSize(150, 50))

        self.verticalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFrame(True)

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setMaximumSize(QSize(400, 100))
        self.frame_3.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.label_2.setMaximumSize(QSize(150, 50))

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setReadOnly(False)

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setMinimumSize(QSize(300, 50))
        self.frame_4.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setMinimumSize(QSize(100, 20))
        self.frame_5.setMaximumSize(QSize(100, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{\n"
"color:white;\n"
"border-radius:15px;\n"
"background:#13568a;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"border-radius:15px;\n"
"background:#0d2f4a;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.label_3.setMaximumSize(QSize(220, 50))
        self.label_3.setStyleSheet("/* Base style for the \"Forget Password\" widget */\n"
"QWidget {\n"
"    color: #007BFF; /* Blue color for the text */\n"
"    text-decoration: underline; /* Underline to mimic a link */\n"
"    font-size: 12px; /* Adjust font size as needed */\n"
"    background-color: transparent; /* Transparent background */\n"
"    border: none; /* Remove border */\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QWidget:hover {\n"
"    color: #0056b3; /* Darker blue when hovered */\n"
"    cursor: pointer; /* Change cursor to pointer to indicate clickability */\n"
"}")

        self.horizontalLayout.addWidget(self.label_3, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Login here", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Username", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", "Username", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Password", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", "Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Forget password?", None))
    # retranslateUi

        from PyQt5 import QtWidgets
# from login_page import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, LoginPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sat Nov 01 11:19:22 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(623, 595)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/imagenes/calculator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("border-image: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 0, 551, 551))
        self.groupBox.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setStyleSheet(_fromUtf8("border-image:url(:/logo_header_jan.png)"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lblBienvenido = QtGui.QLabel(self.groupBox)
        self.lblBienvenido.setStyleSheet(_fromUtf8("font: 75 14pt \"MS Shell Dlg 2\";\n"
"font: 75 16pt \"MV Boli\";"))
        self.lblBienvenido.setObjectName(_fromUtf8("lblBienvenido"))
        self.verticalLayout.addWidget(self.lblBienvenido)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setStyleSheet(_fromUtf8("border-image:url(:/119499456854720557funct.svg.med.png)"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagenes/119499456854720557funct.svg.med.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pbSalir = QtGui.QPushButton(self.groupBox_2)
        self.pbSalir.setGeometry(QtCore.QRect(380, 20, 131, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/dialog-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSalir.setIcon(icon1)
        self.pbSalir.setObjectName(_fromUtf8("pbSalir"))
        self.pbConfig = QtGui.QPushButton(self.groupBox_2)
        self.pbConfig.setGeometry(QtCore.QRect(50, 20, 61, 61))
        self.pbConfig.setStyleSheet(_fromUtf8("border-image: url(:/system-software-update.png)"))
        self.pbConfig.setText(_fromUtf8(""))
        self.pbConfig.setObjectName(_fromUtf8("pbConfig"))
        self.pbIngresar = QtGui.QPushButton(self.groupBox_2)
        self.pbIngresar.setGeometry(QtCore.QRect(220, 20, 131, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbIngresar.setIcon(icon2)
        self.pbIngresar.setObjectName(_fromUtf8("pbIngresar"))
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Resolución de Ecuaciones", None))
        self.lblBienvenido.setText(_translate("MainWindow", "Bienvenido al Software de resolución de Ecuaciones", None))
        self.pbSalir.setText(_translate("MainWindow", "Salir", None))
        self.pbConfig.setToolTip(_translate("MainWindow", "<html><head/><body><p>Download aggiornamento</p></body></html>", None))
        self.pbIngresar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Installa aggiornamento</p></body></html>", None))
        self.pbIngresar.setText(_translate("MainWindow", "Ingresar", None))

import Ventanas.imagenes_rc

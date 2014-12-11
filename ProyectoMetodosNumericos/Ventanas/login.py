# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Mon Nov 17 11:40:02 2014
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
        MainWindow.resize(626, 606)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("border-image: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 551, 551))
        self.groupBox.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setStyleSheet(_fromUtf8("border-image:url(:/logo_header_jan.png)"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 14pt \"MS Shell Dlg 2\";\n"
"font: 75 16pt \"MV Boli\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setStyleSheet(_fromUtf8("border-image:url(:/119499456854720557funct.svg.med.png)"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagenes/119499456854720557funct.svg.med.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.btnSalir = QtGui.QPushButton(self.groupBox_2)
        self.btnSalir.setGeometry(QtCore.QRect(380, 20, 131, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/dialog-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon1)
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        self.btnConfig = QtGui.QPushButton(self.groupBox_2)
        self.btnConfig.setGeometry(QtCore.QRect(50, 20, 61, 61))
        self.btnConfig.setStyleSheet(_fromUtf8("border-image: url(:/system-software-update.png)"))
        self.btnConfig.setText(_fromUtf8(""))
        self.btnConfig.setObjectName(_fromUtf8("btnConfig"))
        self.btnIngresar = QtGui.QPushButton(self.groupBox_2)
        self.btnIngresar.setGeometry(QtCore.QRect(220, 20, 131, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIngresar.setIcon(icon2)
        self.btnIngresar.setObjectName(_fromUtf8("btnIngresar"))
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Resolución de Ecuaciones", None))
        self.label_2.setText(_translate("MainWindow", "Bienvenido al Software de resolución de Ecuaciones", None))
        self.btnSalir.setText(_translate("MainWindow", "Salir", None))
        self.btnConfig.setToolTip(_translate("MainWindow", "<html><head/><body><p>Download aggiornamento</p></body></html>", None))
        self.btnIngresar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Installa aggiornamento</p></body></html>", None))
        self.btnIngresar.setText(_translate("MainWindow", "Ingresar", None))

import imagenes_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\manuel\Documents\ProyectoMetodos\ProyectoMetodosNumericos\ProyectoMetodosNumericos\Ventanas/login.ui'
#
# Created: Wed Nov 19 20:52:50 2014
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

class TestObject(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(626, 606)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("border-image: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 551, 551))
        self.groupBox.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setStyleSheet(_fromUtf8("border-image:url(:/logo_header_jan.png)"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 14pt \"MS Shell Dlg 2\";\n"
"font: 75 16pt \"MV Boli\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setStyleSheet(_fromUtf8("border-image:url(:/119499456854720557funct.svg.med.png)"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagenes/119499456854720557funct.svg.med.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.btnSalir = QtGui.QPushButton(self.groupBox_2)
        self.btnSalir.setGeometry(QtCore.QRect(380, 20, 131, 61))
        self.btnSalir.setStyleSheet(_fromUtf8("\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" "))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/dialog-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon1)
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        self.btnConfig = QtGui.QPushButton(self.groupBox_2)
        self.btnConfig.setGeometry(QtCore.QRect(50, 20, 61, 61))
        self.btnConfig.setStyleSheet(_fromUtf8("border-image: url(:/system-software-update.png)"))
        self.btnConfig.setText(_fromUtf8(""))
        self.btnConfig.setObjectName(_fromUtf8("btnConfig"))
        self.btnIngresar = QtGui.QPushButton(self.groupBox_2)
        self.btnIngresar.setGeometry(QtCore.QRect(220, 20, 131, 61))
        self.btnIngresar.setStyleSheet(_fromUtf8("\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" "))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIngresar.setIcon(icon2)
        self.btnIngresar.setObjectName(_fromUtf8("btnIngresar"))
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Resolución de Ecuaciones", None))
        self.label_2.setText(_translate("MainWindow", "Bienvenido al Software de resolución de Ecuaciones", None))
        self.btnSalir.setText(_translate("MainWindow", "Salir", None))
        self.btnConfig.setToolTip(_translate("MainWindow", "<html><head/><body><p>Download aggiornamento</p></body></html>", None))
        self.btnIngresar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Installa aggiornamento</p></body></html>", None))
        self.btnIngresar.setText(_translate("MainWindow", "Ingresar", None))

import imagenes_rc

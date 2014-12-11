# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IngresarFuncion.ui'
#
# Created: Mon Nov 17 12:22:07 2014
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
        MainWindow.resize(818, 560)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 261, 71))
        self.label.setObjectName(_fromUtf8("label"))
        self.lnFuncion = QtGui.QLineEdit(self.centralwidget)
        self.lnFuncion.setGeometry(QtCore.QRect(180, 110, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lnFuncion.setFont(font)
        self.lnFuncion.setText(_fromUtf8(""))
        self.lnFuncion.setObjectName(_fromUtf8("lnFuncion"))
        self.btnBorrar = QtGui.QPushButton(self.centralwidget)
        self.btnBorrar.setGeometry(QtCore.QRect(630, 110, 51, 31))
        self.btnBorrar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBorrar.setIcon(icon1)
        self.btnBorrar.setObjectName(_fromUtf8("btnBorrar"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(120, 110, 51, 31))
        self.commandLinkButton_2.setText(_fromUtf8(""))
        self.commandLinkButton_2.setIcon(icon)
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.btnEvaluar = QtGui.QPushButton(self.centralwidget)
        self.btnEvaluar.setGeometry(QtCore.QRect(290, 210, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnEvaluar.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/pagefold.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEvaluar.setIcon(icon2)
        self.btnEvaluar.setObjectName(_fromUtf8("btnEvaluar"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 330, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnContinuar = QtGui.QPushButton(self.centralwidget)
        self.btnContinuar.setGeometry(QtCore.QRect(210, 420, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnContinuar.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/dialog-ok-apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnContinuar.setIcon(icon3)
        self.btnContinuar.setObjectName(_fromUtf8("btnContinuar"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(130, 280, 551, 20))
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.btnSalir = QtGui.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(500, 420, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnSalir.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon4)
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ingresar Función", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">Ingrese Función</span></p></body></html>", None))
        self.btnEvaluar.setText(_translate("MainWindow", "Evaluar Función", None))
        self.label_2.setText(_translate("MainWindow", "Nota: Asegurarse que la \n"
"función pase por el eje x.", None))
        self.btnContinuar.setText(_translate("MainWindow", "Continuar", None))
        self.btnSalir.setText(_translate("MainWindow", "Salir", None))

import imagenes_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\manuel\Documents\ProyectoMetodos\ProyectoMetodosNumericos\ProyectoMetodosNumericos\Ventanas/IngresarFuncion.ui'
#
# Created: Wed Nov 19 21:01:43 2014
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
        MainWindow.resize(818, 560)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 261, 71))
        self.label.setObjectName(_fromUtf8("label"))
        self.lnFuncion = QtGui.QLineEdit(self.centralwidget)
        self.lnFuncion.setGeometry(QtCore.QRect(180, 110, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lnFuncion.setFont(font)
        self.lnFuncion.setStyleSheet(_fromUtf8(" border: 2px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;"))
        self.lnFuncion.setText(_fromUtf8(""))
        self.lnFuncion.setObjectName(_fromUtf8("lnFuncion"))
        self.btnBorrar = QtGui.QPushButton(self.centralwidget)
        self.btnBorrar.setGeometry(QtCore.QRect(630, 110, 51, 31))
        self.btnBorrar.setStyleSheet(_fromUtf8("border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     "))
        self.btnBorrar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBorrar.setIcon(icon1)
        self.btnBorrar.setObjectName(_fromUtf8("btnBorrar"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(120, 110, 51, 31))
        self.commandLinkButton_2.setText(_fromUtf8(""))
        self.commandLinkButton_2.setIcon(icon)
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.btnEvaluar = QtGui.QPushButton(self.centralwidget)
        self.btnEvaluar.setGeometry(QtCore.QRect(290, 210, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnEvaluar.setFont(font)
        self.btnEvaluar.setStyleSheet(_fromUtf8("border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/pagefold.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEvaluar.setIcon(icon2)
        self.btnEvaluar.setObjectName(_fromUtf8("btnEvaluar"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 330, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnContinuar = QtGui.QPushButton(self.centralwidget)
        self.btnContinuar.setGeometry(QtCore.QRect(210, 420, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnContinuar.setFont(font)
        self.btnContinuar.setStyleSheet(_fromUtf8("border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/dialog-ok-apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnContinuar.setIcon(icon3)
        self.btnContinuar.setObjectName(_fromUtf8("btnContinuar"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(130, 280, 551, 20))
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.btnSalir = QtGui.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(500, 420, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnSalir.setFont(font)
        self.btnSalir.setStyleSheet(_fromUtf8("border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon4)
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ingresar Función", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">Ingrese Función</span></p></body></html>", None))
        self.btnEvaluar.setText(_translate("MainWindow", "Evaluar Función", None))
        self.label_2.setText(_translate("MainWindow", "Nota: Asegurarse que la \n"
"función pase por el eje x.", None))
        self.btnContinuar.setText(_translate("MainWindow", "Continuar", None))
        self.btnSalir.setText(_translate("MainWindow", "Salir", None))

import imagenes_rc

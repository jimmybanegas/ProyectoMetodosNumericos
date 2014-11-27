# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\manuel\Documents\ProyectoMetodos\ProyectoMetodosNumericos\ProyectoMetodosNumericos\Ventanas\Historial.ui'
#
# Created: Tue Nov 25 19:29:10 2014
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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(715, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(340, 20, 20, 451))
        self.line.setStyleSheet(_fromUtf8("\n"
"   \n"
" "))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 60, 321, 401))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.lbResultados = QtGui.QLabel(self.centralwidget)
        self.lbResultados.setGeometry(QtCore.QRect(380, 20, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lbResultados.setFont(font)
        self.lbResultados.setObjectName(_fromUtf8("lbResultados"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(370, 100, 321, 351))
        self.scrollArea.setStyleSheet(_fromUtf8(" border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
" "))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 317, 347))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btnRegresar = QtGui.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(300, 480, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setStyleSheet(_fromUtf8(" border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" "))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegresar.setIcon(icon1)
        self.btnRegresar.setObjectName(_fromUtf8("btnRegresar"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Historial", None))
        self.label.setText(_translate("mainWindow", "f(x) = ", None))
        self.lbResultados.setText(_translate("mainWindow", "Resultados De Algoritmos \n"
"             Utilizados", None))
        self.btnRegresar.setText(_translate("mainWindow", "Regresar", None))

import imagenes_rc


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IngresarFuncion.ui'
#
# Created: Mon Nov 10 11:00:44 2014
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
        MainWindow.resize(656, 449)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 261, 71))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(330, 10, 20, 391))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(360, 20, 281, 371))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.lnFuncion = QtGui.QLineEdit(self.centralwidget)
        self.lnFuncion.setGeometry(QtCore.QRect(80, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lnFuncion.setFont(font)
        self.lnFuncion.setText(_fromUtf8(""))
        self.lnFuncion.setObjectName(_fromUtf8("lnFuncion"))
        self.btnBorrar = QtGui.QPushButton(self.centralwidget)
        self.btnBorrar.setGeometry(QtCore.QRect(260, 100, 51, 31))
        self.btnBorrar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBorrar.setIcon(icon)
        self.btnBorrar.setObjectName(_fromUtf8("btnBorrar"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 51, 31))
        self.pushButton_2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.btnEvaluar = QtGui.QPushButton(self.centralwidget)
        self.btnEvaluar.setGeometry(QtCore.QRect(40, 160, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnEvaluar.setFont(font)
        self.btnEvaluar.setObjectName(_fromUtf8("btnEvaluar"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 280, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnContinuar = QtGui.QPushButton(self.centralwidget)
        self.btnContinuar.setGeometry(QtCore.QRect(100, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnContinuar.setFont(font)
        self.btnContinuar.setObjectName(_fromUtf8("btnContinuar"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 250, 321, 20))
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 21))
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
        
    def Borrar(self): 
        self.ui.lnFuncion.clear()       

import imagenes_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IngresarFuncion.ui'
#
# Created: Sun Nov 02 17:36:19 2014
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
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pbFuncion = QtGui.QPushButton(self.centralwidget)
        self.pbFuncion.setGeometry(QtCore.QRect(260, 100, 51, 31))
        self.pbFuncion.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbFuncion.setIcon(icon)
        self.pbFuncion.setObjectName(_fromUtf8("pbFuncion"))
        self.pbFuncion = QtGui.QPushButton(self.centralwidget)
        self.pbFuncion.setGeometry(QtCore.QRect(10, 100, 51, 31))
        self.pbFuncion.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbFuncion.setIcon(icon1)
        self.pbFuncion.setObjectName(_fromUtf8("pbFuncion"))
        self.pbEvaluar = QtGui.QPushButton(self.centralwidget)
        self.pbEvaluar.setGeometry(QtCore.QRect(40, 160, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbEvaluar.setFont(font)
        self.pbEvaluar.setObjectName(_fromUtf8("pbEvaluar"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 280, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pbContinue = QtGui.QPushButton(self.centralwidget)
        self.pbContinue.setGeometry(QtCore.QRect(100, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pbContinue.setFont(font)
        self.pbContinue.setObjectName(_fromUtf8("pbContinue"))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">Ingrese Funcion</span></p></body></html>", None))
        self.pbEvaluar.setText(_translate("MainWindow", "Evaluar Funcion", None))
        self.label_2.setText(_translate("MainWindow", "Nota: Asegurarse que la \n"
"funcion pase por el eje x.", None))
        self.pbContinue.setText(_translate("MainWindow", "Continuar", None))

import imagenes_rc

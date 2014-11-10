# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graph.ui'
#
# Created: Sun Nov 02 21:56:31 2014
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
        MainWindow.resize(582, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(25, 510, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lbResult = QtGui.QLabel(self.centralwidget)
        self.lbResult.setGeometry(QtCore.QRect(140, 510, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbResult.setFont(font)
        self.lbResult.setText(_fromUtf8(""))
        self.lbResult.setObjectName(_fromUtf8("lbResult"))
        self.pbPasos = QtGui.QPushButton(self.centralwidget)
        self.pbPasos.setGeometry(QtCore.QRect(360, 500, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pbPasos.setFont(font)
        self.pbPasos.setObjectName(_fromUtf8("pbPasos"))
        self.wgResult = QtGui.QWidget(self.centralwidget)
        self.wgResult.setGeometry(QtCore.QRect(49, 59, 481, 381))
        self.wgResult.setObjectName(_fromUtf8("wgResult"))
        self.lbImage = QtGui.QLabel(self.wgResult)
        self.lbImage.setGeometry(QtCore.QRect(20, 20, 441, 341))
        self.lbImage.setObjectName(_fromUtf8("lbImage"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "Resultado:", None))
        self.pbPasos.setText(_translate("MainWindow", "Ver Pasos", None))
        self.lbImage.setText(_translate("MainWindow", "Placeholder de la imagen de la grafica", None))
        self.label.setText(_translate("MainWindow", "Grafica de la funcion ingresada", None))


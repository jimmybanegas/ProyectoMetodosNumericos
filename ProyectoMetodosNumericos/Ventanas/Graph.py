# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graph.ui'
#
# Created: Mon Nov 17 13:53:08 2014
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
        MainWindow.resize(581, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 440, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lbResult = QtGui.QLabel(self.centralwidget)
        self.lbResult.setGeometry(QtCore.QRect(165, 440, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbResult.setFont(font)
        self.lbResult.setText(_fromUtf8(""))
        self.lbResult.setObjectName(_fromUtf8("lbResult"))
        self.btnVerPasos = QtGui.QPushButton(self.centralwidget)
        self.btnVerPasos.setGeometry(QtCore.QRect(320, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnVerPasos.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit-find.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVerPasos.setIcon(icon1)
        self.btnVerPasos.setObjectName(_fromUtf8("btnVerPasos"))
        self.wgResult = QtGui.QWidget(self.centralwidget)
        self.wgResult.setGeometry(QtCore.QRect(49, 59, 471, 331))
        self.wgResult.setObjectName(_fromUtf8("wgResult"))
        self.lbImage = QtGui.QLabel(self.wgResult)
        self.lbImage.setGeometry(QtCore.QRect(20, 20, 441, 291))
        self.lbImage.setObjectName(_fromUtf8("lbImage"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btnRegresar = QtGui.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(140, 490, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresar.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegresar.setIcon(icon2)
        self.btnRegresar.setObjectName(_fromUtf8("btnRegresar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Resultado", None))
        self.label_3.setText(_translate("MainWindow", "Resultado:", None))
        self.btnVerPasos.setText(_translate("MainWindow", "Ver Pasos", None))
        self.lbImage.setText(_translate("MainWindow", "Placeholder de la imagen de la grafica", None))
        self.label.setText(_translate("MainWindow", "Gráfica de la función ingresada", None))
        self.btnRegresar.setText(_translate("MainWindow", "Regresar", None))

import imagenes_rc

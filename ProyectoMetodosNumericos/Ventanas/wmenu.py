# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wmenu.ui'
#
# Created: Thu Jun 19 15:12:25 2014
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

class Ui_WMenu(object):
    def setupUi(self, WMenu):
        WMenu.setObjectName(_fromUtf8("WMenu"))
        WMenu.resize(601, 481)
        self.centralwidget = QtGui.QWidget(WMenu)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pbResoluEq = QtGui.QPushButton(self.centralwidget)
        self.pbResoluEq.setGeometry(QtCore.QRect(130, 50, 331, 41))
        self.pbResoluEq.setObjectName(_fromUtf8("pbResoluEq"))
        self.pbRungeEdo = QtGui.QPushButton(self.centralwidget)
        self.pbRungeEdo.setGeometry(QtCore.QRect(130, 120, 331, 41))
        self.pbRungeEdo.setObjectName(_fromUtf8("pbRungeEdo"))
        self.pbRungeSis = QtGui.QPushButton(self.centralwidget)
        self.pbRungeSis.setGeometry(QtCore.QRect(130, 190, 331, 41))
        self.pbRungeSis.setObjectName(_fromUtf8("pbRungeSis"))
        self.pbSimpson = QtGui.QPushButton(self.centralwidget)
        self.pbSimpson.setGeometry(QtCore.QRect(130, 260, 331, 41))
        self.pbSimpson.setObjectName(_fromUtf8("pbSimpson"))
        self.pbLineal = QtGui.QPushButton(self.centralwidget)
        self.pbLineal.setGeometry(QtCore.QRect(130, 330, 331, 41))
        self.pbLineal.setObjectName(_fromUtf8("pbLineal"))
        self.pbIndice = QtGui.QPushButton(self.centralwidget)
        self.pbIndice.setGeometry(QtCore.QRect(130, 400, 331, 41))
        self.pbIndice.setObjectName(_fromUtf8("pbIndice"))
        WMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(WMenu)
        QtCore.QObject.connect(self.pbIndice, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pbIndice.click)
        QtCore.QMetaObject.connectSlotsByName(WMenu)

    def retranslateUi(self, WMenu):
        WMenu.setWindowTitle(_translate("WMenu", "MainWindow", None))
        self.pbResoluEq.setText(_translate("WMenu", "Resolucion de Ecuaciones", None))
        self.pbRungeEdo.setText(_translate("WMenu", "Metodo de Runge-Kutta EDO", None))
        self.pbRungeSis.setText(_translate("WMenu", "Metodo de Runge-Kutta Sistemas de Ecuaciones", None))
        self.pbSimpson.setText(_translate("WMenu", "Integracion por Metodo de Simpson", None))
        self.pbLineal.setText(_translate("WMenu", "Diferenciacion por Metodo Lineal de Diferencias Finitas", None))
        self.pbIndice.setText(_translate("WMenu", "Indice de Algoritmos sin Interfaz Grafica", None))


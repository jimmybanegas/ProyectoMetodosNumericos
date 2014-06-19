# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wRungeEdo.ui'
#
# Created: Wed Jun 18 19:45:17 2014
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

class Ui_WRungeEdo(object):
    def setupUi(self, WRungeEdo):
        WRungeEdo.setObjectName(_fromUtf8("WRungeEdo"))
        WRungeEdo.resize(598, 424)
        self.centralwidget = QtGui.QWidget(WRungeEdo)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.leExpresion = QtGui.QLineEdit(self.centralwidget)
        self.leExpresion.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.leExpresion.setObjectName(_fromUtf8("leExpresion"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 46, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.teResultado = QtGui.QTextEdit(self.centralwidget)
        self.teResultado.setGeometry(QtCore.QRect(20, 130, 561, 261))
        self.teResultado.setObjectName(_fromUtf8("teResultado"))
        self.pbResolver = QtGui.QPushButton(self.centralwidget)
        self.pbResolver.setGeometry(QtCore.QRect(390, 90, 111, 23))
        self.pbResolver.setObjectName(_fromUtf8("pbResolver"))
        self.leExa = QtGui.QLineEdit(self.centralwidget)
        self.leExa.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.leExa.setObjectName(_fromUtf8("leExa"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.leExb = QtGui.QLineEdit(self.centralwidget)
        self.leExb.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.leExb.setObjectName(_fromUtf8("leExb"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.leAlpha = QtGui.QLineEdit(self.centralwidget)
        self.leAlpha.setGeometry(QtCore.QRect(390, 30, 113, 20))
        self.leAlpha.setObjectName(_fromUtf8("leAlpha"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 30, 46, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 60, 46, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.leEne = QtGui.QLineEdit(self.centralwidget)
        self.leEne.setGeometry(QtCore.QRect(390, 60, 113, 20))
        self.leEne.setObjectName(_fromUtf8("leEne"))
        WRungeEdo.setCentralWidget(self.centralwidget)

        self.retranslateUi(WRungeEdo)
        QtCore.QMetaObject.connectSlotsByName(WRungeEdo)

    def retranslateUi(self, WRungeEdo):
        WRungeEdo.setWindowTitle(_translate("WRungeEdo", "MainWindow", None))
        self.label.setText(_translate("WRungeEdo", "Expresion", None))
        self.pbResolver.setText(_translate("WRungeEdo", "Resolver", None))
        self.label_2.setText(_translate("WRungeEdo", "Extremo a", None))
        self.label_3.setText(_translate("WRungeEdo", "Extremo b", None))
        self.label_4.setText(_translate("WRungeEdo", "Alpha", None))
        self.label_5.setText(_translate("WRungeEdo", "N", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wsimpson.ui'
#
# Created: Wed Jun 18 23:16:23 2014
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

class Ui_WSimpson(object):
    def setupUi(self, WSimpson):
        WSimpson.setObjectName(_fromUtf8("WSimpson"))
        WSimpson.resize(544, 415)
        self.centralwidget = QtGui.QWidget(WSimpson)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.teResultado = QtGui.QTextEdit(self.centralwidget)
        self.teResultado.setGeometry(QtCore.QRect(30, 110, 491, 241))
        self.teResultado.setObjectName(_fromUtf8("teResultado"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 360, 61, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lbResultado = QtGui.QLabel(self.centralwidget)
        self.lbResultado.setGeometry(QtCore.QRect(360, 360, 161, 31))
        self.lbResultado.setObjectName(_fromUtf8("lbResultado"))
        self.pbResolver = QtGui.QPushButton(self.centralwidget)
        self.pbResolver.setGeometry(QtCore.QRect(30, 360, 111, 23))
        self.pbResolver.setObjectName(_fromUtf8("pbResolver"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 491, 48))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.leFX = QtGui.QLineEdit(self.layoutWidget)
        self.leFX.setObjectName(_fromUtf8("leFX"))
        self.gridLayout.addWidget(self.leFX, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.leA = QtGui.QLineEdit(self.layoutWidget)
        self.leA.setObjectName(_fromUtf8("leA"))
        self.gridLayout.addWidget(self.leA, 0, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 2)
        self.leN = QtGui.QLineEdit(self.layoutWidget)
        self.leN.setObjectName(_fromUtf8("leN"))
        self.gridLayout.addWidget(self.leN, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.leB = QtGui.QLineEdit(self.layoutWidget)
        self.leB.setObjectName(_fromUtf8("leB"))
        self.gridLayout.addWidget(self.leB, 1, 4, 1, 1)
        WSimpson.setCentralWidget(self.centralwidget)

        self.retranslateUi(WSimpson)
        QtCore.QMetaObject.connectSlotsByName(WSimpson)
        WSimpson.setTabOrder(self.leFX, self.leN)
        WSimpson.setTabOrder(self.leN, self.leA)
        WSimpson.setTabOrder(self.leA, self.leB)
        WSimpson.setTabOrder(self.leB, self.teResultado)
        WSimpson.setTabOrder(self.teResultado, self.pbResolver)

    def retranslateUi(self, WSimpson):
        WSimpson.setWindowTitle(_translate("WSimpson", "MainWindow", None))
        self.label_5.setText(_translate("WSimpson", "Resultado: ", None))
        self.lbResultado.setText(_translate("WSimpson", "0", None))
        self.pbResolver.setText(_translate("WSimpson", "Resolver", None))
        self.label.setText(_translate("WSimpson", "Ecuacion F(X):", None))
        self.label_2.setText(_translate("WSimpson", "Limite inferior A:", None))
        self.label_4.setText(_translate("WSimpson", "Numero de Iteraciones N: ", None))
        self.label_3.setText(_translate("WSimpson", "Limite inferior B:", None))


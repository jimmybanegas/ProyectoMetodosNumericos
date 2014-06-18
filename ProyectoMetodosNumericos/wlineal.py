# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wlineal.ui'
#
# Created: Wed Jun 18 16:48:45 2014
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

class Ui_wsimpson(object):
    def setupUi(self, wsimpson):
        wsimpson.setObjectName(_fromUtf8("wsimpson"))
        wsimpson.resize(547, 432)
        self.centralwidget = QtGui.QWidget(wsimpson)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pbResolver = QtGui.QPushButton(self.centralwidget)
        self.pbResolver.setGeometry(QtCore.QRect(390, 140, 131, 23))
        self.pbResolver.setObjectName(_fromUtf8("pbResolver"))
        self.lePx = QtGui.QLineEdit(self.centralwidget)
        self.lePx.setGeometry(QtCore.QRect(70, 50, 113, 20))
        self.lePx.setObjectName(_fromUtf8("lePx"))
        self.leQx = QtGui.QLineEdit(self.centralwidget)
        self.leQx.setGeometry(QtCore.QRect(70, 100, 113, 20))
        self.leQx.setObjectName(_fromUtf8("leQx"))
        self.leRx = QtGui.QLineEdit(self.centralwidget)
        self.leRx.setGeometry(QtCore.QRect(70, 140, 113, 20))
        self.leRx.setObjectName(_fromUtf8("leRx"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.leAlpha = QtGui.QLineEdit(self.centralwidget)
        self.leAlpha.setGeometry(QtCore.QRect(290, 140, 61, 20))
        self.leAlpha.setObjectName(_fromUtf8("leAlpha"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 50, 51, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 140, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 100, 51, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.leExa = QtGui.QLineEdit(self.centralwidget)
        self.leExa.setGeometry(QtCore.QRect(290, 50, 61, 20))
        self.leExa.setObjectName(_fromUtf8("leExa"))
        self.leExb = QtGui.QLineEdit(self.centralwidget)
        self.leExb.setGeometry(QtCore.QRect(290, 100, 61, 20))
        self.leExb.setObjectName(_fromUtf8("leExb"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 50, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(390, 100, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.leBeta = QtGui.QLineEdit(self.centralwidget)
        self.leBeta.setGeometry(QtCore.QRect(460, 50, 61, 20))
        self.leBeta.setObjectName(_fromUtf8("leBeta"))
        self.leEne = QtGui.QLineEdit(self.centralwidget)
        self.leEne.setGeometry(QtCore.QRect(460, 100, 61, 20))
        self.leEne.setObjectName(_fromUtf8("leEne"))
        self.teResultado = QtGui.QTextEdit(self.centralwidget)
        self.teResultado.setGeometry(QtCore.QRect(30, 190, 491, 181))
        self.teResultado.setObjectName(_fromUtf8("teResultado"))
        wsimpson.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(wsimpson)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        wsimpson.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(wsimpson)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        wsimpson.setStatusBar(self.statusbar)

        self.retranslateUi(wsimpson)
        QtCore.QMetaObject.connectSlotsByName(wsimpson)
        wsimpson.setTabOrder(self.lePx, self.leQx)
        wsimpson.setTabOrder(self.leQx, self.leRx)
        wsimpson.setTabOrder(self.leRx, self.leExa)
        wsimpson.setTabOrder(self.leExa, self.leExb)
        wsimpson.setTabOrder(self.leExb, self.leAlpha)
        wsimpson.setTabOrder(self.leAlpha, self.leBeta)
        wsimpson.setTabOrder(self.leBeta, self.leEne)
        wsimpson.setTabOrder(self.leEne, self.pbResolver)
        wsimpson.setTabOrder(self.pbResolver, self.teResultado)

    def retranslateUi(self, wsimpson):
        wsimpson.setWindowTitle(_translate("wsimpson", "MainWindow", None))
        self.pbResolver.setText(_translate("wsimpson", "Resolver", None))
        self.label.setText(_translate("wsimpson", "p(x)", None))
        self.label_2.setText(_translate("wsimpson", "q(x)", None))
        self.label_3.setText(_translate("wsimpson", "r(x)", None))
        self.label_4.setText(_translate("wsimpson", "Extremo a", None))
        self.label_5.setText(_translate("wsimpson", "alpha", None))
        self.label_6.setText(_translate("wsimpson", "Extremo b", None))
        self.label_7.setText(_translate("wsimpson", "beta", None))
        self.label_9.setText(_translate("wsimpson", "Entero N", None))


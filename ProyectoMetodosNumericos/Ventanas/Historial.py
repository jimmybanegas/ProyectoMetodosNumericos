# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Historial.ui'
#
# Created: Sun Dec 07 21:55:42 2014
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
        MainWindow.resize(645, 547)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.cbFx = QtGui.QComboBox(self.centralwidget)
        self.cbFx.setGeometry(QtCore.QRect(130, 20, 251, 31))
        self.cbFx.setObjectName(_fromUtf8("cbFx"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.teSteps = QtGui.QTextEdit(self.centralwidget)
        self.teSteps.setGeometry(QtCore.QRect(30, 70, 431, 431))
        self.teSteps.setObjectName(_fromUtf8("teSteps"))
        self.btnRegresar = QtGui.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(510, 170, 101, 31))
        self.btnRegresar.setObjectName(_fromUtf8("btnRegresar"))
        self.btnWord = QtGui.QPushButton(self.centralwidget)
        self.btnWord.setGeometry(QtCore.QRect(500, 250, 131, 51))
        self.btnWord.setObjectName(_fromUtf8("btnWord"))
        self.lblExito = QtGui.QLabel(self.centralwidget)
        self.lblExito.setGeometry(QtCore.QRect(520, 330, 46, 13))
        self.lblExito.setText(_fromUtf8(""))
        self.lblExito.setObjectName(_fromUtf8("lblExito"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "F(X)=", None))
        self.btnRegresar.setText(_translate("MainWindow", "Regresar", None))
        self.btnWord.setText(_translate("MainWindow", "Exportar a Word", None))


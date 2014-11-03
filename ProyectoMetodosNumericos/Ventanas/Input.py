# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Input.ui'
#
# Created: Sun Nov 02 21:57:13 2014
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
        MainWindow.resize(712, 463)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.leEquation = QtGui.QLineEdit(self.centralwidget)
        self.leEquation.setGeometry(QtCore.QRect(90, 40, 259, 20))
        self.leEquation.setObjectName(_fromUtf8("leEquation"))
        self.cboMethod = QtGui.QComboBox(self.centralwidget)
        self.cboMethod.setGeometry(QtCore.QRect(560, 40, 115, 20))
        self.cboMethod.setObjectName(_fromUtf8("cboMethod"))
        self.cboMethod.addItem(_fromUtf8(""))
        self.cboMethod.addItem(_fromUtf8(""))
        self.cboMethod.addItem(_fromUtf8(""))
        self.cboMethod.addItem(_fromUtf8(""))
        self.cboMethod.addItem(_fromUtf8(""))
        self.cboMethod.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 40, 61, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 40, 61, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupParameters = QtGui.QGroupBox(self.centralwidget)
        self.groupParameters.setGeometry(QtCore.QRect(20, 70, 661, 341))
        self.groupParameters.setObjectName(_fromUtf8("groupParameters"))
        self.leParam4 = QtGui.QLineEdit(self.groupParameters)
        self.leParam4.setGeometry(QtCore.QRect(160, 120, 81, 20))
        self.leParam4.setObjectName(_fromUtf8("leParam4"))
        self.lbParam3 = QtGui.QLabel(self.groupParameters)
        self.lbParam3.setGeometry(QtCore.QRect(30, 90, 131, 21))
        self.lbParam3.setObjectName(_fromUtf8("lbParam3"))
        self.leParam3 = QtGui.QLineEdit(self.groupParameters)
        self.leParam3.setGeometry(QtCore.QRect(160, 90, 81, 20))
        self.leParam3.setObjectName(_fromUtf8("leParam3"))
        self.lbParam4 = QtGui.QLabel(self.groupParameters)
        self.lbParam4.setGeometry(QtCore.QRect(30, 120, 121, 21))
        self.lbParam4.setObjectName(_fromUtf8("lbParam4"))
        self.leParam2 = QtGui.QLineEdit(self.groupParameters)
        self.leParam2.setGeometry(QtCore.QRect(160, 60, 81, 20))
        self.leParam2.setObjectName(_fromUtf8("leParam2"))
        self.leParam5 = QtGui.QLineEdit(self.groupParameters)
        self.leParam5.setGeometry(QtCore.QRect(160, 150, 81, 20))
        self.leParam5.setObjectName(_fromUtf8("leParam5"))
        self.lbParam2 = QtGui.QLabel(self.groupParameters)
        self.lbParam2.setGeometry(QtCore.QRect(30, 60, 131, 21))
        self.lbParam2.setObjectName(_fromUtf8("lbParam2"))
        self.leParam1 = QtGui.QLineEdit(self.groupParameters)
        self.leParam1.setGeometry(QtCore.QRect(160, 30, 81, 20))
        self.leParam1.setObjectName(_fromUtf8("leParam1"))
        self.lbParam1 = QtGui.QLabel(self.groupParameters)
        self.lbParam1.setGeometry(QtCore.QRect(30, 30, 131, 21))
        self.lbParam1.setObjectName(_fromUtf8("lbParam1"))
        self.lbParam5 = QtGui.QLabel(self.groupParameters)
        self.lbParam5.setGeometry(QtCore.QRect(30, 150, 121, 21))
        self.lbParam5.setObjectName(_fromUtf8("lbParam5"))
        self.pbCalculate = QtGui.QPushButton(self.groupParameters)
        self.pbCalculate.setGeometry(QtCore.QRect(20, 250, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbCalculate.setFont(font)
        self.pbCalculate.setObjectName(_fromUtf8("pbCalculate"))
        self.lbEjemplo = QtGui.QLabel(self.groupParameters)
        self.lbEjemplo.setGeometry(QtCore.QRect(440, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbEjemplo.setFont(font)
        self.lbEjemplo.setObjectName(_fromUtf8("lbEjemplo"))
        self.label_3 = QtGui.QLabel(self.groupParameters)
        self.label_3.setGeometry(QtCore.QRect(440, 40, 201, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupParameters)
        self.label_4.setGeometry(QtCore.QRect(390, 80, 251, 241))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.cboMethod.setItemText(0, _translate("MainWindow", "Biseccion", None))
        self.cboMethod.setItemText(1, _translate("MainWindow", "Iteracion de punto fijo", None))
        self.cboMethod.setItemText(2, _translate("MainWindow", "Newton", None))
        self.cboMethod.setItemText(3, _translate("MainWindow", "Secante", None))
        self.cboMethod.setItemText(4, _translate("MainWindow", "Posicion Falsa", None))
        self.cboMethod.setItemText(5, _translate("MainWindow", "Muller", None))
        self.label.setText(_translate("MainWindow", "Ecuacion:", None))
        self.label_2.setText(_translate("MainWindow", "Metodo:", None))
        self.groupParameters.setTitle(_translate("MainWindow", "Parametros", None))
        self.lbParam3.setText(_translate("MainWindow", "Param3:", None))
        self.lbParam4.setText(_translate("MainWindow", "Param4:", None))
        self.lbParam2.setText(_translate("MainWindow", "Param2:", None))
        self.lbParam1.setText(_translate("MainWindow", "Param1:", None))
        self.lbParam5.setText(_translate("MainWindow", "Param5:", None))
        self.pbCalculate.setText(_translate("MainWindow", "Ver Resultado", None))
        self.lbEjemplo.setText(_translate("MainWindow", "Ejemplo", None))
        self.label_3.setText(_translate("MainWindow", "Asi se deben ver los datos", None))
        self.label_4.setText(_translate("MainWindow", "Placeholder", None))


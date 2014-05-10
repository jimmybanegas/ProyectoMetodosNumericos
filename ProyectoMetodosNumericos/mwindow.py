# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwindow.ui'
#
# Created: Sat May 10 08:20:28 2014
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

class Ui_MWindow(object):
    def setupUi(self, MWindow):
        MWindow.setObjectName(_fromUtf8("MWindow"))
        MWindow.resize(763, 504)
        self.centralwidget = QtGui.QWidget(MWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 40, 61, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cboMethod = QtGui.QComboBox(self.centralwidget)
        self.cboMethod.setGeometry(QtCore.QRect(550, 40, 115, 20))
        self.cboMethod.setObjectName(_fromUtf8("cboMethod"))
        self.cboMethod.addItem(_fromUtf8(""))
        self.cboMethod.addItem(_fromUtf8(""))
        self.cboMethod.addItem(_fromUtf8(""))
        self.cboMethod.addItem(_fromUtf8(""))
        self.cboMethod.addItem(_fromUtf8(""))
        self.cboMethod.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 40, 61, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.leEquation = QtGui.QLineEdit(self.centralwidget)
        self.leEquation.setGeometry(QtCore.QRect(80, 40, 259, 20))
        self.leEquation.setObjectName(_fromUtf8("leEquation"))
        self.groupParameters = QtGui.QGroupBox(self.centralwidget)
        self.groupParameters.setGeometry(QtCore.QRect(10, 70, 721, 121))
        self.groupParameters.setObjectName(_fromUtf8("groupParameters"))
        self.leParam4 = QtGui.QLineEdit(self.groupParameters)
        self.leParam4.setGeometry(QtCore.QRect(380, 20, 81, 20))
        self.leParam4.setObjectName(_fromUtf8("leParam4"))
        self.lbParam3 = QtGui.QLabel(self.groupParameters)
        self.lbParam3.setGeometry(QtCore.QRect(10, 80, 131, 21))
        self.lbParam3.setObjectName(_fromUtf8("lbParam3"))
        self.leParam3 = QtGui.QLineEdit(self.groupParameters)
        self.leParam3.setGeometry(QtCore.QRect(140, 80, 81, 20))
        self.leParam3.setObjectName(_fromUtf8("leParam3"))
        self.lbParam4 = QtGui.QLabel(self.groupParameters)
        self.lbParam4.setGeometry(QtCore.QRect(250, 20, 121, 21))
        self.lbParam4.setObjectName(_fromUtf8("lbParam4"))
        self.leParam2 = QtGui.QLineEdit(self.groupParameters)
        self.leParam2.setGeometry(QtCore.QRect(140, 50, 81, 20))
        self.leParam2.setObjectName(_fromUtf8("leParam2"))
        self.leParam5 = QtGui.QLineEdit(self.groupParameters)
        self.leParam5.setGeometry(QtCore.QRect(380, 50, 81, 20))
        self.leParam5.setObjectName(_fromUtf8("leParam5"))
        self.lbParam2 = QtGui.QLabel(self.groupParameters)
        self.lbParam2.setGeometry(QtCore.QRect(10, 50, 131, 21))
        self.lbParam2.setObjectName(_fromUtf8("lbParam2"))
        self.leParam1 = QtGui.QLineEdit(self.groupParameters)
        self.leParam1.setGeometry(QtCore.QRect(140, 20, 81, 20))
        self.leParam1.setObjectName(_fromUtf8("leParam1"))
        self.lbParam1 = QtGui.QLabel(self.groupParameters)
        self.lbParam1.setGeometry(QtCore.QRect(10, 20, 131, 21))
        self.lbParam1.setObjectName(_fromUtf8("lbParam1"))
        self.lbParam5 = QtGui.QLabel(self.groupParameters)
        self.lbParam5.setGeometry(QtCore.QRect(250, 50, 121, 21))
        self.lbParam5.setObjectName(_fromUtf8("lbParam5"))
        self.pbCalculate = QtGui.QPushButton(self.groupParameters)
        self.pbCalculate.setGeometry(QtCore.QRect(524, 90, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbCalculate.setFont(font)
        self.pbCalculate.setObjectName(_fromUtf8("pbCalculate"))
        self.teSteps = QtGui.QTextEdit(self.centralwidget)
        self.teSteps.setGeometry(QtCore.QRect(10, 200, 721, 231))
        self.teSteps.setObjectName(_fromUtf8("teSteps"))
        self.lbResult = QtGui.QLabel(self.centralwidget)
        self.lbResult.setGeometry(QtCore.QRect(545, 440, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbResult.setFont(font)
        self.lbResult.setText(_fromUtf8(""))
        self.lbResult.setObjectName(_fromUtf8("lbResult"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 440, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MWindow)
        QtCore.QMetaObject.connectSlotsByName(MWindow)

    def retranslateUi(self, MWindow):
        MWindow.setWindowTitle(_translate("MWindow", "Resolucion de Ecuaciones", None))
        self.label_2.setText(_translate("MWindow", "Metodo:", None))
        self.cboMethod.setItemText(0, _translate("MWindow", "Biseccion", None))
        self.cboMethod.setItemText(1, _translate("MWindow", "Iteracion de punto fijo", None))
        self.cboMethod.setItemText(2, _translate("MWindow", "Newton", None))
        self.cboMethod.setItemText(3, _translate("MWindow", "Secante", None))
        self.cboMethod.setItemText(4, _translate("MWindow", "Posicion Falsa", None))
        self.cboMethod.setItemText(5, _translate("MWindow", "Muller", None))
        self.label.setText(_translate("MWindow", "Ecuacion:", None))
        self.groupParameters.setTitle(_translate("MWindow", "Parametros", None))
        self.lbParam3.setText(_translate("MWindow", "Param3:", None))
        self.lbParam4.setText(_translate("MWindow", "Param4:", None))
        self.lbParam2.setText(_translate("MWindow", "Param2:", None))
        self.lbParam1.setText(_translate("MWindow", "Param1:", None))
        self.lbParam5.setText(_translate("MWindow", "Param5:", None))
        self.pbCalculate.setText(_translate("MWindow", "Calcular", None))
        self.label_3.setText(_translate("MWindow", "Resultado:", None))


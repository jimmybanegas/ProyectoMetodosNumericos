# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Input.ui'
#
# Created: Mon Nov 17 13:46:45 2014
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
        MainWindow.resize(808, 511)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.leEquation = QtGui.QLineEdit(self.centralwidget)
        self.leEquation.setGeometry(QtCore.QRect(90, 40, 259, 20))
        self.leEquation.setObjectName(_fromUtf8("leEquation"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 40, 61, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupParameters = QtGui.QGroupBox(self.centralwidget)
        self.groupParameters.setGeometry(QtCore.QRect(20, 70, 761, 391))
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
        self.pbCalculate.setGeometry(QtCore.QRect(230, 270, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbCalculate.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/excel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCalculate.setIcon(icon1)
        self.pbCalculate.setObjectName(_fromUtf8("pbCalculate"))
        self.lbEjemplo = QtGui.QLabel(self.groupParameters)
        self.lbEjemplo.setGeometry(QtCore.QRect(410, 10, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbEjemplo.setFont(font)
        self.lbEjemplo.setObjectName(_fromUtf8("lbEjemplo"))
        self.pbRegresar = QtGui.QPushButton(self.groupParameters)
        self.pbRegresar.setGeometry(QtCore.QRect(40, 270, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbRegresar.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbRegresar.setIcon(icon2)
        self.pbRegresar.setObjectName(_fromUtf8("pbRegresar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ingreso de Parámetros", None))
        self.label.setText(_translate("MainWindow", "Ecuación:", None))
        self.groupParameters.setTitle(_translate("MainWindow", "Parámetros", None))
        self.lbParam3.setText(_translate("MainWindow", "Param3:", None))
        self.lbParam4.setText(_translate("MainWindow", "Param4:", None))
        self.lbParam2.setText(_translate("MainWindow", "Param2:", None))
        self.lbParam1.setText(_translate("MainWindow", "Param1:", None))
        self.lbParam5.setText(_translate("MainWindow", "Param5:", None))
        self.pbCalculate.setText(_translate("MainWindow", "Resultado", None))
        self.lbEjemplo.setText(_translate("MainWindow", "Ejemplo", None))
        self.pbRegresar.setText(_translate("MainWindow", "Regresar", None))

import imagenes_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\manuel\Documents\ProyectoMetodos\ProyectoMetodosNumericos\ProyectoMetodosNumericos\Ventanas\Input.ui'
#
# Created: Tue Nov 25 19:30:22 2014
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
        MainWindow.resize(808, 511)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.leEquation = QtGui.QLineEdit(self.centralwidget)
        self.leEquation.setGeometry(QtCore.QRect(90, 40, 259, 20))
        self.leEquation.setStyleSheet(_fromUtf8(" border: 2px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;"))
        self.leEquation.setObjectName(_fromUtf8("leEquation"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 40, 61, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupParameters = QtGui.QGroupBox(self.centralwidget)
        self.groupParameters.setGeometry(QtCore.QRect(20, 70, 761, 391))
        self.groupParameters.setStyleSheet(_fromUtf8("QLineEdit{\n"
"     border: 2px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
"}"))
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
        self.pbCalculate.setGeometry(QtCore.QRect(230, 270, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbCalculate.setFont(font)
        self.pbCalculate.setStyleSheet(_fromUtf8(" border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" "))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/excel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCalculate.setIcon(icon1)
        self.pbCalculate.setObjectName(_fromUtf8("pbCalculate"))
        self.lbEjemplo = QtGui.QLabel(self.groupParameters)
        self.lbEjemplo.setGeometry(QtCore.QRect(410, 10, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbEjemplo.setFont(font)
        self.lbEjemplo.setStyleSheet(_fromUtf8(" border: 2px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0 8px;"))
        self.lbEjemplo.setObjectName(_fromUtf8("lbEjemplo"))
        self.pbRegresar = QtGui.QPushButton(self.groupParameters)
        self.pbRegresar.setGeometry(QtCore.QRect(40, 270, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbRegresar.setFont(font)
        self.pbRegresar.setStyleSheet(_fromUtf8(" border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" "))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbRegresar.setIcon(icon2)
        self.pbRegresar.setObjectName(_fromUtf8("pbRegresar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ingreso de Parámetros", None))
        self.label.setText(_translate("MainWindow", "Ecuación:", None))
        self.groupParameters.setTitle(_translate("MainWindow", "Parámetros", None))
        self.lbParam3.setText(_translate("MainWindow", "Param3:", None))
        self.lbParam4.setText(_translate("MainWindow", "Param4:", None))
        self.lbParam2.setText(_translate("MainWindow", "Param2:", None))
        self.lbParam1.setText(_translate("MainWindow", "Param1:", None))
        self.lbParam5.setText(_translate("MainWindow", "Param5:", None))
        self.pbCalculate.setText(_translate("MainWindow", "Resultado", None))
        self.lbEjemplo.setText(_translate("MainWindow", "Ejemplo", None))
        self.pbRegresar.setText(_translate("MainWindow", "Regresar", None))

import imagenes_rc

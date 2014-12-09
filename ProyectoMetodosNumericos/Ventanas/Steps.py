# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Steps.ui'
#
# Created: Mon Nov 17 14:28:22 2014
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
        MainWindow.resize(546, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.teSteps = QtGui.QTextEdit(self.centralwidget)
        self.teSteps.setGeometry(QtCore.QRect(40, 70, 461, 351))
        self.teSteps.setObjectName(_fromUtf8("teSteps"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btnCerrar = QtGui.QPushButton(self.centralwidget)
        self.btnCerrar.setGeometry(QtCore.QRect(110, 440, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnCerrar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrar.setIcon(icon1)
        self.btnCerrar.setObjectName(_fromUtf8("btnCerrar"))
        self.btnGuardar = QtGui.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(310, 440, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuardar.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/accessories-dictionary.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon2)
        self.btnGuardar.setObjectName(_fromUtf8("btnGuardar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pasos de la ecuación", None))
        self.label.setText(_translate("MainWindow", "Pasos para resolver la ecuación:", None))
        self.btnCerrar.setText(_translate("MainWindow", "Cerrar", None))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar", None))

import imagenes_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\manuel\Documents\ProyectoMetodos\ProyectoMetodosNumericos\ProyectoMetodosNumericos\Ventanas\Steps.ui'
#
# Created: Tue Nov 25 19:31:03 2014
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
        MainWindow.resize(546, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.teSteps = QtGui.QTextEdit(self.centralwidget)
        self.teSteps.setGeometry(QtCore.QRect(40, 70, 461, 351))
        self.teSteps.setObjectName(_fromUtf8("teSteps"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btnCerrar = QtGui.QPushButton(self.centralwidget)
        self.btnCerrar.setGeometry(QtCore.QRect(110, 440, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnCerrar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrar.setIcon(icon1)
        self.btnCerrar.setObjectName(_fromUtf8("btnCerrar"))
        self.btnGuardar = QtGui.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(310, 440, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuardar.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/accessories-dictionary.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon2)
        self.btnGuardar.setObjectName(_fromUtf8("btnGuardar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pasos de la ecuación", None))
        self.label.setText(_translate("MainWindow", "Pasos para resolver la ecuación:", None))
        self.btnCerrar.setText(_translate("MainWindow", "Cerrar", None))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar", None))

import imagenes_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\manuel\Documents\ProyectoMetodos\ProyectoMetodosNumericos\ProyectoMetodosNumericos\Ventanas\Steps.ui'
#
# Created: Tue Nov 25 19:37:49 2014
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
        MainWindow.resize(546, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.teSteps = QtGui.QTextEdit(self.centralwidget)
        self.teSteps.setGeometry(QtCore.QRect(40, 70, 461, 351))
        self.teSteps.setStyleSheet(_fromUtf8(" border: 2px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;"))
        self.teSteps.setObjectName(_fromUtf8("teSteps"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btnCerrar = QtGui.QPushButton(self.centralwidget)
        self.btnCerrar.setGeometry(QtCore.QRect(110, 440, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnCerrar.setFont(font)
        self.btnCerrar.setStyleSheet(_fromUtf8("  border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrar.setIcon(icon1)
        self.btnCerrar.setObjectName(_fromUtf8("btnCerrar"))
        self.btnGuardar = QtGui.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(310, 440, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuardar.setFont(font)
        self.btnGuardar.setStyleSheet(_fromUtf8("  border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/accessories-dictionary.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon2)
        self.btnGuardar.setObjectName(_fromUtf8("btnGuardar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pasos de la ecuación", None))
        self.label.setText(_translate("MainWindow", "Pasos para resolver la ecuación:", None))
        self.btnCerrar.setText(_translate("MainWindow", "Cerrar", None))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar", None))

import imagenes_rc

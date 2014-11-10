# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Steps.ui'
#
# Created: Sun Nov 02 21:57:42 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
from Archivos import creartxt, grabartxt, leerultimotxt
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

class Steps(QtGui.QMainWindow):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(546, 534)
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
        self.pbCerrar = QtGui.QPushButton(self.centralwidget)
        self.pbCerrar.setGeometry(QtCore.QRect(220, 450, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbCerrar.setFont(font)
        self.pbCerrar.setObjectName(_fromUtf8("pbCerrar"))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Pasos para resolver la ecuacion", None))
        self.pbCerrar.setText(_translate("MainWindow", "Cerrar", None))
        
    def limpiarHistorial(self):
        self.ui.teSteps.clear()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mwindow = Steps()
    mwindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlgoritmosV.ui'
#
# Created: Wed Dec 10 19:46:44 2014
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
        MainWindow.resize(907, 474)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 70, 811, 241))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(_fromUtf8(" QTabBar::tab {\n"
"    min-height: 24px;\n"
"border-top: 1px solid palette(mid);\n"
"border-left: 1px solid palette(mid);\n"
"border-bottom: 0px;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"margin-top: -1px;\n"
"margin-right: 4px;\n"
"padding-left: 5px;\n"
"background: rgb(210, 221, 239);\n"
" }\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"     border-color: #9B9B9B;\n"
"     border-bottom-color: #C2C7CB; /* same as pane color */\n"
" }\n"
"\n"
" QTabBar::tab:!selected {\n"
"     margin-top: 2px; /* make non-selected tabs look smaller */\n"
" }"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab0 = QtGui.QWidget()
        self.tab0.setObjectName(_fromUtf8("tab0"))
        self.chBiseccion = QtGui.QRadioButton(self.tab0)
        self.chBiseccion.setGeometry(QtCore.QRect(20, 30, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chBiseccion.setFont(font)
        self.chBiseccion.setObjectName(_fromUtf8("chBiseccion"))
        self.chNewton = QtGui.QRadioButton(self.tab0)
        self.chNewton.setGeometry(QtCore.QRect(20, 90, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chNewton.setFont(font)
        self.chNewton.setObjectName(_fromUtf8("chNewton"))
        self.chSecante = QtGui.QRadioButton(self.tab0)
        self.chSecante.setGeometry(QtCore.QRect(20, 150, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chSecante.setFont(font)
        self.chSecante.setObjectName(_fromUtf8("chSecante"))
        self.chFalsa = QtGui.QRadioButton(self.tab0)
        self.chFalsa.setGeometry(QtCore.QRect(400, 30, 381, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chFalsa.setFont(font)
        self.chFalsa.setObjectName(_fromUtf8("chFalsa"))
        self.chMuller = QtGui.QRadioButton(self.tab0)
        self.chMuller.setGeometry(QtCore.QRect(400, 90, 381, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chMuller.setFont(font)
        self.chMuller.setObjectName(_fromUtf8("chMuller"))
        self.tabWidget.addTab(self.tab0, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.chLagrage = QtGui.QRadioButton(self.tab1)
        self.chLagrage.setGeometry(QtCore.QRect(20, 70, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chLagrage.setFont(font)
        self.chLagrage.setObjectName(_fromUtf8("chLagrage"))
        self.chPolinomialNewton = QtGui.QRadioButton(self.tab1)
        self.chPolinomialNewton.setGeometry(QtCore.QRect(340, 50, 471, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chPolinomialNewton.setFont(font)
        self.chPolinomialNewton.setObjectName(_fromUtf8("chPolinomialNewton"))
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.chPuntoFijo = QtGui.QRadioButton(self.tab2)
        self.chPuntoFijo.setGeometry(QtCore.QRect(30, 30, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chPuntoFijo.setFont(font)
        self.chPuntoFijo.setObjectName(_fromUtf8("chPuntoFijo"))
        self.chInTrapecio = QtGui.QRadioButton(self.tab2)
        self.chInTrapecio.setGeometry(QtCore.QRect(30, 100, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chInTrapecio.setFont(font)
        self.chInTrapecio.setObjectName(_fromUtf8("chInTrapecio"))
        self.chInSimpson = QtGui.QRadioButton(self.tab2)
        self.chInSimpson.setGeometry(QtCore.QRect(410, 10, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chInSimpson.setFont(font)
        self.chInSimpson.setObjectName(_fromUtf8("chInSimpson"))
        self.chInGauss = QtGui.QRadioButton(self.tab2)
        self.chInGauss.setGeometry(QtCore.QRect(410, 100, 391, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chInGauss.setFont(font)
        self.chInGauss.setObjectName(_fromUtf8("chInGauss"))
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.tab3 = QtGui.QWidget()
        self.tab3.setObjectName(_fromUtf8("tab3"))
        self.chSolucionEuler = QtGui.QRadioButton(self.tab3)
        self.chSolucionEuler.setGeometry(QtCore.QRect(30, 30, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chSolucionEuler.setFont(font)
        self.chSolucionEuler.setObjectName(_fromUtf8("chSolucionEuler"))
        self.checkBox = QtGui.QRadioButton(self.tab3)
        self.checkBox.setGeometry(QtCore.QRect(30, 90, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.chSistemasRunge = QtGui.QRadioButton(self.tab3)
        self.chSistemasRunge.setGeometry(QtCore.QRect(30, 150, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chSistemasRunge.setFont(font)
        self.chSistemasRunge.setObjectName(_fromUtf8("chSistemasRunge"))
        self.tabWidget.addTab(self.tab3, _fromUtf8(""))
        self.tab4 = QtGui.QWidget()
        self.tab4.setObjectName(_fromUtf8("tab4"))
        self.chEliGauss = QtGui.QRadioButton(self.tab4)
        self.chEliGauss.setGeometry(QtCore.QRect(30, 30, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chEliGauss.setFont(font)
        self.chEliGauss.setObjectName(_fromUtf8("chEliGauss"))
        self.chInversa = QtGui.QRadioButton(self.tab4)
        self.chInversa.setGeometry(QtCore.QRect(30, 90, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chInversa.setFont(font)
        self.chInversa.setObjectName(_fromUtf8("chInversa"))
        self.tabWidget.addTab(self.tab4, _fromUtf8(""))
        self.tab5 = QtGui.QWidget()
        self.tab5.setObjectName(_fromUtf8("tab5"))
        self.chDescomposicion = QtGui.QRadioButton(self.tab5)
        self.chDescomposicion.setGeometry(QtCore.QRect(20, 30, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chDescomposicion.setFont(font)
        self.chDescomposicion.setObjectName(_fromUtf8("chDescomposicion"))
        self.chRegresion = QtGui.QRadioButton(self.tab5)
        self.chRegresion.setGeometry(QtCore.QRect(20, 80, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chRegresion.setFont(font)
        self.chRegresion.setObjectName(_fromUtf8("chRegresion"))
        self.chDiferencias = QtGui.QRadioButton(self.tab5)
        self.chDiferencias.setGeometry(QtCore.QRect(20, 140, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chDiferencias.setFont(font)
        self.chDiferencias.setObjectName(_fromUtf8("chDiferencias"))
        self.tabWidget.addTab(self.tab5, _fromUtf8(""))
        self.pbHistorial = QtGui.QPushButton(self.centralwidget)
        self.pbHistorial.setGeometry(QtCore.QRect(360, 350, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbHistorial.setFont(font)
        self.pbHistorial.setStyleSheet(_fromUtf8("border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/documentation.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbHistorial.setIcon(icon1)
        self.pbHistorial.setObjectName(_fromUtf8("pbHistorial"))
        self.pbAlgoritmo = QtGui.QPushButton(self.centralwidget)
        self.pbAlgoritmo.setGeometry(QtCore.QRect(580, 350, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pbAlgoritmo.setFont(font)
        self.pbAlgoritmo.setStyleSheet(_fromUtf8("border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/calculator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAlgoritmo.setIcon(icon2)
        self.pbAlgoritmo.setObjectName(_fromUtf8("pbAlgoritmo"))
        self.pbRegresar = QtGui.QPushButton(self.centralwidget)
        self.pbRegresar.setGeometry(QtCore.QRect(140, 350, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pbRegresar.setFont(font)
        self.pbRegresar.setStyleSheet(_fromUtf8("border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbRegresar.setIcon(icon3)
        self.pbRegresar.setObjectName(_fromUtf8("pbRegresar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 907, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Seleccionar Algoritmo", None))
        self.label.setText(_translate("MainWindow", "Seleccione El Algoritmo Que Desea Probar", None))
        self.chBiseccion.setText(_translate("MainWindow", "Metodo Biseccion", None))
        self.chNewton.setText(_translate("MainWindow", "Metodo Newton", None))
        self.chSecante.setText(_translate("MainWindow", "Metodo Secante", None))
        self.chFalsa.setText(_translate("MainWindow", "Metodo de la Falsa Posicion", None))
        self.chMuller.setText(_translate("MainWindow", "Metodo de Muller", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab0), _translate("MainWindow", "Ceros", None))
        self.chLagrage.setText(_translate("MainWindow", "Interpolacion de Lagrange", None))
        self.chPolinomialNewton.setText(_translate("MainWindow", "Interpolacion Polinomial\n"
"de Newton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Interpolacion", None))
        self.chPuntoFijo.setText(_translate("MainWindow", "Metodo de Punto Fijo", None))
        self.chInTrapecio.setText(_translate("MainWindow", "Integracion Numerica:\n"
"Regla del Trapecio", None))
        self.chInSimpson.setText(_translate("MainWindow", "Integracion Numerica:\n"
"Simpsons", None))
        self.chInGauss.setText(_translate("MainWindow", "Integracion Numerica\n"
"Cuadratura:\n"
"Gauss", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Diferenciacion/Integracion", None))
        self.chSolucionEuler.setText(_translate("MainWindow", "Solucion de EDO: Metodo de Euler", None))
        self.checkBox.setText(_translate("MainWindow", "Solucion de EDO: Runge Kutta", None))
        self.chSistemasRunge.setText(_translate("MainWindow", "Sistema de EDO: Runge Kutta", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Ecuacion Diferencial Ordinaria", None))
        self.chEliGauss.setText(_translate("MainWindow", "Sistemas de Ecuaciones Por Eliminacion de Gauss", None))
        self.chInversa.setText(_translate("MainWindow", "Sistemas de Ecuaciones Mediante La Inversa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("MainWindow", "Sistemas de Ecuaciones", None))
        self.chDescomposicion.setText(_translate("MainWindow", "Descomposicion LU", None))
        self.chRegresion.setText(_translate("MainWindow", "Regresion Lineal", None))
        self.chDiferencias.setText(_translate("MainWindow", "Metodo Lineal de Diferencias Finitas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("MainWindow", "Otros", None))
        self.pbHistorial.setText(_translate("MainWindow", "Historial", None))
        self.pbAlgoritmo.setText(_translate("MainWindow", "Algoritmo", None))
        self.pbRegresar.setText(_translate("MainWindow", "Regresar", None))

import imagenes_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlgoritmosV.ui'
#
# Created: Fri Dec 12 17:01:54 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlgoritmosV.ui'
#
# Created: Fri Dec 12 17:03:47 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\manuel\Documents\ProyectoMetodos\ProyectoMetodosNumericos\ProyectoMetodosNumericos\ProyectoMetodosNumericos\Ventanas\AlgoritmosV.ui'
#
# Created: Fri Dec 12 17:06:32 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaGraficado.ui'
#
# Created: Thu Nov 13 09:13:23 2014
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
        MainWindow.resize(686, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.textbox = QtGui.QLineEdit(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(70, 20, 261, 21))
        self.textbox.setObjectName(_fromUtf8("textbox"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 46, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lowerbound = QtGui.QLineEdit(self.centralwidget)
        self.lowerbound.setGeometry(QtCore.QRect(380, 20, 71, 20))
        self.lowerbound.setObjectName(_fromUtf8("lowerbound"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 20, 46, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.upperbound = QtGui.QLineEdit(self.centralwidget)
        self.upperbound.setGeometry(QtCore.QRect(500, 20, 61, 20))
        self.upperbound.setObjectName(_fromUtf8("upperbound"))
        self.draw_button = QtGui.QPushButton(self.centralwidget)
        self.draw_button.setGeometry(QtCore.QRect(570, 20, 81, 31))
        self.draw_button.setObjectName(_fromUtf8("draw_button"))
        self.logx_cb = QtGui.QCheckBox(self.centralwidget)
        self.logx_cb.setGeometry(QtCore.QRect(20, 50, 61, 31))
        self.logx_cb.setIconSize(QtCore.QSize(30, 16))
        self.logx_cb.setObjectName(_fromUtf8("logx_cb"))
        self.logy_cb = QtGui.QCheckBox(self.centralwidget)
        self.logy_cb.setGeometry(QtCore.QRect(130, 50, 70, 31))
        self.logy_cb.setObjectName(_fromUtf8("logy_cb"))
        self.trunc_cb = QtGui.QCheckBox(self.centralwidget)
        self.trunc_cb.setGeometry(QtCore.QRect(260, 50, 101, 31))
        self.trunc_cb.setObjectName(_fromUtf8("trunc_cb"))
        self.hold_cb = QtGui.QCheckBox(self.centralwidget)
        self.hold_cb.setGeometry(QtCore.QRect(390, 50, 70, 31))
        self.hold_cb.setObjectName(_fromUtf8("hold_cb"))
        self.grid_cb = QtGui.QCheckBox(self.centralwidget)
        self.grid_cb.setGeometry(QtCore.QRect(480, 50, 70, 31))
        self.grid_cb.setObjectName(_fromUtf8("grid_cb"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 80, 631, 411))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.matplotlibwidget = MatplotlibWidget(self.widget)
        self.matplotlibwidget.setGeometry(QtCore.QRect(30, 20, 571, 371))
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        self.X_PS = QtGui.QLabel(self.centralwidget)
        self.X_PS.setGeometry(QtCore.QRect(530, 510, 46, 13))
        self.X_PS.setObjectName(_fromUtf8("X_PS"))
        self.Y_POS = QtGui.QLabel(self.centralwidget)
        self.Y_POS.setGeometry(QtCore.QRect(600, 510, 46, 13))
        self.Y_POS.setObjectName(_fromUtf8("Y_POS"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 510, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 510, 75, 23))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFILE = QtGui.QMenu(self.menubar)
        self.menuFILE.setObjectName(_fromUtf8("menuFILE"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.save_plot_action = QtGui.QAction(MainWindow)
        self.save_plot_action.setObjectName(_fromUtf8("save_plot_action"))
        self.import_data_action = QtGui.QAction(MainWindow)
        self.import_data_action.setObjectName(_fromUtf8("import_data_action"))
        self.exitAction = QtGui.QAction(MainWindow)
        self.exitAction.setObjectName(_fromUtf8("exitAction"))
        self.menuFILE.addAction(self.save_plot_action)
        self.menuFILE.addAction(self.import_data_action)
        self.menuFILE.addAction(self.exitAction)
        self.menubar.addAction(self.menuFILE.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">F(x) = </span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">MIN</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">MAX</span></p></body></html>", None))
        self.draw_button.setText(_translate("MainWindow", "PLOT", None))
        self.logx_cb.setText(_translate("MainWindow", "Log-x", None))
        self.logy_cb.setText(_translate("MainWindow", "Log-y", None))
        self.trunc_cb.setText(_translate("MainWindow", "Show negative", None))
        self.hold_cb.setText(_translate("MainWindow", "Hold", None))
        self.grid_cb.setText(_translate("MainWindow", "Grind", None))
        self.X_PS.setText(_translate("MainWindow", "TextLabel", None))
        self.Y_POS.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.menuFILE.setTitle(_translate("MainWindow", "FILE", None))
        self.save_plot_action.setText(_translate("MainWindow", "SAVE PLOT", None))
        self.import_data_action.setText(_translate("MainWindow", "IMPORT DATA", None))
        self.exitAction.setText(_translate("MainWindow", "QUIT", None))

from matplotlibwidget import MatplotlibWidget

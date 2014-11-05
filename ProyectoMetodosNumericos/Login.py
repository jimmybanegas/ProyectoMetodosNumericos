'''
Created on 2/11/2014

@author: Jimmy Ramos
'''
import sys
from PyQt4 import QtGui, QtCore
from  Ventanas.login import Ui_MainWindow

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSalir.clicked.connect(self.Salir)
        self.ui.btnConfig.clicked.connect(self.CambiarColor);
        
    def Salir(self): 
        self.close()
        
    def CambiarColor(self):
        color = QtGui.QColorDialog.getColor();
        self.setStyleSheet("background-color: "+color.name());
    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
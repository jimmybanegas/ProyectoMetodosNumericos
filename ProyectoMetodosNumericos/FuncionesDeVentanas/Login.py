'''
Created on 2/11/2014

@author: Jimmy Ramos
'''
import sys
from PyQt4 import QtGui, QtCore
from Ventanas.login import Ui_MainWindow
from Ventanas import IngresarFuncion
import Ventanas

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSalir.clicked.connect(self.Salir)
        self.ui.btnIngresar.clicked.connect(self.Ingresar)
        self.ui.btnConfig.clicked.connect(self.CambiarColor);
        
    def Salir(self): 
        self.close()
    
    def Ingresar(self): 
        self.w2 = IngresarFuncion()
        self.w2.show()
        
    def CambiarColor(self):
        color = QtGui.QColorDialog.getColor();
        self.setStyleSheet("background-color: "+color.name());
        
class IngresarFuncion(QtGui.QMainWindow,Ui_MainWindow):
        #Init
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.IngresarFuncion.Ui_MainWindow()
            self.ui.setupUi(self)
    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

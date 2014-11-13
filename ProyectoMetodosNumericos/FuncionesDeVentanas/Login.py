'''
Created on 2/11/2014

@author: Jimmy Ramos
'''
import sys
from PyQt4 import QtGui, QtCore
from Ventanas.login import Ui_MainWindow
from Ventanas import IngresarFuncion
from Ventanas import AlgoritmosV
from Ventanas import Historial
from Ventanas import Input
from Ventanas import Steps
from Ventanas import Graph
from Graficador import CutePlot
import Graficador
import Ventanas
import subprocess
from serial.tools.miniterm import console
from multiprocessing import Queue, Process

colorFondo = ""

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
        global colorFondo
        colorFondo = color.name();
        self.setStyleSheet("background-color: "+colorFondo);
        
        
class IngresarFuncion(QtGui.QMainWindow,Ui_MainWindow,Process):
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.IngresarFuncion.Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.btnBorrar.clicked.connect(self.Borrar)
            self.ui.btnContinuar.clicked.connect(self.Continuar)
            self.ui.btnEvaluar.clicked.connect(self.Evaluar)
            global colorFondo
            self.setStyleSheet("background-color: "+colorFondo);
    
    #Limpiar los datos del espacio para ingresar funciones
        def Borrar(self): 
            self.ui.lnFuncion.clear()
        
    #Continuar me lleva a la pantalla de seleccionar el algoritmo con el cual resolvera la funcion
        def Continuar(self): 
            self.w2 = ElegirAlgoritmo()
            self.w2.show()      
        
    #La funcion evaluar es la que me llevara a el grafico de la f(X) que haya ingresado
        def Evaluar(self): 
            #execfile("CutePlot.py")     
            #subprocess.call("CutePlot.py", shell=True)
            self.w2 = CutePlot.CutePlot()
            self.w2.show()           
            
class ElegirAlgoritmo(QtGui.QMainWindow,Ui_MainWindow):
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.AlgoritmosV.Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pbAlgoritmo.clicked.connect(self.EjecutarAlgoritmo)
            self.ui.pbHistorial.clicked.connect(self.VerHistorial)
            global colorFondo
            self.setStyleSheet("background-color: "+colorFondo);
            
        def EjecutarAlgoritmo(self): 
            self.w2 = Input()
            self.w2.show()     

        def VerHistorial(self): 
            self.w2 = Historial()
            self.w2.show()        

class Historial(QtGui.QMainWindow,Ui_MainWindow):
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.Historial.Ui_mainWindow()
            self.ui.setupUi(self)
            self.ui.btnRegresar.clicked.connect(self.Regresar)
            global colorFondo
            self.setStyleSheet("background-color: "+colorFondo);
        
        def Regresar(self): 
            self.close()                
        
            
class Graph(QtGui.QMainWindow,Ui_MainWindow):
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.Graph.Ui_MainWindow()
            self.ui.setupUi(self)
            global colorFondo
            self.setStyleSheet("background-color: "+colorFondo);
            self.ui.btnVerPasos.clicked.connect(self.VerPasos)
        
        def VerPasos(self): 
            self.w2 = Steps()
            self.w2.show()                             

class Steps(QtGui.QMainWindow,Ui_MainWindow):
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.Steps.Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.btnCerrar.clicked.connect(self.Cerrar)
            global colorFondo
            self.setStyleSheet("background-color: "+colorFondo);
          
        def Cerrar(self): 
            self.close()               
            
class Input(QtGui.QMainWindow,Ui_MainWindow):
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.Input.Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pbCalculate.clicked.connect(self.Calcular)
            global colorFondo
            self.setStyleSheet("background-color: "+colorFondo);
            
        def Calcular(self): 
            self.w2 = Graph()
            self.w2.show()                 
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

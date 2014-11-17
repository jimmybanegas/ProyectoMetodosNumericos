'''
Created on 2/11/2014

@author: Jimmy Ramos
'''
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
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
from serial.tools.miniterm import console

colorFondo = ""
metodoSeleccionado =""
funcion = ""

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
        self.close()           
        
    def CambiarColor(self):
        color = QtGui.QColorDialog.getColor();
        global colorFondo
        colorFondo = color.name();
        self.setStyleSheet("background-color: "+colorFondo);
        
        
class IngresarFuncion(QtGui.QMainWindow,Ui_MainWindow):
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.IngresarFuncion.Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.btnBorrar.clicked.connect(self.Borrar)
            self.ui.btnContinuar.clicked.connect(self.Continuar)
            self.ui.btnEvaluar.clicked.connect(self.Evaluar)
            self.ui.btnSalir.clicked.connect(self.Salir)
            global colorFondo
            global metodoSeleccionado
            self.setStyleSheet("background-color: "+colorFondo);
            #self.ui.graphLayout.addWidget()
    
    #Limpiar los datos del espacio para ingresar funciones
        def Borrar(self): 
            self.ui.lnFuncion.clear()
            
        def Salir(self): 
            self.close()     
        
    #Continuar me lleva a la pantalla de seleccionar el algoritmo con el cual resolvera la funcion
        def Continuar(self):
            if(str(self.ui.lnFuncion.text())==''):
                QMessageBox.information(self, 'Advertencia', ''' No ha ingresado datos para graficar''',QMessageBox.Ok)
            else:     
                global funcion 
                funcion = str(self.ui.lnFuncion.text())
                self.w2 = ElegirAlgoritmo()
                self.w2.show()
                self.close()      
        
    #La funcion evaluar es la que me llevara a el grafico de la f(X) que haya ingresado
        def Evaluar(self): 
            if(str(self.ui.lnFuncion.text())==''):
                QMessageBox.information(self, 'Advertencia', ''' No ha ingresado datos para graficar''',QMessageBox.Ok)
            else: 
                self.w2 = CutePlot.CutePlot()
                self.w2.textbox.setText(str(self.ui.lnFuncion.text()))
                self.w2.on_draw()
                self.w2.show()
                 
            
class ElegirAlgoritmo(QtGui.QMainWindow,Ui_MainWindow):
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.AlgoritmosV.Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pbAlgoritmo.clicked.connect(self.EjecutarAlgoritmo)
            self.ui.pbHistorial.clicked.connect(self.VerHistorial)
            self.ui.pbRegresar.clicked.connect(self.Regresar)
            global colorFondo
            global metodoSeleccionado
            self.setStyleSheet("background-color: "+colorFondo);
            
        def closeEvent(self, evnt):
            self.w2 = IngresarFuncion()
            self.w2.show()
            self.close()  
            
        def EjecutarAlgoritmo(self): 
            self.SeleccionarMetodo() 
            if(metodoSeleccionado ==''):
                QMessageBox.information(self, 'Advertencia', ''' No ha seleccioando algoritmo''',QMessageBox.Ok)
            else:                
                self.SeleccionarMetodo() 
                self.w2 = Input()
                self.w2.show()
            
        def Regresar(self): 
            self.close()
            
        def SeleccionarMetodo(self):
            global metodoSeleccionado
            if self.ui.chBiseccion.isChecked():
                metodoSeleccionado = "Biseccion"
            elif self.ui.chNewton.isChecked():
                metodoSeleccionado = "Newton" 
            elif self.ui.chSecante.isChecked():
                metodoSeleccionado = "Secante"
            elif self.ui.chFalsa.isChecked():
                metodoSeleccionado = "Falsa"
            elif self.ui.chMuller.isChecked():
                metodoSeleccionado = "Muller"
            elif self.ui.chLagrage.isChecked():
                metodoSeleccionado = "Lagrage" 
            elif self.ui.chPolinomialNewton.isChecked():
                metodoSeleccionado = "PolinomialNewton"
            elif self.ui.chCubicosNaturales.isChecked():
                metodoSeleccionado = "CubitosNaturales"
            elif self.ui.chCubicosSujetos.isChecked():
                metodoSeleccionado = "CubitosSujetos"
            elif self.ui.chPuntoFijo.isChecked():
                metodoSeleccionado = "PuntoFijo"
            elif self.ui.chDiferenciacion.isChecked():
                metodoSeleccionado = "Diferenciacion"
            elif self.ui.chInTrapecio.isChecked():
                metodoSeleccionado = "InTrapecio"
            elif self.ui.chInSimpson.isChecked():
                metodoSeleccionado = "InSimpson"
            elif self.ui.chInGauss.isChecked():
                metodoSeleccionado = "InGauss"
            elif self.ui.chSolucionEuler.isChecked():
                metodoSeleccionado = "SolucionEuler"
            elif self.ui.checkBox.isChecked():
                metodoSeleccionado = "SolucionRunge"
            elif self.ui.chSistemasRunge.isChecked():
                metodoSeleccionado = "SistemaRunge"
            elif self.ui.chEliGauss.isChecked():
                metodoSeleccionado = "EliGauss"
            elif self.ui.chEliGaussJordan.isChecked():
                metodoSeleccionado = "EliGaussJordan"
            elif self.ui.chInversa.isChecked():
                metodoSeleccionado = "Inversa"
            elif self.ui.chDescomposicion.isChecked():
                metodoSeleccionado = "Descompasicion"
            elif self.ui.chRegresion.isChecked():
                metodoSeleccionado = "Regresion"
            elif self.ui.chDiferencias.isChecked():
                metodoSeleccionado = "Diferencias"
            else:
                metodoSeleccionado = ""                                 

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
            self.ui.btnRegresar.clicked.connect(self.Regresar)
        
        def VerPasos(self): 
            self.w2 = Steps()
            self.w2.show()
            self.close() 
       
        def Regresar(self): 
            self.close() 
            self.w2 = Input()
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
            self.ui.pbRegresar.clicked.connect(self.Regresar)
            self.ui.leEquation.setText(funcion)
            self.ui.leEquation.setEnabled(False)
            global colorFondo
            global metodoSeleccionado
            self.setStyleSheet("background-color: "+colorFondo);
            if metodoSeleccionado == "Biseccion":
                self.Biseccion()                                          
            elif metodoSeleccionado == "Newton":
                self.Newton()                 
            elif metodoSeleccionado == "Secante":
                self.Secante()
            elif metodoSeleccionado == "Falsa":
                self.Falsa()
            elif metodoSeleccionado == "Muller":
                self.Muller()
            elif metodoSeleccionado == "Lagrage":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />") 
            elif metodoSeleccionado == "PolinomialNewton":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "CubitosNaturales":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "CubitosSujetos":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "PuntoFijo":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "Diferenciacion":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "InTrapecio":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "InSimpson":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "InGauss":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "SolucionEuler":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "SolucionRunge":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "SistemaRunge":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "EliGauss":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "EliGaussJordan":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "Inversa":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "Descompasicion":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "Regresion":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "Diferencias":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />") 
                
#self.ui.lbEjemplo.setPixmap(QPixmap("Ventanas\imagenes\Biseccion.JPG"))      
        
        def Biseccion(self):
            self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\biseccion.png/>")
            self.ui.lbParam1.setText("Limite inferior A")
            self.ui.lbParam2.setText("Limite superior B")
            self.ui.lbParam3.setText("Tolerancia")
            self.ui.lbParam4.setText("No. Iteraciones")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.show()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.show()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide() 
        def Newton(self):
            self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\newton.png />")
            self.ui.lbParam1.setText("Aproximacion Inicial")
            self.ui.lbParam2.setText("Tolerancia")
            self.ui.lbParam3.setText("No. Iteraciones")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.hide()
            self.ui.leParam4.hide()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide()
        def Secante(self):
            self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\secante.png />")
            self.ui.lbParam1.setText("Aproximacion Inicial P0")
            self.ui.lbParam2.setText("Aproximacion Inicial P1")
            self.ui.lbParam3.setText("Tolerancia")
            self.ui.lbParam4.setText("No. Iteraciones")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.show()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.show()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide()
        def Falsa(self):
            self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\posicionFalsa.png />")
            self.ui.lbParam1.setText("Aproximacion Inicial P0")
            self.ui.lbParam2.setText("Aproximacion Inicial P1")
            self.ui.lbParam3.setText("Tolerancia")
            self.ui.lbParam4.setText("No. Iteraciones")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.show()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.show()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide()
        def Muller(self):
            self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\muller.png />")
            self.ui.lbParam1.setText("Aproximacion Inicial 0")
            self.ui.lbParam2.setText("Aproximacion Inicial 1")
            self.ui.lbParam3.setText("Aproximacion Inicial 2")
            self.ui.lbParam4.setText("Tolerancia")
            self.ui.lbParam5.setText("No. Iteraciones")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.show()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.show()
            self.ui.lbParam5.show()
            self.ui.leParam5.show()
            
        def Calcular(self): 
            self.w2 = Graph()
            self.w2.show()
            self.close()  
        
        def Regresar(self):
            self.close()                         
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

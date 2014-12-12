'''
Created on 2/11/2014

@author: Jimmy Ramos
'''
import sys
import os
import parser
import math
from parser import ParserError
from math import *
from Archivos import *
from collections import namedtuple
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
from Algoritmos import bisection,Newton,derivPlagrange,euler_ec_dif,factocrout,FactorizacionLUMarco,falsa_posicion,Gauss,lagrangeMarco,lineal_diferencias_finitas,MatrizInversa,minimos_cuadrado,muller,puntofijo,Reduccion_Matrices_Gauss,RegresionLineal,runge_kutta_ecu_dif, secante,simpson,sistema_edo_kutta, trapezoide,Trazador_cubico_natural, lagrange_1
#from Algoritmos import Trazador_cubico_natural
from serial.tools.miniterm import console

from sqlalchemy.sql.expression import except_
from sphinx.ext.pngmath import MathExtError
from _elementtree import ParseError
import code

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
        creartxt(self)
        creartxtfunciones(self)
        
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
            self.ui.btnEvaluar.clicked.connect(self.Evaluar)
            self.ui.btnSalir.clicked.connect(self.Salir)
            self.ui.lnFuncion.setText(funcion)  
            self.ui.btnContinuar.clicked.connect(self.Continuar)                    
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
            global funcion
            funcion = str(self.ui.lnFuncion.text())     
            if  funcion != "" :
                try:
                    x=1
                    eval(funcion)
                    self.w2 = ElegirAlgoritmo()
                    self.w2.show()
                    self.close()             
                except (MathExtError,NameError) :
                    QMessageBox.information(self, 'Advertencia', ''' No ha ingresado la funcion correctamente ''',QMessageBox.Ok)
            else:
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
                self.w2.guardarImagen()
                 
            
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
            self.close()  
            
        def EjecutarAlgoritmo(self): 
            self.SeleccionarMetodo() 
            global funcion
            if(metodoSeleccionado ==''):
                QMessageBox.information(self, 'Advertencia', ''' No ha seleccioando algoritmo''',QMessageBox.Ok)
            else:
                if (self.ui.chBiseccion.isChecked() or self.ui.chNewton.isChecked() or self.ui.chSecante.isChecked() or 
                     self.ui.chFalsa.isChecked() or self.ui.chMuller.isChecked() or self.ui.chLagrage.isChecked() or
                     self.ui.chPolinomialNewton.isChecked()or self.ui.chInGauss.isChecked() or
                     self.ui.chInSimpson.isChecked() or self.ui.chPuntoFijo.isChecked() or
                     self.ui.chInTrapecio.isChecked()):
                    if funcion == "": 
                        QMessageBox.information(self, 'Advertencia', ''' Estos algoritmos nesecitan de una funcion''',QMessageBox.Ok) 
                        self.w2 = IngresarFuncion()
                        self.w2.show()
                        self.close()    
                    else:                    
                        self.SeleccionarMetodo() 
                        self.w2 = Input()
                        self.w2.show()

                else:                
                    self.SeleccionarMetodo() 
                    self.w2 = Input()
                    self.w2.show()
                    self.close()                
                
        def Regresar(self):             
            self.w2 = IngresarFuncion()
            self.w2.show()
            self.close()     
                
            
                
        def SeleccionarMetodo(self):
            global metodoSeleccionado
            if self.ui.tabWidget.currentIndex() == 0:                
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
                    
            if self.ui.tabWidget.currentIndex() == 1:                    
                if self.ui.chLagrage.isChecked():
                    metodoSeleccionado = "Lagrage" 
                elif self.ui.chPolinomialNewton.isChecked():
                    metodoSeleccionado = "PolinomialNewton"
                elif self.ui.chCubicosNaturales.isChecked():
                    metodoSeleccionado = "CubitosNaturales"
                elif self.ui.chCubicosSujetos.isChecked():
                    metodoSeleccionado = "CubitosSujetos"
                    
            if self.ui.tabWidget.currentIndex() == 2:                    
                if self.ui.chPuntoFijo.isChecked():
                    metodoSeleccionado = "PuntoFijo"
                elif self.ui.chInTrapecio.isChecked():
                    metodoSeleccionado = "InTrapecio"
                elif self.ui.chInSimpson.isChecked():
                    metodoSeleccionado = "InSimpson"
                elif self.ui.chInGauss.isChecked():
                    metodoSeleccionado = "InGauss"
                    
            if self.ui.tabWidget.currentIndex() == 3:
                if self.ui.chSolucionEuler.isChecked():
                    metodoSeleccionado = "SolucionEuler"
                elif self.ui.checkBox.isChecked():
                    metodoSeleccionado = "SolucionRunge"
                elif self.ui.chSistemasRunge.isChecked():
                    metodoSeleccionado = "SistemaRunge"
            if self.ui.tabWidget.currentIndex() == 4:                
                if self.ui.chEliGauss.isChecked():
                    metodoSeleccionado = "EliGauss"
                elif self.ui.chInversa.isChecked():
                    metodoSeleccionado = "Inversa"
            
            if self.ui.tabWidget.currentIndex() == 5:                
                if self.ui.chDescomposicion.isChecked():
                    metodoSeleccionado = "Descomposicion"
                elif self.ui.chRegresion.isChecked():
                    metodoSeleccionado = "Regresion"
                elif self.ui.chDiferencias.isChecked():
                    metodoSeleccionado = "Diferencias"                                            

        def VerHistorial(self): 
            self.w2 = Historial()
            self.w2.show()        

class Historial(QtGui.QMainWindow,Ui_MainWindow):
        funciones = []
        index = 0
        new_index = 0
        pasos = []
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.Historial.Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.btnRegresar.clicked.connect(self.Regresar)
            self.ui.btnWord.clicked.connect(self.Escribir)
            global colorFondo
            self.setStyleSheet("background-color: "+colorFondo);
            
            funciones = leerresueltos(self)
            self.ui.cbFx.addItems(funciones)  
            index = self.ui.cbFx.currentIndex()
            posiciones = leerposiciones(self)
            pasos = leerespecifico(self, posiciones[index])
            self.ui.teSteps.clear()
            for n in pasos:
                self.ui.teSteps.append(n)
            self.ui.cbFx.currentIndexChanged.connect(self.IngresarPasos)
            
            
        def IngresarPasos(self):
            index = self.ui.cbFx.currentIndex()
            posiciones = leerposiciones(self)
            pasos = leerespecifico(self, posiciones[index])
            self.ui.teSteps.clear()
            for n in pasos:
                self.ui.teSteps.append(n)
            self.ui.lblExito.setText(" ")
        
        def Regresar(self): 
            self.close()  
        
        def Escribir(self):
            texto = []
            nombre = str(self.ui.cbFx.currentIndex()+1)
            
            index = self.ui.cbFx.currentIndex()
            posiciones = leerposiciones(self)
            pasos = leerespecifico(self, posiciones[index])
            for n in pasos:
                texto.append(n)
                
            deployaword(self, texto, "Ejejercicio "+nombre)
            self.ui.lblExito.setText("Creado!")
            
            
class Graph(QtGui.QMainWindow,Ui_MainWindow):
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ventanas.Graph.Ui_MainWindow()
            self.ui.setupUi(self)
            global colorFondo
            self.setStyleSheet("background-color: "+colorFondo);
            self.ui.btnVerPasos.clicked.connect(self.VerPasos)
            self.ui.btnRegresar.clicked.connect(self.Regresar)
            self.ui.lbResult.setText(leerultimarespuesta(self))
            self.ui.lbImage.setText( "<img src=..\FuncionesDeVentanas\untitled.png />" )
            
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
            lista = leerultimotxt(self)
            for n in lista:
                self.ui.teSteps.append(n)
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
            self.ui.lbEjemplo.setStyleSheet("font: 9pt;font-family:arial")
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
                self.Lagrage() 
            elif metodoSeleccionado == "PolinomialNewton":
                self.PolinomialNewton()
            elif metodoSeleccionado == "CubitosNaturales":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "CubitosSujetos":
                self.ui.lbEjemplo.setText("<img src=..\Ventanas\imagenes\Ejemplos\system-users.png />")
            elif metodoSeleccionado == "PuntoFijo":
                self.PuntoFijo()
            elif metodoSeleccionado == "Diferenciacion":
                self.Diferenciacion()
            elif metodoSeleccionado == "InTrapecio":
                self.InTrapecio()
            elif metodoSeleccionado == "InSimpson":
                self.InSimpson()
            elif metodoSeleccionado == "InGauss":
                self.InGauss()
            elif metodoSeleccionado == "SolucionEuler":
                self.SolucionEuler()
            elif metodoSeleccionado == "SolucionRunge":
                self.SolucionRunge()
            elif metodoSeleccionado == "SistemaRunge":
                self.SistemaRunge()
            elif metodoSeleccionado == "EliGauss":
                self.EliGauss()
            elif metodoSeleccionado == "EliGaussJordan":
                self.EliGaussJordan()
            elif metodoSeleccionado == "Inversa":
                self.Inversa()
            elif metodoSeleccionado == "Descomposicion":
                self.Descomposicion()
            elif metodoSeleccionado == "Regresion":
                self.Regresion()
            elif metodoSeleccionado == "Diferencias":
                self.Diferencias() 
                
#self.ui.lbEjemplo.setPixmap(QPixmap("Ventanas\imagenes\Biseccion.JPG"))      
        def Diferencias(self):            
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"FUNCION P(X) :-2/x \n  \n"
                                      +"FUNCION Q(X) : 2/(x*x) \n  \n"
                                      +"FUNCION R(X) :(sin( log(x, e) )) / (x*x) \n  \n"
                                      +"EXTREMO A : 1 \n \n"
                                      +"EXTREMO B : 2 \n  \n"
                                      +"CONDICION DE FRONTERA A : 1 \n  \n"
                                      +"CONDICION DE FRONTERA B : 2 \n \n"
                                      +"NO. DE SUBINTERVALOS N : 10")
            
            self.ui.lbParam1.setText("Funcion P(x)")
            self.ui.lbParam2.setText("Funcion Q(x)")
            self.ui.lbParam3.setText("Funcion R(x)")
            self.ui.lbParam4.setText("Extremo a")
            self.ui.lbParam5.setText("Extremo b")
            self.ui.lbParam6.setText("condicion de frontera A")
            self.ui.lbParam7.setText("condicion de frontera B")
            self.ui.lbParam8.setText("numero de subintervalos N")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.show()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.show()
            self.ui.lbParam5.show()
            self.ui.leParam6.show()
            self.ui.leParam7.show()
            self.ui.leParam8.show()   
        def Biseccion(self):
            self.ui.lbEjemplo.clear()
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"LIMITE SUPERIOR A: -3 \n \t debe de ser de signo contrario a limite superior \n\n"
                                      +"LIMITE INFERIOR B: 3 \n \t debe de ser de signo contrario a limite inferior \n\n"
                                      +"TOLERANCIA : 0.0000001 \n  \n\n"
                                      +"NO.ITERACIONES : 100")
            
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
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def Newton(self):
            self.ui.lbEjemplo.clear()
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"APROXIMACION INICIAL : 1 \n\n"
                                      +"TOLERANCIA : 0.0000001 \n \n\n"
                                      +"NO.ITERACIONES : 100")
             
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
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def Secante(self):
            self.ui.lbEjemplo.clear()
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"APROXIMACION INICIAL P0 : 0 \n\n"
                                      +"APROXIMACION INICIAL P1: 1 \n\n"
                                      +"TOLERANCIA : 0.0000001 \n \n\n"
                                      +"NO.ITERACIONES : 100")
           
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
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def Falsa(self):
            self.ui.lbEjemplo.clear()
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"APROXIMACION INICIAL P0 : 0 \n\n"
                                      +"APROXIMACION INICIAL P1: 1 \n\n"
                                      +"TOLERANCIA : 0.0000001 \n  \n\n"
                                      +"NO.ITERACIONES : 100")
           
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
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def Muller(self):
            self.ui.lbEjemplo.clear()
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"APROXIMACION INICIAL 0 : 5 \n\n"
                                      +"APROXIMACION INICIAL 1: -5 \n\n"
                                      +"APROXIMACION INICIAL 2: 0 \n\n"
                                      +"TOLERANCIA : 0.0000001 \n  \n\n"
                                      +"NO.ITERACIONES : 100")
           
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
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def Lagrage(self):
            self.ui.lbEjemplo.setText("\t\t\t EJEMPLO \n\n"
                                      +"GRADO: 4  \n\n"
                                      +"LISTA X : [23,45,22,134,324] \n \t las 2 listas tienen el mismo numero de elementos  \n\n"
                                      +"LISTA F(X): [433,46,232,435,66] \n \t las 2 listas tienen el mismo numero de elementos \n\n"
                                      +"PUNTO A EVALUAR : 4  \n\n"
                                      )
           
            self.ui.lbParam1.setText("GRADO")
            self.ui.lbParam2.setText(" LISTA X ")
            self.ui.lbParam3.setText("LISTA F(X)")
            self.ui.lbParam4.setText("PUNTO A EVALUAR")
            self.ui.lbParam5.setText("No. Iteraciones")
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
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def PolinomialNewton(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"APROXIMACION INICIAL P0 : -1 \n\n"
                                      +"APROXIMACION INICIAL P1: 0 \n\n"
                                      +"APROXIMACION INICIAL P2: 1 \n\n"
                                      +"TOLERANCIA : 0.0000005 \n  \n\n"
                                      +"NO.ITERACIONES : 100")
           
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
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def SolucionEuler(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"FUNCION F(x,t) :x**2+t -3 \n \t debe de ser de menor al extremo B \n\n"
                                      +"Extremo A : 0 \n \t debe de ser de menor al extremo B \n\n"
                                      +"Extremo B : 2 \n \t debe de ser de mayor al extremo A \n\n"
                                      +"Condicion Inicial : 0.5 \n \t es el valor de f(A) \n\n"
                                      +"Numero Subintervalos N : 10")
            self.ui.lbParam1.setText("FUNCION F(x,t)")
            self.ui.lbParam2.setText("Extremo A")
            self.ui.lbParam3.setText("Extremo B")
            self.ui.lbParam4.setText("Condicion Inicial")
            self.ui.lbParam5.setText("Numero Subintervalos N")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.show()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.show()
            self.ui.leParam5.show()
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()  
        def InGauss(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"NUMERO DE PUNTOS A UTILIZAR : 4 \n\n"
                                      +"LIMITE INFERIOR A : -3 \n \t debe de ser menor a limite superior b \n\n"
                                      +"LIMITE SUPERIOR B : 3 \n \t debe de ser mayot a limite inferior a \n\n"
                                       )
            
            self.ui.lbParam1.setText("Matriz")
            self.ui.lbParam2.setText("Limite Inferior A")
            self.ui.lbParam3.setText("Limite Superior B")
            self.ui.lbParam4.setText("Numero Subintervalos N")
            self.ui.lbParam5.setText("No. Iteraciones")
            self.ui.leParam1.show()
            self.ui.leParam2.hide()
            self.ui.leParam3.hide()
            self.ui.leParam4.hide()
            self.ui.lbParam1.show()
            self.ui.lbParam2.hide()
            self.ui.lbParam3.hide()
            self.ui.lbParam4.hide()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide()
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide() 
        def EliGauss(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"NUMERO DE FILAS : 3 \n\n"
                                      +"NUMERO DE COLUMNAS : 3 \n\n"
                                      +"FILA 1 :3 4 6 \n \n\n"
                                      +"FILA 2 :2 4 6 \n \n\n"
                                      +"FILA 3 :3 6 8 \n \n\n"
                                       )
            self.ui.lbParam1.setText("Matriz")
            self.ui.lbParam2.setText("Numero de Columnas")
            self.ui.lbParam3.setText("Fila 1")
            self.ui.lbParam4.setText("Fila 2")
            self.ui.lbParam5.setText("Fila 3")
            self.ui.leParam1.show()
            self.ui.leParam2.hide()
            self.ui.leParam3.hide()
            self.ui.leParam4.hide()
            self.ui.lbParam1.show()
            self.ui.lbParam2.hide()
            self.ui.lbParam3.hide()
            self.ui.lbParam4.hide()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide()
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def EliGaussJordan(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"NUMERO DE FILAS : 3 \n\n"
                                      +"NUMERO DE COLUMNAS : 3 \n\n"
                                      +"FILA 1 : 2 3 5 \n \n\n"
                                      +"FILA 2 : 3 5 6 \n \n\n"
                                      +"FILA 3 : 3 5 7  \n \n\n"
                                       )
            self.ui.lbParam1.setText("Numero de Filas")
            self.ui.lbParam2.setText("Numero de Columnas")
            self.ui.lbParam3.setText("Fila 1")
            self.ui.lbParam4.setText("Fila 2")
            self.ui.lbParam5.setText("Fila 3")
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
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()    
        def Regresion(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"VALOR DE X : [[1,10,15,24,70]] \n\n"
                                      +"VALOR DE Y : [[14,23,28,37,83]] \n\n"
                                      +"X A APROXIMAR : 0  \n\n"
                                       )
            self.ui.lbParam1.setText("Valores de X")
            self.ui.lbParam2.setText("Valores de Y")
            self.ui.lbParam3.setText("X a Aproximar")
            self.ui.lbParam4.setText("Fila 2")
            self.ui.lbParam5.setText("Fila 3")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.hide()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.hide()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide()
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def Descomposicion(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"Dimension de la Matriz : 3\n\n"
                                      +"MATRIZ A: [[0,0,0,0],[0,1,3,4],[0,2,1,3],[0,4,2,1]] \n\t la matriz debe de ser de n x n \n\n"
                                      +"MATRIZ L :[[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] \n\t la matriz debe de ser de n x n  \n\n"
                                      +"MATRIZ U :[[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] \n\t la matriz debe de ser de n x n \n\n"
                                      
                                      )
            self.ui.lbParam1.setText("Dimension de la Matriz")
            self.ui.lbParam2.setText("Matriz A")
            self.ui.lbParam3.setText("Matriz L")
            self.ui.lbParam4.setText("Matriz U")
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
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def InSimpson(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"EXTREMO A: -1 \n\n"
                                      +"EXTREMO B L :5  \n\n"
                                      +"ENTERO POSITIVO : 9 \n\n"
                                      )
            self.ui.lbParam1.setText("Extremo A")
            self.ui.lbParam2.setText("Extremo B")
            self.ui.lbParam3.setText("Entesro Positivo")
            self.ui.lbParam4.setText("Matriz U")
            self.ui.lbParam5.setText("Fila 3")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.hide()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.hide()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide()
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def SolucionRunge(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"FUNCION F(x,t) : x**2+t  \n\n"
                                      +"Extremo A : -3 \n \t debe de ser de menor al extremo B \n\n"
                                      +"Extremo B : 3 \n \t debe de ser de mayor al extremo A \n\n"
                                      +"Condicion Inicial : 0 \n \t es el valor de f(A) \n\n"
                                      +"N : 10")
            
            self.ui.lbParam1.setText("FUNCION F(x,t)")
            self.ui.lbParam2.setText("Extremo A")
            self.ui.lbParam3.setText("Extremo B")
            self.ui.lbParam4.setText("Condicion Inicial")
            self.ui.lbParam5.setText("Numero de Iteraciones")
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
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()  
        def Inversa(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"MATRIZ A: [[3,4],[2,5]] \n\t la matriz debe de ser de n x n \n\n"
                                      +"MATRIZ B :[[4],[2]] \n\t la matriz debe de ser de n x 1 \n\n"
                                      )
            self.ui.lbParam1.setText("Matriz")
            self.ui.lbParam2.setText("Matriz A")
            self.ui.lbParam3.setText("Matriz B")
            self.ui.lbParam4.setText("Numero de Iteraciones")
            self.ui.lbParam5.setText("Fila 3")
            self.ui.leParam1.hide()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.hide()
            self.ui.lbParam1.hide
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.hide()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide()
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide() 
        def PuntoFijo(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"APROXIMACION INICIAL : 1 \n\n"
                                      +"TOLERANCIA : 0.0000005 \n \n\n"
                                      +"NO.ITERACIONES : 100")
            self.ui.lbParam1.setText("Aproximacion Inicial")
            self.ui.lbParam2.setText("Tolerancia")
            self.ui.lbParam3.setText("Numero Iteraciones")
            self.ui.lbParam4.setText("Numero de Iteraciones")
            self.ui.lbParam5.setText("Fila 3")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.hide()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.hide()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide()
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()  
        def InTrapecio(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"NUMERO DE TRAPECIOS : 5 \n\n"
                                      +"LIMITE INFERIOR : 1 \n \t debe de ser menor a limite superior b \n\n"
                                      +"LIMITE SUPERIOR : 2 \n \t debe de ser mayot a limite inferior a \n\n"
                                       )
            self.ui.lbParam1.setText("Numero de Trapecios")
            self.ui.lbParam2.setText("Limite Inferior")
            self.ui.lbParam3.setText("Limite Superior")
            self.ui.lbParam4.setText("Numero de Iteraciones")
            self.ui.lbParam5.setText("Fila 3")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.leParam4.hide()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            self.ui.lbParam4.hide()
            self.ui.lbParam5.hide()
            self.ui.leParam5.hide()
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        def Diferenciacion(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"GRADO: 4 \n \t numero de iteraciones\n\n"
                                      +"LISTA X : [23,45,22,134,324] \n \t las 2 listas tienen el mismo numero de elementos  \n\n"
                                      +"LISTA F(X): [433,46,232,435,66] \n \t las 2 listas tienen el mismo numero de elementos \n\n"
                                      +"X DERIVADA : 1.5  \n\n")
            self.ui.lbParam1.setText("Grado N")
            self.ui.lbParam2.setText("Lista x")
            self.ui.lbParam3.setText("Lista FX")
            self.ui.lbParam4.setText("X Derivada")
            self.ui.lbParam5.setText("Fila 3")
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
            self.ui.lbParam5.setText("")
            self.ui.lbParam6.setText("")
            self.ui.lbParam7.setText("")
            self.ui.lbParam8.setText("")
            self.ui.leParam6.hide()
            self.ui.leParam7.hide()
            self.ui.leParam8.hide()
        
        def SistemaRunge(self):
            self.ui.lbEjemplo.setText("\t\t\tEJEMPLO \n\n"
                                      +"FUNCION 1: X**2+Y**2+Z**3 \n\n"
                                      +"FUNCION 2: 2*X+Y**3+(Z) \n\n"
                                      +"X0: 2 \n\n"
                                      +"Y0 : 1  \n\n"
                                      +"Z0 : 6  \n\n"
                                      +"XF : 8  \n\n"
                                      +"N DE ITERACIONES :100")
            self.ui.lbParam1.setText("FUNCION 1:")
            self.ui.lbParam2.setText("FUNCION 2")
            self.ui.lbParam3.setText("X0")
            self.ui.lbParam4.setText("Y0")
            self.ui.lbParam5.setText("Z0")
            self.ui.lbParam6.setText("XF")
            self.ui.lbParam7.setText("Numero de Itereaciones ")
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
            self.ui.lbParam6.show()
            self.ui.leParam6.show()
            self.ui.lbParam7.show()
            self.ui.leParam7.show()
            self.ui.lbParam8.setText("")
            self.ui.leParam8.hide()    
           
        def closeEvent(self, evnt):
            self.w2 = ElegirAlgoritmo()
            self.w2.show()
            self.close()   
        
        def LlamarRespuesta(self):
            self.w2 = Graph()
            self.w2.show()    
            
        def Calcular(self): 
            lista=[]            
            if metodoSeleccionado == "Biseccion":              
                    resp=bisection.bis(str(funcion),float(str(self.ui.leParam1.text()))
                                                  ,float(str(self.ui.leParam2.text()))
                                                  ,float(str(self.ui.leParam3.text()))
                                                  ,int(str(self.ui.leParam4.text())),lista)

                    grabartxt(self, lista, str(resp), str(funcion))
                    self.w2 = Graph()
                    self.w2.show()    
                                                          
            elif metodoSeleccionado == "Newton":          
                    resp=Newton.Newt(str(funcion)
                                     ,float(str(self.ui.leParam1.text()))
                                     ,float(str(self.ui.leParam2.text()))
                                    ,int(str(self.ui.leParam3.text())),lista)
                    
                    grabartxt(self, lista, str(resp), str(funcion))
                    self.w2 = Graph()
                    self.w2.show()
                               
            elif metodoSeleccionado == "Secante":
                    resp=secante.secante(str(funcion),
                              float(str(self.ui.leParam1.text())),
                              float(str(self.ui.leParam2.text())),
                              float(str(self.ui.leParam3.text())),
                              int(str(self.ui.leParam4.text())),lista)              
        
                    grabartxt(self, lista, str(resp), str(funcion))
                    self.w2 = Graph()
                    self.w2.show()
                
            elif metodoSeleccionado == "Falsa":
                resp=falsa_posicion.pos_f(str(funcion)
                           ,float(str(self.ui.leParam1.text())),
                           float(str(self.ui.leParam2.text())),
                           float(str(self.ui.leParam3.text())),
                           int(str(self.ui.leParam4.text())),lista)

                grabartxt(self, lista, str(resp), str(funcion))
                self.w2 = Graph()
                self.w2.show()
                
            elif metodoSeleccionado == "Muller":
                resp=muller.muller(str(funcion),
                            float(str(self.ui.leParam1.text())),
                            float(str(self.ui.leParam2.text())),
                            float(str(self.ui.leParam3.text())),
                            float(str(self.ui.leParam4.text())),
                            int(str(self.ui.leParam5.text())),lista)             
        
                grabartxt(self, lista, str(resp), str(funcion))
                self.w2 = Graph()
                self.w2.show()
                
            elif metodoSeleccionado == "Lagrage":
                resp=lagrange_1.lagrange(int(str(self.ui.leParam1.text())),
                            eval(str(self.ui.leParam2.text())),
                            eval(str(self.ui.leParam3.text())),
                            float(str(self.ui.leParam4.text())),
                            lista)             
        
                grabartxt(self, lista, str(resp), str(funcion))
                self.w2 = Graph()
                self.w2.show() 
                
            elif metodoSeleccionado == "PolinomialNewton":
                self.PolinomialNewton()
                
            elif metodoSeleccionado == "CubitosNaturales":
                resp=Trazador_cubico_natural.traz_cubico_nat(str(funcion),
                            float(str(self.ui.leParam1.text())),
                            float(str(self.ui.leParam2.text())),
                            float(str(self.ui.leParam3.text())),
                            float(str(self.ui.leParam4.text())),
                            int(str(self.ui.leParam5.text())),lista)             
        
                grabartxt(self, lista, str(resp), str(funcion))
                self.w2 = Graph()
                self.w2.show()
               
            elif metodoSeleccionado == "PuntoFijo":
                 resp=puntofijo.puntoFijo(float(str(self.ui.leParam1.text())),
                            float(str(self.ui.leParam2.text())),
                            float(str(self.ui.leParam3.text())),
                            float(str(self.ui.leParam4.text())),
                            int(str(self.ui.leParam5.text())),lista)             
        
                 grabartxt(self, lista, str(resp), str(funcion))
                 self.w2 = Graph()
                 self.w2.show()
                
            elif metodoSeleccionado == "Diferenciacion":
                resp=puntofijo.puntoFijo(str(funcion),
                            float(str(self.ui.leParam1.text())),
                            float(str(self.ui.leParam2.text())),
                            float(str(self.ui.leParam3.text())),
                            float(str(self.ui.leParam4.text())),
                            int(str(self.ui.leParam5.text())),lista)             
        
                grabartxt(self, lista, str(resp), str(funcion))
                self.w2 = Graph()
                self.w2.show()
                 
            elif metodoSeleccionado == "InTrapecio":
                resp=trapezoide.reglaTrapezoide(str(funcion),
                            float(str(self.ui.leParam1.text())),
                            float(str(self.ui.leParam2.text())),
                            float(str(self.ui.leParam3.text())),
                            lista)             
        
                grabartxt(self, lista, str(resp), str(funcion))
                self.w2 = Graph()
                self.w2.show()
                
            elif metodoSeleccionado == "InSimpson":
                resp = simpson.simpson(str(funcion),
                                  float(self.ui.leParam1.text()), 
                                  float(self.ui.leParam2.text()),
                                  int(self.ui.leParam3.text()),lista)             
        
                grabartxt(self, lista, str(resp), str(funcion))
                self.w2 = Graph()
                self.w2.show()
                
            elif metodoSeleccionado == "InGauss":
                 resp = Gauss.gauss(eval(str(self.ui.leParam1.text())), lista)     
        
                 grabartxt(self, lista, str(resp), str(funcion))
                 self.w2 = Graph()
                 self.w2.show()
                
            elif metodoSeleccionado == "SolucionEuler":
                resp = euler_ec_dif.euler_ecu_dif(str(self.ui.leParam1.text()),
                                  float(str(self.ui.leParam2.text())), 
                                  float(str(self.ui.leParam3.text())),
                                  float(str(self.ui.leParam4.text())),
                                  int(str(self.ui.leParam5.text())),lista)   
                 
                grabartxt(self, lista, str(resp), str(funcion))
                self.w2 = Graph()
                self.w2.show()

                
            elif metodoSeleccionado == "SolucionRunge":
                resp = runge_kutta_ecu_dif.runge_kutta_ecu_dif(str(self.ui.leParam1.text()), 
                                           float(str(self.ui.leParam2.text())),
                                           float(str(self.ui.leParam3.text())),
                                           float(str(self.ui.leParam4.text())),
                                           float(str(self.ui.leParam5.text())),lista)
                grabartxt(self, lista, "ver pasos ", str(self.ui.leParam1.text()))
                self.w2 = Graph()
                self.w2.show()
                
            elif metodoSeleccionado == "SistemaRunge":
                 resp = sistema_edo_kutta.sistema_edo_kuta(str(funcion),
                                  float(str(self.ui.leParam1.text)), 
                                  float(str(self.ui.leParam2.text())),
                                  float(str(self.ui.leParam3.text())),
                                  float(str(self.ui.leParam4.text())),
                                  float(str(self.ui.leParam5.text())),lista)             
        
                 grabartxt(self, lista, str(resp), str(funcion))
                 self.w2 = Graph()
                 self.w2.show()
                
            elif metodoSeleccionado == "EliGauss":
                 resp = Gauss.gauss(eval(str(self.ui.leParam1.text())), lista)
        
                 grabartxt(self, lista, str(resp), str(funcion))
                 self.w2 = Graph()
                 self.w2.show()
                
            elif metodoSeleccionado == "EliGaussJordan":
                 resp = simpson(str(funcion),
                                  str(self.ui.leParam1.text()), 
                                  str(self.ui.leParam2.text()),
                                  str(self.ui.leParam3.text()),lista)             
        
                 grabartxt(self, lista, str(resp), str(funcion))
                 self.w2 = Graph()
                 self.w2.show()
                
            elif metodoSeleccionado == "Inversa":
                 resp = MatrizInversa.MatrizInversa((str(self.ui.leParam2.text())),
                                (str(self.ui.leParam3.text())),lista)             
        
                 grabartxt(self, lista, "ver pasos", str(funcion))
                 self.w2 = Graph()
                 self.w2.show()
                
            elif metodoSeleccionado == "Descomposicion":
                 resp =FactorizacionLUMarco.factorizacionLUMarco(int(self.ui.leParam1.text()), 
                                                                 str(self.ui.leParam2.text()),str(self.ui.leParam3.text()),
                                                                 str(self.ui.leParam4.text()),lista)             
        
                 grabartxt(self, lista, "ver pasos", str(funcion))
                 self.w2 = Graph()
                 self.w2.show()
                
            elif metodoSeleccionado == "Regresion":
                 resp = RegresionLineal.RegresionLineal( self.ui.leParam1.text(),
                                                         self.ui.leParam2.text(),
                                                         int(self.ui.leParam3.text()), lista)                                
                                              
                 grabartxt(self, lista, "VER PASOS", str(funcion))
                 self.w2 = Graph()
                 self.w2.show()
                
            elif metodoSeleccionado == "Diferencias":
                resp = lineal_diferencias_finitas.linealDiferenciasFinitas(str(self.ui.leParam1.text()),
                                  str(self.ui.leParam2.text()), 
                                  str(self.ui.leParam3.text()),
                                  float(str(self.ui.leParam4.text())),
                                  float(str(self.ui.leParam5.text())),
                                  float(str(self.ui.leParam6.text())),
                                  float(str(self.ui.leParam7.text())),
                                  int(str(self.ui.leParam8.text())),lista)             
                resp = "Ver Pasos"
                grabartxt(self, lista, str(resp), str(funcion))
                self.w2 = Graph()
                self.w2.show()
        
        def Regresar(self):
            self.w2 = ElegirAlgoritmo()
            self.w2.show()
            self.close()
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\manuel\Documents\ProyectoMetodos\ProyectoMetodosNumericos\ProyectoMetodosNumericos\FuncionesDeVentanas/login.ui'
#
# Created: Wed Nov 19 20:48:21 2014
#      by: PyQt4 UI code generator 4.9.6

#
# WARNING! All changes made in this file will be lost!

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\manuel\Documents\ProyectoMetodos\ProyectoMetodosNumericos\ProyectoMetodosNumericos\Ventanas/login.ui'
#
# Created: Wed Nov 19 20:49:13 2014
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
        MainWindow.resize(626, 606)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/119499456854720557funct.svg.med.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("border-image: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 551, 551))
        self.groupBox.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setStyleSheet(_fromUtf8("border-image:url(:/logo_header_jan.png)"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 14pt \"MS Shell Dlg 2\";\n"
"font: 75 16pt \"MV Boli\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setStyleSheet(_fromUtf8("border-image:url(:/119499456854720557funct.svg.med.png)"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagenes/119499456854720557funct.svg.med.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.btnSalir = QtGui.QPushButton(self.groupBox_2)
        self.btnSalir.setGeometry(QtCore.QRect(380, 20, 131, 61))
        self.btnSalir.setStyleSheet(_fromUtf8("\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" "))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/dialog-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon1)
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        self.btnConfig = QtGui.QPushButton(self.groupBox_2)
        self.btnConfig.setGeometry(QtCore.QRect(50, 20, 61, 61))
        self.btnConfig.setStyleSheet(_fromUtf8("border-image: url(:/system-software-update.png)"))
        self.btnConfig.setText(_fromUtf8(""))
        self.btnConfig.setObjectName(_fromUtf8("btnConfig"))
        self.btnIngresar = QtGui.QPushButton(self.groupBox_2)
        self.btnIngresar.setGeometry(QtCore.QRect(220, 20, 131, 61))
        self.btnIngresar.setStyleSheet(_fromUtf8("\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" "))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIngresar.setIcon(icon2)
        self.btnIngresar.setObjectName(_fromUtf8("btnIngresar"))
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Resolucion de Ecuaciones", None))
        self.label_2.setText(_translate("MainWindow", "Bienvenido al Software de resolucion de Ecuaciones", None))
        self.btnSalir.setText(_translate("MainWindow", "Salir", None))
        self.btnConfig.setToolTip(_translate("MainWindow", "<html><head/><body><p>Download aggiornamento</p></body></html>", None))
        self.btnIngresar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Installa aggiornamento</p></body></html>", None))
        self.btnIngresar.setText(_translate("MainWindow", "Ingresar", None))

#import imagenes_rc

# -*- coding: utf-8 -*-
"""
Created on Mon May  5 15:03:54 2014

@author: Juan Carlos Espinza, William Avila
"""
import sys
from PyQt4 import QtGui
from Algoritmos.bisection import bis
from Algoritmos.Newton import Newt
from Algoritmos.puntofijo import puntoFijo
from Algoritmos.falsa_posicion import pos_f
from Algoritmos.muller import muller
from Algoritmos.secante import secante
from Ventanas.visualFunctions import resetAll, hideAll

from Ventanas.mwindow import Ui_MWindow
'''from Ventanas.login import Ui_MainWindow'''
from Main2 import Main2
class Main(QtGui.QMainWindow):
        #Init
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            '''self.ui = Ui_MainWindow()'''
            self.ui = Ui_MWindow()
            self.ui.setupUi(self)
            self.ui.cboMethod.currentIndexChanged.connect(self.checkIndex) 
            self.ui.leEquation.setText("")
            self.checkIndex()
            self.ui.pbCalculate_2.clicked.connect(self.limpiarHistorial)
            self.ui.pushButtonOtros.clicked.connect(self.mWind2)
            self.w2=None            
            
        def mWind2(self):
            self.w2 = Main2()
            self.w2.show()
            self.close()             
                                   
        def limpiarHistorial(self):
            self.ui.teSteps.clear()
            
        def pushbutton_ClickedBiseccion(self):
            lista=[]
            #bis("x**2 +4*(x**2)-10",1,2,0.00005,50)
            #test=bis("2*(x**3)-4*(x**2)+4*(x)+4",-1,-2,0.00005,50)
            try:
                resp=bis(str(self.ui.leEquation.text()),float(str(self.ui.leParam1.text())),float(str(self.ui.leParam2.text())),float(str(self.ui.leParam3.text())),int(str(self.ui.leParam4.text())),lista)
                for n in lista:
                    self.ui.teSteps.append(n)
            
                self.ui.lbResult.setText(str(resp))
            except:
                self.ui.teSteps.clear()
                self.ui.teSteps.setText("Ingrese los datos corectamente")
                
                
        def pushbutton_ClickedNewton(self):
            lista=[]
            #Newton("cos(x)-x",1,0.00005,50,lista)
            try:
                resp=Newt(str(self.ui.leEquation.text()),float(str(self.ui.leParam1.text())),float(str(self.ui.leParam2.text())),int(str(self.ui.leParam3.text())),lista)
                for n in lista:
                    self.ui.teSteps.append(n)
        
                self.ui.lbResult.setText(str(resp))
            except:
                self.ui.teSteps.clear()
                self.ui.teSteps.setText("Ingrese los datos corectamente")
                
        def pushbutton_ClickedPuntoFijo(self):
            lista=[]
            try:
                resp=puntoFijo(str(self.ui.leEquation.text()),float(str(self.ui.leParam1.text())),float(str(self.ui.leParam2.text())),int(str(self.ui.leParam3.text())),lista)
                for n in lista:
                    self.ui.teSteps.append(n)
        
                self.ui.lbResult.setText(str(resp))
            except:
                self.ui.teSteps.clear()
                self.ui.teSteps.setText("Ingrese los datos corectamente")
                
        def pushbutton_ClickedFalsaPosicion(self):
            lista=[]
            try:
                resp=pos_f(str(self.ui.leEquation.text()),float(str(self.ui.leParam1.text())),float(str(self.ui.leParam2.text())),float(str(self.ui.leParam3.text())),int(str(self.ui.leParam4.text())),lista)
                for n in lista:
                    self.ui.teSteps.append(n)
        
                self.ui.lbResult.setText(str(resp))
            except:
                self.ui.teSteps.clear()
                self.ui.teSteps.setText("Ingrese los datos corectamente")
            
        def pushbutton_ClickedMuller(self):
            lista=[]
            try:
                resp=muller(str(self.ui.leEquation.text()),float(str(self.ui.leParam1.text())),float(str(self.ui.leParam2.text())),float(str(self.ui.leParam3.text())),float(str(self.ui.leParam4.text())),int(str(self.ui.leParam5.text())),lista)
                for n in lista:
                    self.ui.teSteps.append(n)
        
                self.ui.lbResult.setText(str(resp))
            except:
                self.ui.teSteps.clear()
                self.ui.teSteps.setText("Ingrese los datos corectamente")
                
        def pushbutton_ClickedSecante(self):
            lista=[]
            try:
                resp=secante(str(self.ui.leEquation.text()),float(str(self.ui.leParam1.text())),float(str(self.ui.leParam2.text())),float(str(self.ui.leParam3.text())),int(str(self.ui.leParam4.text())),lista)
                for n in lista:
                    self.ui.teSteps.append(n)
        
                self.ui.lbResult.setText(str(resp))
            except:
                self.ui.teSteps.clear()
                self.ui.teSteps.setText("Ingrese los datos corectamente")
                
                
        
        def checkIndex(self):
            index = self.ui.cboMethod.currentIndex()
            def methodBisection(self):
                resetAll(self)
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
                self.ui.pbCalculate.clicked.connect(self.pushbutton_ClickedBiseccion)
                
            def methodPuntoFijo(self):
                resetAll(self)
                self.ui.lbParam1.setText("Aproximacion Inicial")
                self.ui.lbParam2.setText("Tolerancia")
                self.ui.lbParam3.setText("No. Iteraciones")
                self.ui.leParam1.show()
                self.ui.leParam2.show()
                self.ui.leParam3.show()
                self.ui.lbParam1.show()
                self.ui.lbParam2.show()
                self.ui.lbParam3.show()
                self.ui.leParam4.hide()
                self.ui.lbParam4.hide()
                self.ui.lbParam5.hide()
                self.ui.leParam5.hide()
                self.ui.pbCalculate.clicked.connect(self.pushbutton_ClickedPuntoFijo)
               
                
            def methodNewton(self):
                resetAll(self)
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
                self.ui.pbCalculate.clicked.connect(self.pushbutton_ClickedNewton)
               
                
            def methodPosicionFalsa(self):
                resetAll(self)
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
                self.ui.pbCalculate.clicked.connect(self.pushbutton_ClickedFalsaPosicion)
                
            def methodSecante(self):
                resetAll(self)
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
                self.ui.pbCalculate.clicked.connect(self.pushbutton_ClickedSecante)
                
            def methodMuller(self):
                resetAll(self)
                self.ui.lbParam1.setText("Aproximacion Inicial 1")
                self.ui.lbParam2.setText("Aproximacion Inicial 2")
                self.ui.lbParam3.setText("Aproximacion Inicial 3")
                self.ui.lbParam4.setText("Tolerancia")
                self.ui.lbParam5.setText("No. Iteraciones")
                self.ui.leParam1.show()
                self.ui.leParam2.show()
                self.ui.leParam3.show()
                self.ui.leParam4.show()
                self.ui.leParam5.show()
                self.ui.lbParam1.show()
                self.ui.lbParam2.show()
                self.ui.lbParam3.show()
                self.ui.lbParam4.show()
                self.ui.lbParam5.show()
                self.ui.pbCalculate.clicked.connect(self.pushbutton_ClickedMuller)
            options = {
                    0 : methodBisection,
                    1 : methodPuntoFijo,
                    2 : methodNewton,
                    3 : methodSecante,
                    4 : methodPosicionFalsa,
                    5 : methodMuller
                }
            options[index](self)
            
            return index
        
              

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mwindow = Main()
    mwindow.show()

    sys.exit(app.exec_())

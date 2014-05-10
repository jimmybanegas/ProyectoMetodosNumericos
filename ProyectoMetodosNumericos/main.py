# -*- coding: utf-8 -*-
"""
Created on Mon May  5 15:03:54 2014

@author: Juan Carlos Espinza, William Avila
"""
import sys
from PyQt4 import QtGui
from bisection import bis
from Newton import Newt
from visualFunctions import resetAll, hideAll
from mwindow import Ui_MWindow

class Main(QtGui.QMainWindow):
        #Init
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ui_MWindow()
            self.ui.setupUi(self)
            self.ui.cboMethod.currentIndexChanged.connect(self.checkIndex) 
            self.ui.leEquation.setText("")
            self.checkIndex()
           
            
            
        def pushbutton_ClickedBiseccion(self):
            lista=[]
            #bis("x**2 +4*(x**2)-10",1,2,0.00005,50)
            #test=bis("2*(x**3)-4*(x**2)+4*(x)+4",-1,-2,0.00005,50)
            try:
               
                resp=bis(str(self.ui.leEquation.text()),int(str(self.ui.leParam1.text())),int(str(self.ui.leParam2.text())),float(str(self.ui.leParam3.text())),int(str(self.ui.leParam4.text())),lista)
                for n in lista:
                    self.ui.teSteps.append(n)
            
                self.ui.lbResult.setText(str(resp))
            except:
                self.ui.teSteps.clear()
                self.ui.teSteps.setText("Ingrese los datos corectamente")
                
                
        def pushbutton_ClickedNewton(self):
            lista=[]
            #Newton("cos(x)-x",1,0.00005,50,lista)
            #test=bis("2*(x**3)-4*(x**2)+4*(x)+4",-1,-2,0.00005,50)
            try:
               
                resp=Newt(str(self.ui.leEquation.text()),int(str(self.ui.leParam1.text())),float(str(self.ui.leParam2.text())),int(str(self.ui.leParam3.text())),lista)
                for n in lista:
                    self.ui.teSteps.append(n)
        
                self.ui.lbResult.setText(str(resp))
            except:
                self.ui.teSteps.clear()
                self.ui.teSteps.setText("Ingrese los datos corectamente")
              
        
      
            
            
            
        def checkIndex(self):
            index = self.ui.cboMethod.currentIndex()
            def methodBisection():
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
                
            def methodPuntoFijo():
                resetAll(self)
                self.ui.lbParam1.setText("Ecuacion Secundaria")
                self.ui.lbParam2.setText("Aproximacion Inicial")
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
               
                
            def methodNewton():
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
               
                
            def methodSecanteAndPosicionFalsa():
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
                
            def methodMuller():
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
                
                
            options = {
                0 : methodBisection,
                1 : methodPuntoFijo,
                2 : methodNewton,
                3 : methodSecanteAndPosicionFalsa,
                4 : methodSecanteAndPosicionFalsa,
                5 : methodMuller
            }
            options[index]()
            
            return index
        
              

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mwindow = Main()
    mwindow.show()
    sys.exit(app.exec_())

'''
Created on 08/05/2014

@author: William
'''
import sys
from PyQt4 import QtGui
from Algoritmos.bisection import bis
from Algoritmos.Newton import Newt
from Ventanas.mwindow import Ui_MWindow




def hideAll(self):
    self.ui.leParam1.setText("")
    self.ui.leParam2.setText("")
    self.ui.leParam3.setText("")
    self.ui.leParam4.setText("")
    self.ui.leParam5.setText("")
    self.ui.leParam1.hide()
    self.ui.leParam2.hide()
    self.ui.leParam3.hide()
    self.ui.leParam4.hide()
    self.ui.leParam5.hide()
    self.ui.lbParam1.hide()
    self.ui.lbParam2.hide()
    self.ui.lbParam3.hide()
    self.ui.lbParam4.hide()
    self.ui.lbParam5.hide() 
    self.ui.cboMethod.clearFocus()      


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
    self.ui.pbCalculate.clicked.connect(pushbutton_ClickedBiseccion)
    
def methodPuntoFijo(self):
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
    self.ui.pbCalculate.clicked.connect(pushbutton_ClickedNewton)
   
    
def methodSecanteAndPosicionFalsa(self):
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
        

   

        
    



def resetAll(self):
    self.ui.leEquation.clear()
    self.ui.leParam1.clear()
    self.ui.leParam2.clear()
    self.ui.leParam3.clear()
    self.ui.leParam4.clear()
    self.ui.leParam5.clear()
    self.ui.lbResult.clear()
    self.ui.teSteps.clear()
    
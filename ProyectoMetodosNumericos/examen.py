# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 17:02:05 2014

@author: Juan Carlos
"""
import sys
from PyQt4 import QtGui

from wlineal import Ui_WLineal
from wsimpson import Ui_WSimpson
from wRungeEdo import Ui_WRungeEdo

from runge_kutta_ecu_dif import runge_kutta_ecu_dif
from lineal_diferencias_finitas import linealDifFinitas
from simpson import simpson

class MainLineal(QtGui.QMainWindow):
        #Init
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ui_WLineal()
            self.ui.setupUi(self)
            self.ui.pbResolver.clicked.connect(self.resolver)
        
        def resolver(self):
            lista=[]
            try:
                resp = linealDifFinitas(str(self.ui.lePx.text()), str(self.ui.leQx.text()), str(self.ui.leRx.text()), float(str(self.ui.leExa.text())), float(str(self.ui.leExb.text())), float(str(self.ui.leAlpha.text())), float(str(self.ui.leBeta.text())), int(str(self.ui.leEne.text())), lista)
                
                self.ui.teResultado.append("Tabla de Resultados:")
                for n in resp:
                    self.ui.teResultado.append("x\t\ty(x)")
                    self.ui.teResultado.append(str(n[0]) + "\t\t" + str(n[1]))
            except:
                self.ui.teResultado.clear()
                self.ui.teResultado.setText("Ingrese los datos corectamente")

class MainRungeEdo(QtGui.QMainWindow):
        #Init
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ui_WRungeEdo()
            self.ui.setupUi(self)
            self.ui.pbResolver.clicked.connect(self.resolver)
            
        def resolver(self):
            lista=[]
            try:
                resp = runge_kutta_ecu_dif(str(self.ui.leExpresion.text()), float(str(self.ui.leExa.text())), float(str(self.ui.leExb.text())), float(str(self.ui.leApha.text())), int(str(self.ui.leEne.text())))
                self.ui.teResultado.append("Tabla de Resultados:")
                
                for n in resp:
                    '''                    
                    self.ui.teResultado.append("x\t\ty(x)")
                    self.ui.teResultado.append(str(n[0]) + "\t\t" + str(n[1]))
                    '''
                    self.ui.teResultado.append(str(n))
            except:
                self.ui.teResultado.clear()
                self.ui.teResultado.setText("Ingrese los datos corectamente")
                
class MainSimpson(QtGui.QMainWindow):
        #Init
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ui_WSimpson()
            self.ui.setupUi(self)
            self.ui.pbResolver.clicked.connect(self.resolver)
            
        def resolver(self):
            lista=[]
            try:
                resp = simpson(str(self.ui.leFX.text()), float(str(self.ui.leA.text())), float(str(self.ui.leB.text())), float(str(self.ui.leN.text())), lista)
                
                for n in lista:
                    self.ui.teResultado.append(n)
                self.ui.lbResultado.setText(str(resp))
                
            except:
                self.ui.teResultado.clear()
                self.ui.teResultado.setText("Ingrese los datos corectamente")
                
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mwindow = MainSimpson()
    mwindow.show()
    sys.exit(app.exec_())
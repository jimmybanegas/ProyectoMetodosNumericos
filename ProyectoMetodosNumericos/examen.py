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

import runge_kutta_ecu_dif
from lineal_diferencias_finitas import linealDifFinitas
import simpson

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
                #resp=bis(str(self.ui.leEquation.text()),float(str(self.ui.leParam1.text())),float(str(self.ui.leParam2.text())),float(str(self.ui.leParam3.text())),int(str(self.ui.leParam4.text())),lista)
                ##resp = linealDifFinitas("algo", "as", "3x", float(str(self.ui.leExa.text())), float(str(self.ui.leExb.text())), float(str(self.ui.leAlpha.text())), float(str(self.ui.leBeta.text())), int(str(self.ui.leEne.text())), lista))
                ##resp = linealDifFinitas(str(self.ui.lePx.text()), str(self.ui.leQx.text()), str(self.ui.leRx.text()), float(str(self.ui.leExa.text())), float(str(self.ui.leExb.text())), float(str(self.ui.leAlpha.text())), float(str(self.ui.leBeta.text())), int(str(self.ui.leEne.text())), lista))
                for n in resp:
                    self.ui.teResultado.append(n)
                print("nada")
            except:
                self.ui.teResultado.clear()
                self.ui.teResultado.setText("Ingrese los datos corectamente")
                
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mwindow = MainLineal()
    mwindow.show()
    sys.exit(app.exec_())
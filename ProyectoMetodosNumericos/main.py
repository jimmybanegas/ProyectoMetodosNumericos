# -*- coding: utf-8 -*-
"""
Created on Mon May  5 15:03:54 2014

@author: Juan Carlos Espinza, William Avila
"""
import sys
from PyQt4 import QtGui
from bisection import bis
from Newton import Newt
from visualFunctions import resetAll, hideAll, methodBisection, methodPuntoFijo,methodNewton, methodSecanteAndPosicionFalsa, methodSecanteAndPosicionFalsa, methodMuller
            
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
    
        def checkIndex(self):
            index = self.ui.cboMethod.currentIndex()
        
            options = {
                0 : methodBisection,
                1 : methodPuntoFijo,
                2 : methodNewton,
                3 : methodSecanteAndPosicionFalsa,
                4 : methodSecanteAndPosicionFalsa,
                5 : methodMuller
            }
            options[index](self)
            
            return index
        
              

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mwindow = Main()
    mwindow.show()
    sys.exit(app.exec_())

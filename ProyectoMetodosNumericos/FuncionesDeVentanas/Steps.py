'''
Created on 10/11/2014

@author: Jimmy Ramos
'''
import sys
from PyQt4 import QtGui, QtCore
from Ventanas.Steps import Steps


class MyApp(QtGui.QMainWindow,Steps):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Steps.__init__(self)
        self.ui = Steps()
        self.ui.setupUi(self)
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

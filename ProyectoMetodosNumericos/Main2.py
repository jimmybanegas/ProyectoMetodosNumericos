'''
Created on 15/06/2014

@author: William
'''
from mwindow2 import Ui_MainWindow
from PyQt4 import QtGui
import sys

class Main2(QtGui.QMainWindow):
        #Init
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            
if __name__ == '__main__':
   app = QtGui.QApplication(sys.argv)
   mwindow = Main2()
   mwindow.show()

   sys.exit(app.exec_())

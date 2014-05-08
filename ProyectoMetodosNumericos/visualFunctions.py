'''
Created on 08/05/2014

@author: William
'''
import sys
from PyQt4 import QtGui
from bisection import bis

from mwindow import Ui_MWindow
class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MWindow()
        self.ui.setupUi(self)
        self.ui.pbCalculate.clicked.connect(self.test)
        self.ui.cboMethod.currentIndexChanged.connect(self.checkIndex)
        self.ui.leParam1.setText("")
        self.ui.leParam2.setText("")
        self.ui.leParam3.setText("")
        self.ui.leParam4.setText("")
        self.ui.leParam5.setText("")
        self.ui.leParam6.setText("")
        self.ui.leParam7.setText("")
        self.ui.leParam8.setText("")
        self.ui.lbParam1.setText("Param1")
        self.ui.lbParam2.setText("Param2")
        self.ui.lbParam3.setText("Param3")
        self.ui.lbParam4.setText("Param4")
        self.ui.lbParam5.setText("Param5")
        self.ui.lbParam6.setText("Param6")
        self.ui.lbParam7.setText("Param7")
        self.ui.lbParam8.setText("Param8")
        self.ui.leParam1.hide()
        self.ui.leParam2.hide()
        self.ui.leParam3.hide()
        self.ui.leParam4.hide()
        self.ui.leParam5.hide()
        self.ui.leParam6.hide()
        self.ui.leParam7.hide()
        self.ui.leParam8.hide()
        self.ui.lbParam1.hide()
        self.ui.lbParam2.hide()
        self.ui.lbParam3.hide()
        self.ui.lbParam4.hide()
        self.ui.lbParam5.hide()
        self.ui.lbParam6.hide()
        self.ui.lbParam7.hide()
        self.ui.lbParam8.hide()   
        self.ui.cboMethod.clearFocus()      
        
        self.ui.leEquation.setText("")
        #self.ui.lbResult.hide()
        
        self.ui.pbCalculate.clicked.connect(self.pushbutton_Clicked)
        
        
        
        
    def pushbutton_Clicked(self):
        lista=[]
        #bis("x**2 +4*(x**2)-10",1,2,0.00005,50)
        #test=bis("2*(x**3)-4*(x**2)+4*(x)+4",-1,-2,0.00005,50)
        try:
            resp=bis(str(self.ui.leEquation.text()),int(str(self.ui.leParam1.text())),int(str(self.ui.leParam2.text())),float(str(self.ui.leParam3.text())),int(str(self.ui.leParam4.text())),lista)
        except:
            self.ui.teSteps.clear()
            self.ui.setText("Ingrese los datos corectamente")
          
           
        for n in lista:
            self.ui.teSteps.append(n)
        
        self.ui.lbResult.setText(str(resp))
        
        
    def checkIndex(self):
        index = self.ui.cboMethod.currentIndex()
        def methodBisection():
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
            
        def methodPuntoFijo():
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
            
        def methodNewton():
            self.ui.lbParam1.setText("Aproximacion Inicial")
            self.ui.lbParam2.setText("Tolerancia")
            self.ui.lbParam3.setText("No. Iteraciones")
            self.ui.leParam1.show()
            self.ui.leParam2.show()
            self.ui.leParam3.show()
            self.ui.lbParam1.show()
            self.ui.lbParam2.show()
            self.ui.lbParam3.show()
            
        def methodSecanteAndPosicionFalsa():
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
            
        def methodMuller():
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
      
        
        # def resetAll(self):
        
        
    def cleanHistory(self):
        self.ui.teSteps("")
    

        
        
    def test(self):
        
        '''
        resp=bis(str(self.ui.lineEdit.text()),int(str(self.ui.lineEdit_2.text())),int(str(self.ui.lineEdit_3.text())),float(str(self.ui.lineEdit_4.text())),int(str(self.ui.lineEdit_5.text())),lista)
        for n in lista:
            self.ui.textEditMessage.append(n)
        self.ui.lineEdit_6Repuesta.setText(str(resp))
        '''
        lista = []
        res = bis("x**2 +4*(x**2)-10",1,2,0.00005,50, lista)
        
        print(res)

        
'''
Created on Nov 16, 2014

@author: carlosa
'''

import math
from math import *
from test.test_support import temp_cwd



if __name__ == '__main__':
    print "Metodo de Regresion Lineal"
    n = int(raw_input('Ingrese el numero de datos: '))
    lx = map(int, raw_input("Ingrese los valores de x: ").split())
    ly = map(int, raw_input("Ingrese los valores de y: ").split())
    
    sumx = 0
    sumy = 0
    sumxy = 0
    sumx2 = 0
    i = 0
    
    while i < n:
        sumx = sumx + lx[i]
        sumy = sumy + ly[i]
        sumx2 = sumx2 + (lx[i]*lx[i])
        sumxy = sumxy + (lx[i]*ly[i])
        i = i + 1
        
    denominador = (sumx*sumy) - (n*sumx2)
    
    m = (sumx*sumy - n*sumxy)/denominador
    b = (sumx*sumxy - sumx2*sumy)/denominador
    
    print "m: " + str(m) + " , b: " + str(b)
    
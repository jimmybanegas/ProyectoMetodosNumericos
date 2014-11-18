'''
Created on Nov 16, 2014

@author: carlosa
'''
import math
from math import *

def IngresarMatriz ():
    

    if __name__ == '__main__':
 
        print "SISTEMAS DE ECUACIONES POR ELIMINACION DE GAUSS"
        n = int(raw_input('Ingrese el numero de filas de la matriz a reducir: '))
        m = int(raw_input('Ingrese el numero de columnas de la matriz a reducir: '))
 
    s = 0
    matrizA
    while s < n:
        sp = s + 1
        sri = "Ingrese la fila " + str(sp)
        fila = map(int, raw_input(sri).split())
        matrizA.append(fila)
        s = s + 1
    print "Reduciendo Matriz"
    i = 0
    while i < m:
        if matrizA([i,i]) == 0:
            j=i
            while j < m:
                if matrizA([j,i]) != 0:
                    temp = matrizA[j]
                    matrizA[j] = matrizA[i]
                    matrizA[i] = temp
                    j = m
                elif ((matrizA([j,i]) == 0) & (j=m)):
                    print "La matriz no se puede reducir"
                j = j + 1
        if matrizA([i,i] != 1):
            z = i
            while z < n:
                matrizA([i,z]) = (matrizA([i,z])/matrizA([i,i]))
                x = 0
                while x < m:
                    w = 0
                    while w < n:
                        if x != i:
                            if x != 0:
                                factor = (-1)*(matrizA([x,w]))
                            matrizA([x,w]) = matrizA([x,w]) + matrizA([x,w])*factor
                        w = w + 1
                    x = x + 1
                z = z + 1
        i = i + 1
    print "Proceso realizado exitosamente"    
                
 raw_input("Presione una tecla para finalizar")

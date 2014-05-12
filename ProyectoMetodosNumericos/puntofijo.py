# -*- coding: utf-8 -*-
"""
Created on Sun May 11 17:46:27 2014
Metodo de Iteracion de punto fijo como esta en el libro
@author: Jay C Espinoza
"""
from math import *
import parser
from sympy import *
#import simpy

def puntoFijo(ecuacion, p0, tol, N, lista):
    x = Symbol('x')
    def f(x):
        return eval(ecuacion)
        
    lista.append('Paso 1: tome i = 1')
    i = 1
    lista.append('Paso 2: Mientras i <= hacer pasos 3 a 6')
    while i <= N:
        lista.append("------------------ i = " + str(i) + " ------------------")
        lista.append('Paso 3: Tome p = g(p0)')
        p = float(f(p0))
        lista.append('En este caso p = ' + str(p))
        lista.append('Paso 4: Es |p - p0|  < TOL ?')
        lista.append('Es decir, es ' + str(abs(p - p0)) + ' menor que ' + str(tol) + '?')
        if(abs(p - p0) < tol):
            lista.append('Sí, si lo es, entonces:')
            lista.append('La respuesta es ' + str(p))
            return p
        lista.append('')
        i += 1
        lista.append('Paso 5: Incrementar i -> i = ' + str(i))
        lista.append('Paso 6: Redefinir p0 como p. Es decir p0 = p')
        p0 = float(p)
    lista.append('Paso 7: El metodo fracaso luego de ' + str(N) +' iteraciones')

lista=[]
puntoFijo('atanh(x)/10', 0.5749, 0.0001, 50, lista)
print(lista)

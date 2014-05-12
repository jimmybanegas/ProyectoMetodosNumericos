# -*- coding: utf-8 -*-
"""
Created on Sun May 11 22:51:30 2014

@author: Juan Carlos Espinoza
"""
#from math import *
from cmath import *
import parser
from sympy import *

def muller(ecuacion, x0,x1,x2,tol,N,lista):
    x = Symbol('x')
    
    #derivada=str(diff(ecuacion,x))
    def f(x):
        return eval(ecuacion)
        
    lista.append('Metodo de Muller')
    lista.append('Paso 1: Inicializar variables')
    h1 = x1 - x0
    lista.append('h1 = x1 - x0; h1 = ' + str(h1))
    h2 = x2 - x1
    lista.append('h2 = x2 - x1; h2 = ' + str(h2))
    s1 = (f(x1)-f(x0))/h1
    lista.append('s1 = (f(x1)-f(x0))/h1; s1 = ' + str(s1))
    s2 = (f(x2)-f(x1))/h2
    lista.append('s2 = (f(x2)-f(x1))/h2; s2 = ' + str(s2))
    d = (s2 - s1)/(h2 - h1)
    lista.append('d = (s2 - s1)/(h2 - h1); d = ' + str(d))
    i = 3
    lista.append('i = 3')
    
    lista.append('Paso 2: Mientras i <= N hacer pasos 3 al 7')
    while i <= N:
        lista.append("------------------ i = " + str(i) + " ------------------")
        b = s2 + h2*d
        lista.append('Paso 3: b = s2 + h2*d; b = ' + str(b))
        D = (b**2 - 4*f(x2)*d)**(1/2)
        lista.append('Paso 4: Es |b - D| < |b + D| ?')
        if(abs(b - D) < abs(b + D)):
            E = b + D
            lista.append('Sí, si lo es. Entonces E = b + D; E = '+ str(E))
        else:
            E = b - D
            lista.append('No, no lo es. Entonces E = b - D; E = '+ str(E))
        h = -2*f(x2)/E
        lista.append('Paso 5: h = -2*f(x2)/E; h = ' + str(h))
        p = x2 + h
        lista.append('y p = x2 + h; p = ' + str(p))
        lista.append('Paso 6: Es |h| < tol ?')
        if( abs(h) < tol):
            lista.append('Sí, si lo es. Entonces retornar p = ' + str(p))
            return p
            break
        lista.append('No, no lo es.')
        lista.append('Paso 7: Prepararse para la siguiente iteacion.')
        x0 = x1
        lista.append('Tomar x0 = x1; x0 = ' + str(x0))
        x1 = x2
        lista.append('x1 = x2; x1 = ' + str(x1))
        x2 = p
        lista.append('Tomar x2 = p; x2 = ' + str(x2))
        h1 = x1 - x0
        lista.append('h1 = x1 - x0; h1 = ' + str(h1))
        h2 = x2 - x1
        lista.append('h2 = x2 - x1; h2 = ' + str(h2))
        s1 = (f(x1)-f(x0))/h1
        lista.append('s1 = (f(x1)-f(x0))/h1; s1 = ' + str(s1))
        s2 = (f(x2)-f(x1))/h2
        lista.append('s2 = (f(x2)-f(x1))/h2; s2 = ' + str(s2))
        d = (s2 - s1)/(h2 - h1)
        lista.append('d = (s2 - s1)/(h2 - h1); d = ' + str(d))
        i += 1
        lista.append('Incrementar i; i = ' + str(i))
    lista.append('El algoritmo fallo luego de ' + str(N) + ' iteraciones.')
    return 0
'''    
lista =[]
muller('16*x**4-40*x**3+5*x**2+20*x+6',2.5,2.0,2.25,0.00001,50,lista)
for n in lista:
    print(n)
    '''
#coding=utf-8
from math import *

import parser

from sympy import *
def Newt(ecuacion,a,tol,n,lista):
    x = Symbol ('x')    
        
        
    lista.append ('METODO DE NEWTON')    
    lista.append ('Para obtener una solucion a f(x) = 0 dada la funcion diferenciable f y una aproximacion inicial p_0.')    
    lista.append (' ')    
        
    """ecuacion = raw_input('Introduzca la ecuacion a resolver en forma de funcion: f(x)= ')    
    a = float(input('Introduzca aproximacion inicial (p_0): '))    
    tol = float(input('Introduzca tolerancia: '))    
    n = int(raw_input('Introduzca el numero de iteraciones que desea realizar (i): '))    
    lista.append (' ')"""

    primera_derivada = str(diff(ecuacion, x))    
        
    def f(x):    
        return eval(ecuacion)    
    def d(x):    
        return eval(primera_derivada)    
        
    i = 1    
    P_0 = a    
        
    lista.append ("")    
    lista.append ("Paso #1")    
    lista.append ("Tome i = " + str(i))    
        
    lista.append ("")    
    lista.append ("Paso #2")    
    lista.append ("Mientras i sea menor o igual al numero de iteraciones")    
    lista.append ("Hacer los pasos 3, 4, 5 y 6")    
    lista.append ("")    
        
    while i <= n:    
        lista.append ("------------------ i = " + str(i) + " ------------------")    
                
        lista.append ("Paso #3")    
        P = P_0 - (f(P_0)/d(P_0))                lista.append (str(P)+"")
        P = float(P)    
            
           
            
        lista.append ("p = "+str(P_0)+" - ("+str(f(P_0))+"/"+str(d(P_0))+")")    
        lista.append ("p = "+str(P))    
        lista.append ("")    
            
        lista.append ("Paso #4")    
        t = abs(P - P_0)    
        lista.append ("|"+str(P)+" - "+str(P_0)+"| < "+str(tol))    
            
        if t < tol:    
            s = "VERDADERO"    
        else:    
            s = "FALSO"    
            
        lista.append (str(t)+" < "+str(tol)+" ? : "+s)    
        lista.append ("")    
        if t < tol:
            break    
        
        lista.append ("Paso #5")    
        i += 1    
        lista.append ("i = " + str(i))    
        lista.append ("")    
        
        lista.append ("Paso #6")    
        P_0 = P    
        lista.append ("p_0 = " + str(P_0))    
        lista.append ("")    
        
    if s == "VERDADERO":            return P    
        
    else:        
        lista.append ("El método fracasó luego de "+str(n)+" iteraciones")        return 0
lista=[]"""Newt("cos(x)-x",1,0.00005,50,lista)for c in lista:    print(c)"""

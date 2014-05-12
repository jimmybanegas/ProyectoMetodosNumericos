#!/usr/bin/python
import parser
import math
from math import atan,asin,acos

def pos_f(cadena,formula, p0, p1, tol, n_iter):
    cadena.append("Paso #1")
    itera = 2
    n_iter1=n_iter
    cadena.append("Tome i = "+str(itera))
    code = parser.expr(formula).compile()
    x=p0
    q0 = eval(code)
    cadena.append("q= "+str(q0))
    x=p1
    q1=eval(code)
    cadena.append("q= "+str(q1))
    cadena.append("Paso #2")
    cadena.append("Mientras  sea menor o igual ")
    cadena.append("Hacer los pasos 3, 4, 5, 6 y 7") 
    
    while itera <= n_iter:
        cadena.append("------------- i = " + str(itera) + " ------------------")
        cadena.append("Paso #3")
        cadena.append("tome p= "+str(p1)+"-"+str(q1)+"("+str(p1)+"-"+str(p0)+")"+"/("+str(q1)+"-"+str(q0)+")")
        
        pa1=float(p1-p0)
        pa2=float(q1*pa1)
        pa4=float(q1-q0)
        pa3=float(pa2/pa4)
        p=float(p1-pa3) 

        cadena.append("Paso #4")
        cadena.append("Si |"+str(p)+"-"+str(p1)+"|<"+str(tol))
        if abs(p-p1)<tol:
            cadena.append("Procedimiento terminado exitosamente")
            cadena.append("Su resultado es: "+str(p))
            print cadena
            return p
            break
        cadena.append("Paso #5")
        cadena.append("tome i="+str(itera)+"1")
        itera=itera+1
        
        x=p
        q = eval(code)
        cadena.append("q= "+str(q))
        cadena.append("Paso #6")
        cadena.append("Si q*q1<0 entonces p=p1  y q=q1")
        if (q*q1)<0:
            cadena.append("p0= "+str(p1))
            cadena.append("q0= "+str(q1))
            p0=p1
            q0=q1       
        cadena.append("Paso #7")
        cadena.append("p1= "+str(p))
        cadena.append("q1= "+str(q))
        p1=p
        q1=q
    cadena.append("El metodo Fallo sobrepaso el numero maximo de iteraciones sin encontrar respuesta.")
    return 0    

cadena=[]  
pos_f(cadena,"cos(x)-x",0.5,0.7853,0.00005,50)  
    
    
    

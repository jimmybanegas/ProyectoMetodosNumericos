#!/usr/bin/python
import parser
import math
from math import *
import sys

def simpson(formula, a, b,n,cadena):
    cadena.append("Paso #1")
    ba=b-a
    h=ba/float(n)
    i=1
    cadena.append("tome h=("+str(b)+"-"+str(a)+")/"+str(n)+"="+str(h))
    cadena.append("Paso #2")
    code = parser.expr(formula).compile()
    x=a
    fa=eval(code)
    x=b
    fb=eval(code)
    Xl0=float(fa+fb)
    cadena.append("tome Xl0="+str(Xl0))
    Xl1=0
    Xl2=0
    cadena.append("Paso#3: Para i=1....,n-1 hacer pasos 4 y 5")
    while i< n:
        cadena.append("i="+str(i))
        X=float(a+(i*h))
        cadena.append("Paso#4: Tome X="+str(a)+str(i)+"*"+str(h)+"="+str(X))
        x=X
        fx=eval(code)
        if i%2==0: 
            Xl2=float(Xl2+fx)
            cadena.append("Paso#5:  i es par , entonces: Xl2="+str(Xl2))
        else:
            Xl1=float(Xl1+fx)
            cadena.append("Paso#5:  i es impar , entonces: Xl1="+str(Xl1))
        i=i+1
    Xl=float((h*(Xl0+(2*Xl2)+(4*Xl1)))/3)
    cadena.append("Paso#6: Xl="+str(h)+"*("+str(Xl0)+"+"+"2*"+str(Xl2)+"+"+"4*"+str(Xl1)+")/3")
    cadena.append("Paso#7: Xl="+str(Xl))
    return Xl


#if __name__ == '__main__':
#    cadena=[]
 #   print (simpson("sin(x)",0,3.141592654,20,cadena))
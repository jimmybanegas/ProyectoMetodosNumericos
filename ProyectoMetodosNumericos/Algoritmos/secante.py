'''
Created on 18/10/2014

@author: Auditor3
'''
import parser
from math import acos,asin,atan,atan2,cos,sin,tan,acosh,asinh,atanh,cosh,sinh,tanh,pi,e


def secante(formula, p0, p1, tol, n_iter, lista):
    code = parser.expr(formula).compile()
    valor = None

    var = "**********Metodo Secante********** \n \n"

    var += "       *****Paso 1***** \n"
    itera = 2
    var +=  "Tome i = "+str(itera) + "\n"
    x = p0
    q0 = eval(code)
    var += "Q0 = " + str(q0) + "\n"
    x = p1
    q1 = eval(code)    
    var += "Q1 = " + str(q1) + "\n" + "\n"
    var += "        *****Paso 2*****" + "\n"
    var += "Mientras i <= a " + str(n_iter) + "\n" 
    var += "Hacer los pasos del 3 al 6" + "\n" + "\n" 

    while itera <= n_iter:
        var += "------------- i = " + str(itera) + " ------------------" + "\n"
        var += "         *****Paso 3*****" + "\n"
        p = p1-((q1*(p1-p0))/(q1-q0))
#        if(p == valor):
#            var += "p = " + str(p)
#            break
        valor = p
        var += "      p = " + str(p) + "\n" + "\n"

        var += "         *****Paso 4*****" + "\n"
        if(abs(p-p1) < tol):
            var += "Procedimiento terminado satisfactoriamente  despues de " + str(itera) + " iteracion(es)" + "\n"
            var += "Con resultado : " + str(p) + "\n"
            lista.append(var)
            return p
        else:
            var += "      FALSO" + "\n"    
            var += "         *****Paso 5*****" + "\n"
            itera  = itera +1
            var += "      i = " + str(itera-1) + "+1=" + str(itera)     + "\n" + "\n"

            var += "         *****Paso 6*****" + "\n"
            p0 = p1
            var += "      P0 = " + str(p1) + "\n"    

            q0 = q1
            var += "      Q0 = " + str(q1) + "\n"
            p1 = p
            var += "      P1 = " + str(p)  + "\n"
            x = p
            var += "      x = " + str(p) + "\n"
            q1 = eval(code)
            var += "      Q1 = " + str(q1) + "\n" + "\n" 
    var += "Metodo Fallo" + "\n"
    lista.append(var)
    return p
'''
        
print "Ingrese ecuacion: "
ecua = str(raw_input())
print "Ingrese aprox inicial P0: "
p0 = float(raw_input())    
print "Ingrese aprox inicial P1: "
p1 = float(raw_input())
print "Ingrese tolerancia: "
tol = float(raw_input())
print "Ingrese total de iteraciones: "
ite = int(raw_input())

print secante("cos(x)-x",1,2.0,0.00005,50)
print secante(ecua,p0,p1,tol,ite)

'''
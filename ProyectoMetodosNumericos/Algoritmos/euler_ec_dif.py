import parser
import math
from math import *
from array import *

def euler_ecu_dif(formula, a, b, alfa, N, lista):
    
    code = parser.expr(formula).compile()
    h = float((b - a))/N
    t = a
    x = alfa
    t_list=[t]
    x_list=[x]

    itera = 1
    lista.append( "f(t,x)")
    lista.append("f("+str(t)+","+str(x)+")")

    lista.append("Paso #2")
    lista.append("Mientras i sea menor o igual al numero de iteraciones" )
    lista.append("Hacer los pasos 3, 4, 5 x 6")
    while itera <= N:
        lista.append("------------- i = " + str(itera) + " ------------------")

        lista.append("Paso #3")
        fun_x_t = eval(code)
        x = x + h * fun_x_t
        t = a + itera*h

        fun_x_t = eval(code)

        t_list.append(t)
        x_list.append(x)
        
        lista.append("f(t,x)")
        lista.append("f("+str(t)+","+str(x)+")")
        
        itera = itera+1
    lista.append("------------- RESULTADOS ------------------")
    lista.append("\tf(t,x)")
    for i in range(len(t_list)):
        lista.append("\tf("+str(t_list[i])+","+str(x_list[i])+")")
    
    return fun_x_t
#lista = []
#euler_ecu_dif("x - t**2 + 1",0,2,0.5,10, lista)
#for c in lista:
#    print c

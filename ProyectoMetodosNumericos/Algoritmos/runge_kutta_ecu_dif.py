import parser
import math
from math import *

def runge_kutta_ecu_dif(formula, a, b, alfa, N,lista):
  
    h = float((b - a))/N
      
    t = a
    x = alfa

    t_list=[t]
    x_list=[x]
    
    funcion = parser.expr(formula).compile()
    
    itera = 1
    lista.append("f(t,x) ")
    lista.append ("f("+str(t)+","+str(x)+")")

    lista.append ("Paso #2")
    lista.append("Mientras i sea menor o igual al numero de iteraciones" )
    lista.append ("Hacer los pasos 3, 4, 5 x 6" )
    while itera <= N:
        lista.append ("------------- i = " + str(itera) + " ------------------")
        t_bak = t
        x_bak = x

        lista.append("Paso #3")
        fun_t_x = eval(funcion)
        k_1 = h * fun_t_x

        t = t_bak+float(h)/2
        x = x_bak+float(k_1)/2
        fun_t_x = eval(funcion)
        k_2 = h * fun_t_x
        
        t = t_bak+float(h)/2
        x = x_bak+float(k_2)/2
        fun_t_x = eval(funcion)
        k_3 = h * fun_t_x

        t = t_bak+ h
        x = x_bak+ k_3
        fun_t_x = eval(funcion)
        k_4 = h * fun_t_x

        x = x_bak + float((k_1 + 2*k_2 + 2*k_3 + k_4 ))/6
        t = a + itera * h

        t_list.append(t)
        x_list.append(x)

        lista.append ("f(t,x)")
        lista.append ("f("+str(t)+","+str(x)+")")
        itera = itera+1

    lista.append("------------- RESULTADOS ------------------")
    lista.append ("\tf(t,w)")
    for i in range(len(t_list)):
        lista.append("\tf("+str(t_list[i])+","+str(x_list[i])+")")

    return lista



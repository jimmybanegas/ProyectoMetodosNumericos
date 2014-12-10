import parser
import math
from math import *

def sistema_edo_kuta(formula,formula2,x0,y0,z0,xf,N,lista):
    
    funcion = parser.expr(formula).compile()
    funcion2 = parser.expr(formula2).compile()
    h = float((xf - x0))/N
    x=x0
    y=y0
    z=z0
    
    y_list=[y]
    z_list=[z]
    
    itera = 1
    lista.append("f(x,y,z)")
    lista.append ("f("+str(x)+","+str(y)+","+str(z)+")")

    lista.append ("Paso #2")
    lista.append("Mientras i sea menor o igual al numero de iteraciones" )
    lista.append ("Hacer los pasos 3, 4, 5 x 6" )
    while itera <= N:
        lista.append ("------------- i = " + str(itera) + " ------------------")
        x_bak = x
        y_bak = y
        z_bak = z

        lista.append("Paso #3")
        fun_x_y_z = eval(funcion)
        k_1 = fun_x_y_z

        fun2_x_y_z = eval(funcion2)
        c_1 = fun2_x_y_z
        
        x = x_bak+float(h)/2
        y = y_bak+(float(k_1)/2)*k_1
        z=  z_bak+(float(k_1)/2)*c_1
        fun_x_y_z = eval(funcion)
        k_2 = fun_x_y_z
        
        fun2_x_y_z = eval(funcion2)
        c_2 = fun2_x_y_z
        
        x = x_bak+float(h)/2
        y = y_bak+(float(k_1)/2)*k_2
        z=  z_bak+(float(k_1)/2)*c_2
        fun_x_y_z = eval(funcion)
        k_3 = fun_x_y_z
        
        fun2_x_y_z = eval(funcion2)
        c_3 = fun2_x_y_z
        
        
        x = x_bak+float(h)/2
        y = y_bak+(float(k_1)/2)*k_3
        z=  z_bak+(float(k_1)/2)*c_3
        fun_x_y_z = eval(funcion)
        k_4 = fun_x_y_z
        
        fun2_x_y_z = eval(funcion2)
        c_4 = fun2_x_y_z
        
        y = y_bak+float(h)/6*(k_1+2*k_2+2*k_3+k_4)
        z = z_bak+float(h)/6*(c_1+2*c_2+2*c_3+c_4)
        x = x+float(h)
        
        y_list.append(y)
        z_list.append(z)

        lista.append ("f(t,x)")
        lista.append ("f("+str(x)+","+str(y)+","+str(z)+")")
        itera = itera+1

    lista.append("------------- RESULTADOS ------------------")
    lista.append ("\tf(t,w)")
    for i in range(len(y_list)):
        print ("\tf("+str(y_list[i])+","+str(z_list[i])+")")

    return y_list


    
    # Print input # Calculate solution

 
 

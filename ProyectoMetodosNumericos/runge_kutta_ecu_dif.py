import parser
import math
from math import cos

def runge_kutta_ecu_dif(formula, a, b, alfa, N):
    
    funcion = parser.expr(formula).compile()
    h = float((b - a))/N
    t = a
    x = alfa

    t_list=[t]
    x_list=[x]

    itera = 1
    print "f(t,x) "
    print "f("+str(t)+","+str(x)+")"

    print "Paso #2"
    print "Mientras i sea menor o igual al numero de iteraciones" 
    print "Hacer los pasos 3, 4, 5 x 6" 
    while itera <= N:
        print "------------- i = " + str(itera) + " ------------------"
        t_bak = t
        x_bak = x

        print "Paso #3"
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

        print "f(t,x)"
        print "f("+str(t)+","+str(x)+")"
        itera = itera+1

    print "------------- RESULTADOS ------------------"
    print "\tf(t,w)"
    for i in range(len(t_list)):
        print "\tf("+str(t_list[i])+","+str(x_list[i])+")"

    return fun_t_x

runge_kutta_ecu_dif("x - t**2 + 1",0,2,0.5,10)

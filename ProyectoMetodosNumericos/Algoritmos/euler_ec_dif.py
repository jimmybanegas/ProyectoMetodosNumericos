import parser
import math
from math import *
from array import *

def euler_ecu_dif(formula, a, b, alfa, N):
    
    code = parser.expr(formula).compile()
    h = float((b - a))/N
    t = a
    x = alfa
    t_list=[t]
    x_list=[x]

    itera = 1
    print "f(t,x)"
    print "f("+str(t)+","+str(x)+")"

    print "Paso #2"
    print "Mientras i sea menor o igual al numero de iteraciones" 
    print "Hacer los pasos 3, 4, 5 x 6" 
    while itera <= N:
        print "------------- i = " + str(itera) + " ------------------"

        print "Paso #3"
        fun_x_t = eval(code)
        x = x + h * fun_x_t
        t = a + itera*h

        fun_x_t = eval(code)

        t_list.append(t)
        x_list.append(x)
        
        print "f(t,x)"
        print "f("+str(t)+","+str(x)+")"
        
        itera = itera+1
    print "------------- RESULTADOS ------------------"
    print "\tf(t,x)"
    for i in range(len(t_list)):
        print "\tf("+str(t_list[i])+","+str(x_list[i])+")"
    
    return fun_x_t

euler_ecu_dif("x - t**2 + 1",0,2,0.5,10)

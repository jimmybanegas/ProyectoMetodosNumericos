'''
Created on 13/11/2014

@author: manuel
'''
import parser
import math 
from math import *
from array import *



def linealDiferenciasFinitas(px, qx, rx, a, b, alpha, beta, N, lista):
    
    funcP = parser.expr(px).compile()
    funcQ = parser.expr(qx).compile()
    funcR = parser.expr(rx).compile()
    
    def p(x):
        return eval(funcP)
    def q(x):
        return eval(funcQ)
    def r(x):
        return eval(funcR)
    
    u = [ [ 0 for i in range(N+1) ] for j in range(3) ]
    v = [ [ 0 for i in range(N+1) ] for j in range(3) ]
    
    
    lista.append ('METODO LINEAL DE DIFERENCIAS FINITAS(METODO DEL DISPARO LINEAL)')
    
    lista.append (' ')
    
    #Paso 1
    lista.append ("Paso #1")
    
    h = float((b-a))/N 
    u[1][0] = float(alpha)
    u[2][0] = float(0)
    v[1][0] = float(0)
    v[2][0] = float(1)
    lista.append("h = "+str(h))
    lista.append("u1,0 = "+str(u[1][0]))
    lista.append("u2,0 = "+str(u[2][0]))
    lista.append("v1,0 = "+str(v[1][0]))
    lista.append("v2,0 = "+str(v[2][0]))
    
    
    lista.append ("")
    lista.append ("Paso #2")
    lista.append ("Mientras i sea menor o igual al numero de iteraciones")
    lista.append ("Hacer los pasos 3 y 4")
    lista.append ("")
    
    for i in range(N):
        lista.append ("------------------ i = " + str(i) + " ------------------")
        x = a + i*h 
        lista.append ("Paso #3")
        lista.append ("Tome x = " + str(x))
        k = [ [ 1 for l in range(3) ] for j in range(5) ]
        k[1][1] = h * u[2][i]
        k[1][2] = h*( p(x) * u[2][i] + q(x) * u[1][i] + r(x))
        k[2][1] = h * (u[2][i] + 0.5 * k[1][2])
        k[2][2] = h*(p(x + h/2) * (u[2][i] + 0.5*k[1][2])
                     + q(x + h/2) * (u[1][i] + 0.5*k[1][1]) + r(x + h/2))
        k[3][1] = h* (u[2][i] + 0.5*k[2][2])
        k[3][2] = h* (p(x + h/2) * (u[2][i] + 0.5*k[2][2]) 
                     + q(x + h/2) * (u[1][i] + 0.5*k[2][1]) + r(x + h/2))
        k[4][1] = h* (u[2][i] + k[3][2])
        k[4][2] = h* (p(x + h) * (u[2][i] + k[3][2]) 
                     + q(x + h) * (u[1][i] + k[3][1]) + r(x + h))
        u[1][i+1] = u[1][i] + (float(1)/6)*(k[1][1] + 2*k[2][1] + 2*k[3][1] + k[4][1])
        u[2][i+1] = u[2][i] + (float(1)/6)*(k[1][2] + 2*k[2][2] + 2*k[3][2] + k[4][2])
        
        lista.append("u1,"+str(i+1)+"= "+str(u[1][i+1]))
        lista.append("u2,"+str(i+1)+" = "+str(u[2][i+1]))
        k[1][1] = h * v[2][i]
        k[1][2] = h * (p(x)*v[2][i] + q(x)*v[1][i])
        k[2][1] = h * (v[2][i] + (0.5)*k[1][2])
        k[2][2] = h * (p(x + h/2) * (v[2][i] + 0.5*k[1][2]) 
                     + q(x + h/2) * (v[1][i] + 0.5*k[1][1]))
        k[3][1] = h * (v[2][i] + (0.5)*k[2][2])
        k[3][2] = h * (p(x + h/2) * (v[2][i] + 0.5*k[2][2]) 
                     + q(x + h/2) * (v[1][i] + 0.5*k[2][1]))
        k[4][1] = h * (v[2][i] + k[3][2] )
        k[4][2] = h *(p(x + h) * (v[2][i] + k[3][2]) + q(x+h)*(v[1][i] + k[3][1]))
        v[1][i+1] = v[1][i] + (float(1)/6)*(k[1][1] + 2*k[2][1] + 2*k[3][1] + k[4][1])
        v[2][i+1] = v[2][i] + (float(1)/6)*(k[1][2] + 2*k[2][2] + 2*k[3][2] + k[4][2])
        lista.append("v1,"+str(i+1)+"= "+str(v[1][i+1]))
        lista.append("v2,"+str(i+1)+" = "+str(v[2][i+1]))
        
        
        
        
    #Paso 5
    w2 = (beta -u[1][N])/v[1][N]
    lista.append("")
    lista.append ("Paso #5")
    lista.append ("w2 = " + str(w2))
    
    #Paso 6
    W1 =  [ 0 for r in range(N+1) ]
    W2 =  [ 0 for t in range(N+1) ]
    lista.append ("")
    lista.append ("Paso #6")
    lista.append ("Mientras i sea menor o igual al numero de iteraciones")
    for i in range(N+1):
        lista.append ("------------------ i = " + str(i) + " ------------------")
        W1[i] = u[1][i] + w2*v[1][i]
        W2[i] = u[2][i] + w2*v[2][i]
        x = a + i*h
        lista.append ("W1 = " + str(W1[i]))
        lista.append ("W2 = " + str(W2[i]))
    
    lista.append("------------- RESULTADOS ------------------")
    lista.append("\tx \tW1 \t\tW2 \t\tu1 \t\tv1")
    for i in range(N+1):
        x = a + i*h
        lista.append("\t"+str(x)+"\t"+str(W1[i])+"\t"+str(W2[i])+"\t"+str(u[1][i])+"\t"+str(v[1][i]))
        
    for c in lista:
        print(c)

lista = []    
linealDiferenciasFinitas("-2/x","2/(x*x)","(sin( log(x, e) )) / (x*x)", 1, 2, 1, 2, 10, lista)
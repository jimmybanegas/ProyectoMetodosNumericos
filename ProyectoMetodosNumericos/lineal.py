# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 13:48:15 2014

@author: Juan Carlos
"""

#663
def linealDifFinitas(px, qx, rx, exa, exb, alpha, beta, N, lista):
    A = [0 for i in range(N+1)]
    B = [0 for i in range(N+1)]
    C = [0 for i in range(N+1)]
    D = [0 for i in range(N+1)]
    L = [0 for i in range(N+1)]
    U = [0 for i in range(N+1)]
    Z = [0 for i in range(N+1)]
    X = [0 for i in range(N+2)]
    W = [0 for i in range(N+2)]
    
    def p(x):
        return eval(px)
    def q(x):
        return eval(qx)
    def r(x):
        return eval(rx)
    
    a = exa
    b = exb
    
    h = (b - a)/(N + 1)
    x = a + h
    A[0] = 2 + h*h*q(x)
    B[0] = -1 + (h/2)*p(x)
    D[0] = -h*h*r(x) + (1 + (h/2)*p(x))*alpha
    
    for i in range(1, N - 1):
        x = a + i*h
        A[i] = 2 + h*h*q(x)
        B[i] = -1 + (h/2)*p(x)
        C[i] = -1 - (h/2)*p(x)
        D[i] = -h*h*r(x)
        
    x = b - h
    A[N-1] = 2 + h*h*q(x)
    C[N-1] = -1 - (h/2)*p(x)
    D[N-1] = -h*h*r(x) + (1 - (h/2)*p(x))*beta
    
    L[0] = A[0]
    U[0] = B[0]/A[0]
    Z[0] = D[0]/L[0]
    
    for i in range(1, N-1):
        L[i] = A[i] - C[i]*U[i-1]
        U[i] = B[i]/L[i]
        Z[i] = (D[i]-C[i]*Z[i-1])/L[i]
        
    L[N-1] = A[N-1] - C[N-1]*U[N-2]
    Z[N-1] = (D[N-1] - C[N-1]*Z[N-2])/L[N-1]
    
    W[0] = alpha
    W[N+1] = beta
    W[N] = Z[N-1]
    print(W)
    Y = [0 for i in range(N+2)]
    
    for i in range(N-1, -1 , -1):
        print("i " + str(i))
        W[i] = Z[i] - U[i]*W[i+1]
        Y[i+1] = W[i]
    print(Y)
    
    for i in range(N+2):
        X[i] = a + i*h
        #print(str(i-1) + " x, w - " + str(X[i]) + ", " + str(W[i-1])) #changed from algorithm W[i]
    
    return W
    
if(__name__ == "__main__"):
    fx = "-2/x"
    qx = "2/(x*x)"
    rx = "(sin( log(x) )) / (x*x)"
    exa = 1
    exb = 2
    alp = 1
    bet = 2
    lista = []
    N = 9 
    print( "REsult: " + str(linealDifFinitas(fx,qx,rx, exa, exb, alp, bet, N, lista)))
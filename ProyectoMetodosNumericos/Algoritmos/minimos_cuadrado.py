#!/usr/bin/python
import parser
import math
from math import *
import sys
import numpy as np

def minimos_cuadrado(n,X,Y,m,cadena):
    cadena.append("Paso #1: hacer J=0")
    M=m
    N=n
    J=0
    SS=[]
    S=[]
    B=[]
    for i in range(n+2):
       S.append(0)
    for i in range(n+1):
       SS.append(0)
    cadena.append("Paso #2: mientras J<(2*("+str(N)+"-1)) hacer pasos 3,4,5")
    while J<=(2*N-1):
        cadena.append("Paso #3: Si"+str(J)+"<"+str(N)+" hacer SS["+str(J)+"]=0")
        if J<=N:
            SS[J]=0
        else:
            cadena.append("Paso #4: hacer S["+str(J)+"]=0")
            S[J]=0
        cadena.append("Paso #5: hacer J="+str(J)+"+1")
        J=J+1
    cadena.append("Paso #6: hacer I=1")
    I=0
    cadena.append("Paso #7: mientras "+str(I)+"<"+str(M)+"hacer pasos del 8 al 15")
    while I<=M-1:
        cadena.append("Paso #8: hacer XX=1")
        XX=1
        cadena.append("Paso #9: hacer J=0")
        J=0
        cadena.append("Paso #10: mientras J<(2*("+str(N)+"-1)) hacer pasos del 11 al 14")
        while J<=(2*N-1):
            
            if J<=N:
                cadena.append("Paso #11: Si"+str(J)+"<"+str(N)+" hacer SS["+str(J)+"]="+str(SS[J])+"+"+str(XX)+"*"+str(Y[I]))
                SS[J]=SS[J]+(XX*float(Y[I]))
            
                
            cadena.append("Paso #12: hacer XX="+str(XX)+"*"+str(X[I]))
            XX=(XX*float(X[I]))
            cadena.append("Paso #13: hacer S["+str(J)+"]="+"S["+str(J)+"]+"+str(XX))
            S[J]=S[J]+float(XX)
            cadena.append("Paso #14: hacer J="+str(J)+"+")
            J=J+1
        cadena.append("Paso #15: hacer I="+str(I)+"+1")
        I=I+1
    cadena.append("Paso #16: hacer B[0,0]="+str(M))
    for i in range(N+1):
        B.append([])
        for j in range(N+2):
            B[i].append(0)
    B[0][0]=M
    cadena.append("Paso #17: hacer I=0")
    I=0
    cadena.append("Paso #18: mientras "+str(I)+"<"+str(N)+"hacer pasos del 19 al 24")
    while I<=N:
        cadena.append("Paso #19: hacer J=0")
        J=0
        cadena.append("Paso #20: mientras"+str(J)+"<"+str(N)+"hacer pasos del 21 al 22")
        while J<=N:
            if I!=0 or J!=0:
                B[I][J]=float(S[J-1+I])
            J=J+1
        B[I][N+1] = float(SS[I])
        
        I=I+1
    A=[]
    for i in range(N+1):
        A.append([])
        for j in range(M-2):
            A[i].append(0)
    for i in range(N+1):
        for j in range(M-2):
            A[i][j]=float(B[i][j])
            
    return resolver_matriz(A,SS)
   

def resolver_matriz(A,b):
    n = len(A)
    if len(b) != n:
        raise ValueError("Tamanos incompatibles entre A y b.", len(b), n)
    for pivot_row in xrange(n-1):
        for row in xrange(pivot_row+1, n):
            multiplier = A[row][pivot_row]/float(A[pivot_row][pivot_row])
            A[row][pivot_row] = multiplier
            for col in xrange(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
            b[row] = b[row] - multiplier*b[pivot_row]
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k][k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k][k+1:],x[k+1:]))/A[k][k]
        k = k-1
    return x
'''
X=[0.00,0.25,0.50,0.75,1.00]
Y=[1.000,1.2840,1.6487,2.1170,2.7183]
cadena=[]
B=[[10,1,-5],[-20,3,20],[5,3,5]]
S=[1,2,6]
resp=minimos_cuadrado(2,X,Y,5,cadena)
print resp
'''
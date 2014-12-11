# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 14:10:19 2014

@author: Marco
"""

#408
def factoCroutTridiagon(n, A, lista):
    L = [[0 for j in range(n+1)] for i in range(n) ]
    U = [[0 for j in range(n+1)] for i in range(n) ]
    Z = [0 for i in range(n) ]
    
    
    #Step 1
    L[0][0] = A[0][0]
    U[0][1] = A[0][1]/L[0][0]
    Z[0] = A[0][n]/L[0][0]
    
    for i in range(1, n-1):
        print("i -> " + str(i))
        L[i][i-1] = A[i][i-1]
        L[i][i] = A[i][i] - L[i][i-1]*U[i-1][i]
        U[i][i+1] = A[i][i+1]/L[i][i]
        Z[i] = (A[1][n]-L[i][i-1]*Z[i-1]) / L[i][i]
        
    L[n-1][n-2] = A[n-1][n-2]
    L[n-1][n-1] = A[n-1][n-1]-L[n-1][n-2]*U[n-2][n-1]
    Z[n-1] = (A[n-1][n]-L[n-1][n-2]*Z[n-2])/L[n-1][n-1]
    
    X = [0 for i in range(n)]
    X[n-1] = Z[n-1]
    
    for i in range(n-2,-1,-1):
        print(" i = " + str(i))
        X[i] = Z[i]-U[i][i+1]*X[i+1]
    
    return X;
'''
if( __name__ == "__main__"):
    arg = ([[2, -1, 0, 0, 1],
            [-1, 2, -1, 0, 0],
            [0, -1, 2, -1, 0],
            [0, 0, -1, 2, 1]])
    dim = 4
    lst = []
    
    print(factoCroutTridiagon(dim, arg, lst))
    
    print("Test Two:")
    mat = ([[3, 1, 0, -1],
            [2, 4, 1, 7],
            [0, 2, 5, 9]])
    dim = 3
    lis = []
    print(factoCroutTridiagon(dim, mat, lis))
    '''
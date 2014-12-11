# -*- coding: utf-8 -*-
"""
Algoritmo de Factorizacion LU

Created on Sat Nov 15 10:58:38 2014

@author: Marco
"""

def factorizacionLUMarco(dimensionN, matrizA, matrizL, matrizU, listaPasos):
    #Seleccionar L_11*U_11 = A_11
    listaPasos.append("#Paso 1-Seleccionar L_11*U_11 = A_11")
    if(matrizL[1][1]*matrizU[1][1] == 0):
        print("Factorizacion Fallo")
    j = 2
    
    for j in range (2, dimensionN+1):
        matrizU[1][j] = matrizA[1][j]/matrizL[1][1]
        matrizL[j][1] = matrizA[j][1]/matrizU[1][1]
        listaPasos.append("#Paso 2- para j= "+ str(j)+"  "+" tome u1j=" + str(matrizA[1][j]/matrizL[1][1]) + "   "+ "l1j=" + str(matrizA[j][1]/matrizU[1][1]))
    listaPasos.append("#Paso 3-para i=2....n-1 haga los pasos 4 y 5")
    for i in range(2, dimensionN):
        
        listaPasos.append("#Paso 4 - seleccione lii y uii satifaciendo LiiUii= sumatoria (i-1, k=1) Lik Uki ")
        if(matrizL[i][i]*matrizU[i][i] == 0):
            print("Factorizacion Imposible")
        listaPasos.append("#Paso 5 - para j=j+1 ....n tome uij= 1/lii[aij - sumatoria(i-1 ,k=1)Lik Ukj    y    lji= 1/uii[aji - sumatoria(i-1 ,k=1)Ljk Uki    ")
        for j in range(i+1, dimensionN+1):
            tempSuma = 0
            for k in range(1, i):
                tempSuma = matrizL[i][k]*matrizU[k][j]
            matrizU[i][j] = (1/matrizL[i][i])*(matrizA[i][j] - tempSuma)
            listaPasos.append("uij=" + str(matrizU[i][j]))
            for k in range(1, i):
                tempSuma = matrizL[j][k]*matrizU[k][i]
            matrizL[j][i] = (1/matrizU[i][i])*(matrizA[j][i] - tempSuma)
            listaPasos.append("lji=" + str( matrizL[j][i]))
        listaPasos.append("#Paso 6-  lnn y unn tales que lnnUnn=ann - sumatoria (n-1 , k=1) lnk Ukn")
        listaPasos.append("#Seleccionar matrizL[n][n] y matrizU[n][n] tal que matrizL[n][n]*matrizU[n][n] = 0")
        if(matrizL[dimensionN][dimensionN]*matrizU[dimensionN][dimensionN] == 0):
            print("A = LU, pero A es singular")

n = 3
mA = [[0,0,0,0],
      [0,1,3,4],
      [0,2,4,1],
      [0,3,1,1]]
mL = [[0,0,0,0],
      [0,1,0,0],
      [0,0,1,0],
      [0,0,0,1]]
mU = [[0,0,0,0],
      [0,1,0,0],
      [0,0,1,0],
      [0,0,0,1]]
pasos = []
factorizacionLUMarco(3, mA, mL, mU, pasos)
'''
for paso in pasos:
    print(paso)
    print(" ")

print("Matriz A")
for i in range(1, n+1):
    for j in range(1, n+1):
        print( mA[i][j]),
    print("")

print("Matriz L")
for i in range(1, n+1):
    for j in range(1, n+1):
        print( mL[i][j]),
    print("")
    
print("Matriz U")
for i in range(1, n+1):
    for j in range(1, n+1):
        print( mU[i][j]),
    print("")
    '''
#imprimir los pasos, para saber que hizo el algoritmo:


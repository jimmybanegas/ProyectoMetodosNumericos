# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 16:23:22 2014

@author: TECNOCOMP
"""

"""
PASO l. Hacer X = A.
 PASO 2. Hacer S = O.
 PASO 3. Hacer H = (B - A)/N.
 PASO 4. SI N = 1,ir al paso 10. De otro modo continuar. 
 PASO 5. Hacer 1 =1. 
 PASO 6. Mientras 1::; N -1, repetir los pasos 7 a 9. 
 PASO 7. Hacer X = X + H.
 PASO 8. Hacer S = S + F (X). 
 PASO 9. Hacer 1= 1+ 1. 
 PASO 10. Hacer ÁREA = H/2 * (F (A) + 2 *S + F (B)). 
 PASO 11. IMPRIMIR ÁREA Y TERMINAR.

"""
import parser

def reglaTrapezoide(  funcion,trapeciosN, limiteInferiorA , limiteSuperiorB , cadena ):
    def funcion2(x):
        return eval(funcion)      

    cadena.append("Hacer X = A.")
    X = limiteInferiorA
    cadena.append("X = limiteInferiorA")
    S = 0
    cadena.append("S =0")
    H = (float(limiteSuperiorB) - limiteInferiorA)/trapeciosN
    cadena.append("Hacer la variable H = limite Superior - Limite Inferior / Numero de Trapecios")

    if trapeciosN != 1:
        I =1
        cadena.append("Variable I = 1")
        cadena.append("Mientraz I <= Numero de Trapecios -1 hacer los siguientes pasos:")
        while I<=trapeciosN-1:
            cadena.append(str(I)+" <= "+str(trapeciosN-1))
            
            X = X + H
            cadena.append("X = X + H")
            cadena.append("X = "+str(H))
            
            S = S +funcion2(X)
            cadena.append("S = S + X")
            cadena.append("S = "+str(S))
            
            I= I+ 1
            cadena.append("I = I + 1")
            cadena.append("I = "+str(I))
            
    AREA = H/ 2 * (funcion2(limiteInferiorA) + 2 *S + funcion2(limiteSuperiorB))
    cadena.append("AREA  = H/2 * LIMITE INFERIOR + 2 * LIMITE SUPERIOR")
    return AREA
   
erick=[]
#print(str(reglaTrapezoide("x**2+2",5,1,2,erick)))
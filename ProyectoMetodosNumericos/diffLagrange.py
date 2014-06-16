# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 16:28:22 2014

@author: Juan Carlos Espinoza
"""
import numpy


def polinomioLagrange(N, xs, fs, x_d, lista):
    dp = 0
    lista.append("Paso 1. Hacer dp = 0")
    lista.append("Paso 2. Mientras i <= N repetir pasos de 3 al 20. Con i empezando en 0")
    for i in range(0, N, 1):
        print("---- i = " + str(i) + " -----")
        lista.append("Paso 3. Hacer p = 1")
        p = 1
        lista.append("Paso 4. Mientras j <= N repetir pasos 7. Con j empezando e 0")
        for j in range(0, N, 1):
            print("---- j = " + str(j) + " -----")
            lista.append("Paso 7. Comparar i con j")
            if i != j:
                lista.append("Como son diferentes entonces hacer p = p*(x(i)-x(j))")
                p = p*(xs[i] - xs[j])
        lista.append("Paso 8. Hacer s = 0")
        s = 0
        print("Paso 19. Mientras k <= N repetir pasos a . Con k empezando en 0")
        for k in range(0,N, 1):
            print("---- k = " + str(k) + " -----")
            print("Paso 10. Comparar i con K")
            if( i != k):
                print("Como son diferentes, hacer pasos al ")
                print("Paso 11. Hacer p1 = 1")
                p1 = 1
                print("Paso 12. Hacer j = 0")
                j = 0
                print("Paso 13. Mientras j <= N hacer repetir pasos al")
                while j <= N:
                    print("---- j = " + str(j) + " -----")
                    print("Paso 14. Verificar que i sea distinto que j y que j distinto que k")
                    if i != j and j != k:
                        print("Paso 15. Se cumple, entonces hacer p1 = p1*(x_d - x(j) )")
                        p1 = p1*(x_d - xs[j])
                    print("Paso 16. Incrementar j en 1")
                    j += 1
                print("Paso 17. Hacer s = s + p1")
                s = s + p1
        print("Paso 18. Hacer dp = dp + f(i)/p*s")
        dp = dp + fs[i]/p*s
    print("Resultado: " + str(dp))
    return dp

X = [1, 2, 3, 4]
Fx = [1, 4, 9, 16]
ene = 2
exd = 2.5
lista = []
polinomioLagrange(ene, X, Fx, exd, lista)

#469
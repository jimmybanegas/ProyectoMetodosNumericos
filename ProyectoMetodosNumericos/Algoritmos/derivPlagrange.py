# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 10:53:14 2014

@author: Juan Carlos
"""

def deriv_PLagrange(N, xs, fs, x_d, lista):
    lista.append("Paso 1. Hacer DP = 0")
    dp = 0
    lista.append("Paso 2. Hacer I = 0")
    i = 0
    lista.append("Paso 3. Mientras I <= N hacer pasos 4 a 21")
    while i <= N:
        lista.append("------ i = " + str(i) + " ------")
        lista.append("Paso 4. Hacer P = 1")
        p = 1
        lista.append("Paso 5. Hacer J = 0")
        j = 0
        lista.append("Paso 6. Mientras J <= N hacer pasos 7 a 8")
        while j <= N:
            lista.append("----- j = " +str(j) + " -----")
            lista.append("Paso 7. I es distinto de J?")
            if i != j:
                p = p * (xs[i] - xs[j])
                lista.append("Entonces hacer P = P *(X[I] - X[J]) = "+ str(p))
            lista.append("Paso 8. Incrementar J en uno")
            j += 1
        lista.append("Paso 9. Hacer S = 0")
        s = 0
        lista.append("Paso 10. Hacer K = 0")
        k = 0
        lista.append("Paso 11. Mientras K <= N hacer pasos 12 a 19")
        while k <= N:
            lista.append("----- k = " + str(k) + " -----")
            lista.append("Paso 12. Es I distinto que K")
            if i != k:
                lista.append("Entonces hacer pasos 13 a 18")
                lista.append("Paso 13. Hacer P1 = 1")
                p1 = 1
                lista.append("Paso 14. Hacer J = 0")
                j = 0
                lista.append("Paso 15. Mientras J <= N hacer pasos 16 y 17")
                while j <= N:
                    lista.append("---- j = " + str(j) + " ----")
                    lista.append("Paso 16. Es I distinto que J y J distinto que K?")
                    if i != j and j != k:
                        p1 = p1 *( x_d - xs[j])
                        lista.append("Entonces hacer P1 = P1*(XD - X[J] = " + str(p1))
                    lista.append("Paso 17. Incrementar J en uno")
                    j += 1
                lista.append("Paso 18. Incrementar S con P1")
                s += p1
            lista.append("Paso 19. Incrementar K en uno.")
            k += 1
        dp += fs[i]/p*s
        lista.append("Paso 20. Hacer DP = DP + FX[i]/(P*S) = " + str(dp))
        lista.append("Paso 21. Incrementar I en uno")
        i += 1
    lista.append("Paso 22. Retornar DP = " + str(dp))
    return dp
     
X = [1, 2, 3, 4]
Fx = [1, 4, 9, 16]
ene = 2
exd = 2.5
#lista = []
#print(str(deriv_PLagrange(ene, X, Fx, exd, lista)))
#for i in range(lista.__len__()):
#    print(lista[i])
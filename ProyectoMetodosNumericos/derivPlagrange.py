# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 10:53:14 2014

@author: Juan Carlos
"""

def deriv_PLagrange(N, xs, fs, x_d, lista):
    dp = 0
    i = 0
    while i <= N:
        p = 1
        j = 0
        while j <= N:
            if i != j:
                p = p * (xs[i] - xs[j])
            j += 1
        s = 0
        k = 0
        while k <= N:
            if i != k and j != k:
                p1 = 1
                j = 0
                while j <= N:
                    if i != k and j != k:
                        p1 = p1 *( x_d - xs[j])
                    j += 1
                s += p1
            k += 1
        dp += fs[i]/p*s
        i += 1
    print( str(dp))
     
X = [1, 2, 3, 4]
Fx = [1, 4, 9, 16]
ene = 2
exd = 2.5
lista = []
deriv_PLagrange(ene, X, Fx, exd, lista)
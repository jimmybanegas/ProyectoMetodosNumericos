#coding=utf-8
from math import *
from sympy import *
import parser

x = Symbol ('x')

def F(x):
    return eval(ecuacion)

ecuacion = raw_input('Introduzca la ecuación a resolver en forma de función: f(x)= ')
N = int(raw_input('Introduzca número de puntos a utilizar: N = '))
A = float(input('Introduzca límite inferior: A = '))
B = float(input('Introduzca límite superior: B = '))

NP = [0, 2, 3, 4, 5, 6]
IAUX = [0, 1, 2, 4, 6, 9, 12]
Z = [0.0, 0.577350269, 0.0, 0.774596669, 0.339981044, 0.861136312, 0.0, 0.538469310, 0.906179846, 0.238619186, 0.661209387, 0.932469514]
W = [0.0, 1.0, 0.888888888, 0.555555555, 0.652145155, 0.347854845, 0.568888888, 0.478628671, 0.236926885, 0.467913935, 0.360761573, 0.171324493]
I = 1

print
print 'PASO 1: '
print 'NP(I) = ['+str(NP[1])+', '+str(NP[2])+', '+str(NP[3])+', '+str(NP[4])+', '+str(NP[5])+']'
print
print 'PASO 2: '
print 'IAUX(I) = ['+str(IAUX[1])+', '+str(IAUX[2])+', '+str(IAUX[3])+', '+str(IAUX[4])+', '+str(IAUX[5])+', '+str(IAUX[6])+']'
print
print 'PASO 3: '
print 'Z(I) = ['+str(Z[1])+', '+str(Z[2])+', '+str(Z[3])+', '+str(Z[4])+', '+str(Z[5])+', '+str(Z[6])+', '+str(Z[7])+', '+str(Z[8])+', '+str(Z[9])+', '+str(Z[10])+', '+str(Z[11])+']'
print
print 'PASO 4: '
print 'W(I) = ['+str(W[1])+', '+str(W[2])+', '+str(W[3])+', '+str(W[4])+', '+str(W[5])+', '+str(W[6])+', '+str(W[7])+', '+str(W[8])+', '+str(W[9])+', '+str(W[10])+', '+str(W[11])+']'
print
print 'PASO 5: '
print 'I = '+str(I)
print
print 'PASO 6:'
print 'Mientras I sea menor o igual que 5'
print

while (I <= 5):
    print '--------------- I = '+str(I)+' ---------------'
    print
    print 'PASO 7:'
    
    if N == NP[I]:
        print 'Si N = NP(I), ir al paso 10: '+str(N)+' = '+str(NP[I])+' ? true'
        print
        I += 1
        break
    print 'Si N = NP(I), ir al paso 10: '+str(N)+' = '+str(NP[I])+' ? false'
    print
    print 'PASO 8:'
    print 'I = '+str(I)+' + 1'
    I += 1
    print 'I = '+str(I)
    print

if (N == NP[I-1]):
    I -= 1
    S = 0
    J = IAUX[I]
    
    print 'PASO 10:'
    print 'S = '+str(S)
    print
    print 'PASO 11:'
    print 'J = IAUX(I)'
    print 'J = '+str(IAUX[I])
    print
    print 'PASO 12:'
    print 'Mientras J sea menor o igual a IAUX (I + 1) - 1'
    print
    
    while (J <= IAUX[I+1] - 1):
        print '--------------- J = '+str(J)+' ---------------'
        print
        
        ZAUX = (Z[J] * (B - A) + B + A) / 2
        print 'PASO 13:'
        print 'ZAUX = (Z(J) * (B - A) + B + A) / 2'
        print 'ZAUX = ('+str(Z[J])+' * ('+str(B)+' - '+str(A)+') + '+str(B)+' + '+str(A)+') / 2'
        print 'ZAUX = '+str(ZAUX)
        print
        
        S = S + F(ZAUX) * W[J]
        print 'PASO 14:'
        print 'S = S + F(ZAUX) * W(J)'
        print 'S = '+str(S)+' + '+str(F(ZAUX))+' * '+str(W[J])
        print 'S = '+str(S)
        print
        
        ZAUX = (-Z[J] * (B - A) + B + A ) / 2
        print 'PASO 15:'
        print 'ZAUX = (-Z(J) * (B - A) + B + A) / 2'
        print 'ZAUX = ('+str(-Z[J])+' * ('+str(B)+' - '+str(A)+') + '+str(B)+' + '+str(A)+') / 2'
        print 'ZAUX = '+str(ZAUX)
        print
        
        S = S + F(ZAUX) * W[J]
        print 'PASO 16:'
        print 'S = S + F(ZAUX) * W(J)'
        print 'S = '+str(S)+' + '+str(F(ZAUX))+' * '+str(W[J])
        print 'S = '+str(S)
        print
        
        print 'PASO 17:'
        print 'J = '+str(J)+' + 1'
        J += 1
        print 'J = '+str(J)
        print
    AREA = (B - A) / 2 * S
    print 'PASO 18:'
    print 'AREA = (B - A) / 2 * S'
    print 'AREA = ('+str(B)+' - '+str(A)+') / 2 * '+str(S)
    print 'AREA = '+str(AREA)
    print 'AREA = '+str("%.8f" % AREA)
    print
else:
    print 'PASO 9:'
    print 'N NO ES 2, 3, 4, 5, o 6'
    print

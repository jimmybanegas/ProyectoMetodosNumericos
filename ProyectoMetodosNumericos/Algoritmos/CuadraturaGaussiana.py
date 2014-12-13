#coding=utf-8
import parserimport mathfrom math import *from lxml.html.builder import AREA
def cuadraturaGaus (funcion,A,B,N,lista ):
    ecuacion = parser.expr(funcion).compile()    resultado=0
    NP = [0, 2, 3, 4, 5, 6]    
    IAUX = [0, 1, 2, 4, 6, 9, 12]    
    Z = [0.0, 0.577350269, 0.0, 0.774596669, 0.339981044, 0.861136312, 0.0, 0.538469310, 0.906179846, 0.238619186, 0.661209387, 0.932469514]    
    W = [0.0, 1.0, 0.888888888, 0.555555555, 0.652145155, 0.347854845, 0.568888888, 0.478628671, 0.236926885, 0.467913935, 0.360761573, 0.171324493]    
    I = 1    
        
    lista.append ('PASO 1: ')    
    lista.append( 'NP(I) = ['+str(NP[1])+', '+str(NP[2])+', '+str(NP[3])+', '+str(NP[4])+', '+str(NP[5])+']')    
    
    lista.append('PASO 2: ')    
    lista.append('IAUX(I) = ['+str(IAUX[1])+', '+str(IAUX[2])+', '+str(IAUX[3])+', '+str(IAUX[4])+', '+str(IAUX[5])+', '+str(IAUX[6])+']')        
    lista.append( 'PASO 3: ')    
    lista.append( 'Z(I) = ['+str(Z[1])+', '+str(Z[2])+', '+str(Z[3])+', '+str(Z[4])+', '+str(Z[5])+', '+str(Z[6])+', '+str(Z[7])+', '+str(Z[8])+', '+str(Z[9])+', '+str(Z[10])+', '+str(Z[11])+']')    
        
    lista.append( 'PASO 4: ')    
    lista.append( 'W(I) = ['+str(W[1])+', '+str(W[2])+', '+str(W[3])+', '+str(W[4])+', '+str(W[5])+', '+str(W[6])+', '+str(W[7])+', '+str(W[8])+', '+str(W[9])+', '+str(W[10])+', '+str(W[11])+']')        
    lista.append( 'PASO 5: ')    
    lista.append( 'I = '+str(I))        
    lista.append( 'PASO 6:')    
    lista.append( 'Mientras I sea menor o igual que 5')    
    while (I <= 5):    
        lista.append( '--------------- I = '+str(I)+' ---------------')    
        
        lista.append('PASO 7:')    
            
        if N == NP[I]:    
            lista.append( 'Si N = NP(I), ir al paso 10: '+str(N)+' = '+str(NP[I])+' ? true')    
    
            I += 1    
            break    
        lista.append('Si N = NP(I), ir al paso 10: '+str(N)+' = '+str(NP[I])+' ? false')        
        lista.append( 'PASO 8:')    
        lista.append( 'I = '+str(I)+' + 1')    
        I += 1    
        lista.append( 'I = '+str(I))    
        
    if (N == NP[I-1]):    
        I -= 1    
        S = 0    
        J = IAUX[I]    
            
        lista.append( 'PASO 10:')    
        lista.append( 'S = '+str(S))        
        lista.append( 'PASO 11:')    
        lista.append('J = IAUX(I)')    
        lista.append('J = '+str(IAUX[I]))    
        lista.append( 'PASO 12:')    
        lista.append( 'Mientras J sea menor o igual a IAUX (I + 1) - 1')    
            
            
        while (J <= IAUX[I+1] - 1):    
            lista.append( '--------------- J = '+str(J)+' ---------------')    
    
            ZAUX = (Z[J] * (B - A) + B + A) / 2    
            lista.append( 'PASO 13:')    
            lista.append( 'ZAUX = (Z(J) * (B - A) + B + A) / 2')    
            lista.append( 'ZAUX = ('+str(Z[J])+' * ('+str(B)+' - '+str(A)+') + '+str(B)+' + '+str(A)+') / 2')    
            lista.append( 'ZAUX = '+str(ZAUX))    
            x = ZAUX    
            S = S + eval(ecuacion) * W[J]    
            lista.append( 'PASO 14:')    
            lista.append( 'S = S + F(ZAUX) * W(J)')    
            lista.append( 'S = '+str(S)+' + '+str( eval(ecuacion) )+' * '+str(W[J]))    
            lista.append( 'S = '+str(S))    
            
            ZAUX = (-Z[J] * (B - A) + B + A ) / 2    
            lista.append( 'PASO 15:')    
            lista.append( 'ZAUX = (-Z(J) * (B - A) + B + A) / 2')    
            lista.append( 'ZAUX = ('+str(-Z[J])+' * ('+str(B)+' - '+str(A)+') + '+str(B)+' + '+str(A)+') / 2')    
            lista.append('ZAUX = '+str(ZAUX))    
            
            S = S +  eval(ecuacion) * W[J]    
            lista.append('PASO 16:')    
            lista.append( 'S = S + F(ZAUX) * W(J)')    
            lista.append( 'S = '+str(S)+' + '+str( eval(ecuacion) )+' * '+str(W[J]))    
            lista.append( 'S = '+str(S))                        lista.append( 'PASO 17:')    
            lista.append( 'J = '+str(J)+' + 1')    
            J += 1    
            lista.append( 'J = '+str(J))    
    
        AREA = (B - A) / 2 * S                resultado=AREA        
        lista.append( 'PASO 18:')    
        lista.append( 'AREA = (B - A) / 2 * S')    
        lista.append( 'AREA = ('+str(B)+' - '+str(A)+') / 2 * '+str(S))    
        lista.append( 'AREA = '+str(AREA))    
        lista.append( 'AREA = '+str("%.8f" % AREA))    
           
    else:    
        lista.append( 'PASO 9:')    
        lista.append( 'N NO ES 2, 3, 4, 5, o 6')            if(resultado<0):       resultado=resultado*-1                return resultado;
            

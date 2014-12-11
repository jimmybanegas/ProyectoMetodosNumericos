# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 00:18:39 2014

@author: Marco
"""

def lagrangeMarco(gradoN,listaX,listaFX,xDerivada,listaPasos):
    listaPasos.append("#paso1 derivadaPolinomio =0")
    
    derivadaPolinomio=0 
    listaPasos.append("#paso2 contador =0")
    contador=0
    listaPasos.append("#paso3 mientras que i <= n")
    for contador in range (gradoN):
        listaPasos.append("#paso4 hacer p=1")
        p=1
        listaPasos.append("#paso5 hacer j=0")
        j=0
        listaPasos.append("#paso6 mientras j < n repetir pso 7 y 8 ")
        for j in range (gradoN):
            listaPasos.append("#paso7 i(contador) sea distinto que j hacer p=p*(x(i)-x(j))")
            if contador != j :
                p=p*(listaX[contador]-listaX[j])
                listaPasos.append("p="+ str(p))
                
            listaPasos.append("# paso8 j+1")
            j=j+1
            listaPasos.append(j)
            
        listaPasos.append("#paso9 hacer s=0")
        s=0
        listaPasos.append("#paso10 k=0")
        k=0
        listaPasos.append("#paso11 k<= gradoN repetir del 12 a  19")
        for k in range (gradoN):
            listaPasos.append("#paso12 mienta contador sea distinto que k realizar 13 a 18")
            listaPasos.append ("contador =" + str(contador)+ str(" ")+ str("k=") + str(k))
            if contador != k:
                listaPasos.append("#paso 13 hacer p1 = 1")
                p1 = 1
                listaPasos.append("#paso 14 Hacer j = 0")
                j = 0
                listaPasos.append("#paso 15 mientras j <= gradoN retir pasos 16 y 17")
                
        
                for j in range(gradoN):
                    listaPasos.append("#paso 16 si contador es distinto que J y J es distinto que K")
                    listaPasos.append ("contador="+ str(contador)+ str("  ") + str("j=") + str(j)+ str("  ")+ str("k=") + str(k))
                    if contador != j and j != k:
                        listaPasos.append("#hacer p1 = p1 * (xDerivada - listaX[j])")
                        listaPasos.append("p1="+ str(p1))
                        p1=p1*(xDerivada-listaX[j])
                    listaPasos.append("#paso 17 j+1")
                    
                    
                    j=j+1
                    listaPasos.append("j="+ str(j))
                listaPasos.append("#paso 18 hacer s= s+ p1")
                
                
                s=s+p1
                listaPasos.append("s="+str(s))
                
            listaPasos.append("#paso 19 hacer k+1")
            
            
            k=k+1
            listaPasos.append("k=" + str(k))
            
            
        listaPasos.append("#paso 20 derivadaPolinomio=derivadaPolinomio+listaFX[contador]/p*s")
        derivadaPolinomio=derivadaPolinomio+listaFX[contador]/p*s
        listaPasos.append("derivadaPolinomio=  "+ str(derivadaPolinomio))
        listaPasos.append("#paso 21 contador+1")
        contador=contador+1
    
    listaPasos.append("paso 22 imprimir derivadaPolinomio ")
    listaPasos.append(derivadaPolinomio )
#pasos = []
#lagrangeMarco(4,[23,45,22,134,324],[433,46,232,435,66],28,pasos)
            

            
            
                    
        
            
            
        
        
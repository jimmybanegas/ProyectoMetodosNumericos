# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 00:18:39 2014

@author: Marco
"""

def lagrangeMarco(gradoN,listaX,listaFX,iteraciones,resultadoTexto,xDerivada):
    print ("#paso1 derivadaPolinomio =0")
    print("  ")
    derivadaPolinomio=0 
    print("#paso2 contador =0")
    print("  ")
    contador=0
    print("#paso3 mientras que i <= n")
    print("  ")
    for contador in range (gradoN):
        print("#paso4 hacer p=1")
        print("  ")
        p=1
        print("#paso5 hacer j=0")
        print("  ")
        j=0
        print("#paso6 mientras j < n repetir pso 7 y 8 ")
        print("  ")
        for j in range (gradoN):
            print("#paso7 i(contador) sea distinto que j hacer p=p*(x(i)-x(j))")
            print("  ")
            if contador != j :
                p=p*(listaX[contador]-listaX[j])
                print("p=" , p)
                
            print("# paso8 j+1")
            print("  ")
            j=j+1
            print(j)
            print("  ")
        print("#paso9 hacer s=0")
        print("  ")
        s=0
        print("#paso10 k=0")
        print("  ")
        k=0
        print("#paso11 k<= gradoN repetir del 12 a  19")
        print("  ")
        for k in range (gradoN):
            print("#paso12 mienta contador sea distinto que k realizar 13 a 18")
            print("  ")
            print ("contador =" ,contador,"  ","k=", k)
            print("  ")
            if contador != k:
                print("#paso 13 hacer p1 = 1")
                print("  ")
                p1 = 1
                print("#paso 14 Hacer j = 0")
                print("  ")
                j = 0
                print("#paso 15 mientras j <= gradoN retir pasos 16 y 17")
                print("  ")
        
                for j in range(gradoN):
                    print("#paso 16 si contador es distinto que J y J es distinto que K")
                    print("  ")
                    print ("contador=",contador,"  ","j=",j,"  ","k=",k)
                    print("  ")
                    if contador != j and j != k:
                        print("#hacer p1 = p1 * (xDerivada - listaX[j])")
                        print("  ")
                        print("p1=",p1)
                        p1=p1*(xDerivada-listaX[j])
                    print("#paso 17 j+1")
                    print("  ")
                    
                    j=j+1
                    print("j=",j)
                    print("  ")
                print("#paso 18 hacer s= s+ p1")
                print("  ")
                
                s=s+p1
                print("s=",s)
                print("  ")
            print("#paso 19 hacer k+1")
            print("  ")
            
            k=k+1
            print("k=",k)
            print("  ")
            
        print("#paso 20 derivadaPolinomio=derivadaPolinomio+listaFX[contador]/p*s")
        print("  ")
        derivadaPolinomio=derivadaPolinomio+listaFX[contador]/p*s
        print("derivadaPolinomio=  ",derivadaPolinomio)
        print("  ")
        print("#paso 21 contador+1")
        print("   ")
        print("   ")
        print("   ")
        print("   ")
        contador=contador+1
    
    #paso 22 imprimir derivadaPolinomio 
    print(derivadaPolinomio )
holis=" "
lagrangeMarco(4,[23,45,22,134,324],[433,46,232,435,66],10, holis,28)
            
            
                    
        
            
            
        
        
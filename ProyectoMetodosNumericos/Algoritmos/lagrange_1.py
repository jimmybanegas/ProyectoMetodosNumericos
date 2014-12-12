# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 17:03:59 2014

@author: Marco
"""

def lagrange(gradoN,listaX,listaFx,xi,listaPasos):
    listaPasos.append("hacer FXINT=0")
    FXINT=0
    listaPasos.append("Hacer i=0")
    i=0
    for i in range(gradoN):
        listaPasos.append("hacer l=1")
        l=1
        listaPasos.append("hacer j=0")
        j=0
        listaPasos.append("Mientras j sea <= gradoN, repetir los pasos 7 y 8")
        for j in range(gradoN):
            listaPasos.append("mientras i sea distinto que j")
            if i != j:
                listaPasos.append("hacer l=l*((punto a evaluar-listax[j])/(listaX[i]-listax[j]))")
                l=l*((xi-listaX[j])/(listaX[i]-listaX[j]))
            listaPasos.append("hacer j=j+1")
            j=j+1
        listaPasos.append("FXINT=FXINT+L*listaFx[i]")
        FXINT=FXINT+l*listaFx[i]
        listaPasos.append("hacer i=i+1")
        i=i+1
    listaPasos.append(" imprimir FXINT")
    listaPasos.append(FXINT)
    
    return FXINT
#pasos=[]    
#lagrange(4,[87,65,34,32,67],[12,34,54,65,67],1.5,pasos)

    

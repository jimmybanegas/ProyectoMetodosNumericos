# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:37:45 2014

@author: Juan Carlos

Ejemplo para Erick
"""

#esta funcion se usa para evaluar una funcion con 'x' como variable, la String tiene
#que llevar 'x'. Por ejemplo x**2 + 2*x * 4. Si lleva otro simbolo no funciona por ejemplo
# y**3 + 4x. Para hacer estas cosas tenes que leer la documentacion, mejor quedate con la x

#definamos la expresion
expresion = "x**2 + 1"

def f(x):
    return eval(expresion)
    #en eval, se sustituira la variable por la 'x' que viene de parametro

#ahora usemos la funcion usando x = 2

print( "Dado f(x) = x**2 + 1, entonces f(2) = " + str(f(2)))

'''
Created on Nov 16, 2014

@author: carlosa
'''

def RegresionLineal(valoresX, valoresY, Xo):
        m = len(valoresX)
        constante1 = 0
        constante2 = 0
        constante3 = 0
        constante4 = 0
        i = 0
        while i < m:
            constante1 = constante1 + valoresY[i]
            constante2 = constante2 + (valoresX[i] * valoresX[i])
            constante3 = constante3 + valoresX[i]
            constante4 = constante4 + (valoresX[i] * valoresY[i])
            i = i + 1
        coeficiente1 = ((constante1*constante2) - (constante3*constante4))/((m * constante2)-(constante3*constante3))
        coeficiente2 = ((m*constante4) - (constante1*constante3))/((m * constante2)-(constante3*constante3))
        return coeficiente1 + (Xo*coeficiente2)


if __name__ == '__main__':
    print "Metodo de Regresion Lineal"
    lx = map(float, raw_input("Ingrese los valores de x: ").split())
    ly = map(float, raw_input("Ingrese los valores de y: ").split())
    x = raw_input("Ingrese el valor de la x a aproximar: ")
    xx = float(x)
    y = RegresionLineal(lx,ly,xx)
    
    print "y=" + str(y) + " para x=" + x  
'''
Created on Nov 16, 2014

@author: carlosa
'''

def RegresionLineal(valoresX, valoresY, Xo, lista):
        lista.append("Paso #1: Tome i=0")
        m = len(valoresX)
        constante1 = 0
        constante2 = 0
        constante3 = 0
        constante4 = 0
        i = 0
        while i < m:
            lista.append(" Mientras i<numero de datos, haga pasos 2-5")
            lista.append(" i=" + str(i))
            constante1 = constante1 + valoresY[i]
            constante2 = constante2 + (valoresX[i] * valoresX[i])
            constante3 = constante3 + valoresX[i]
            constante4 = constante4 + (valoresX[i] * valoresY[i])
            lista.append(" Paso 2: Tome c1= c1 + Yi")
            lista.append(" c1=" + str(constante1))
            lista.append(" Paso 3: Tome c2= c2 + Xi*Xi")
            lista.append(" c2=" + str(constante2))
            lista.append(" Paso 4: Tome c3= c3 + Xi")
            lista.append(" c3=" + str(constante3))
            lista.append(" Paso 5: Tome c4= c4 + Xi*Yi")
            lista.append(" c4=" + str(constante4))
            i = i + 1
        coeficiente1 = ((constante1*constante2) - (constante3*constante4))/((m * constante2)-(constante3*constante3))
        coeficiente2 = ((m*constante4) - (constante1*constante3))/((m * constante2)-(constante3*constante3))
        lista.append(" Paso 6: Tome coeficiente1= (c1*c2 - c3*c4)/(m*c2 - c3*c3)")
        lista.append(" coeficiente1=" + str(coeficiente1))
        lista.append(" Paso 7: Tome coeficiente2= (m*c4 - c1*c3)/(m*c2 - c3*c3)")
        lista.append(" coeficiente2=" + str(coeficiente2))
        lista.append(" Paso 8: Calcule la y de Xo con los coeficientes. Y=coef1 + Xo*coef2")
        y = coeficiente1 + (Xo*coeficiente2)
        lista.append(" Y de Xo=" + str(y))
        return y

'''
if __name__ == '__main__':
    print "Metodo de Regresion Lineal"
    lx = map(float, raw_input("Ingrese los valores de x: ").split())
    ly = map(float, raw_input("Ingrese los valores de y: ").split())
    x = raw_input("Ingrese el valor de la x a aproximar: ")
    xx = float(x)
    y = RegresionLineal(lx,ly,xx)
    
    print "y=" + str(y) + " para x=" + x  
    '''
   
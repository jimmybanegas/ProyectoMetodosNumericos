'''
Created on Nov 16, 2014

@author: carlosa
'''

def IngresarValores(matrizV, numfil):
        s = 0
        while s < numfil:
            sp = s + 1
            sri = "Ingrese la fila " + str(sp)
            fila = map(int, raw_input(sri).split())
            matrizV.append(fila)
            s = s + 1
            

def Reduccion_Gauss(matrizV, numfil, numcol):
        i = 0
        while i < numcol:
            if matrizV[i][i] == 0:
                j=i
                while j < numcol:
                    if matrizV[j][i] != 0:
                        temp = matrizV[j]
                        matrizV[j] = matrizV[i]
                        matrizV[i] = temp
                        j = numcol
                    elif ((matrizV[j][i] == 0) and (j==numcol)):
                        print "La matriz no se puede reducir"
                    j = j + 1
            if matrizV[i][i] != 1:
                z = i
                while z < numfil:
                    matrizV[i][z] = matrizV[i][z]/matrizV[i][i]
                    x = 0
                    while x < numcol:
                        w = 0
                        while w < numfil:
                            if x != i:
                                if x != 0:
                                    factor = (-1)*(matrizV[x][w])
                                matrizV[x][w] = matrizV[x][w] + matrizV[x][w]*factor
                            w = w + 1
                        x = x + 1
                    z = z + 1
            i = i + 1
        print "Proceso realizado exitosamente"
        f = 0
        while f < numfil:
            g = 0
            while g < numcol:
                print matrizV[f][g]
                g = g + 1
            f = f + 1

if __name__ == '__main__':
    print "SISTEMAS DE ECUACIONES POR ELIMINACION DE GAUSS"
    n = int(raw_input('Ingrese el numero de filas de la matriz a reducir: '))
    m = int(raw_input('Ingrese el numero de columnas de la matriz a reducir: '))
    matrizA = []
    IngresarValores(matrizA,n)
    print "Reduciendo Matriz"
    Reduccion_Gauss(matrizA, n, m)
    raw_input("Presione una tecla para finalizar")

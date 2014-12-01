'''
Created on 27/11/2014

@author: Javier
'''
def IngresarValores(matrizV, numfil, numcol):
        s = 0
        while s < numfil:
            sp = s + 1
            sri = "Ingrese la fila " + str(sp)
            fila = map(int, raw_input(sri).split())
            matrizV.append(fila)
            s = s + 1
            
'''n = numero de ecuaciones, a = matriz, b = vector de terminos '''
def Reduccion_Gauss(n, a , b):
    det = 1
    x = []
    i = 1
    while i <= n - 1:
        det = det*a[i,i]
        if det == 0  :
            print "HAY UN CERO EN LA DIAGONAL PRINCIPAL"
            return -1
        k = i+1
        while k<=n :
            j = i + i
            while j<=n :
                a[k,j] = a[k,j]-(a[k,i] * a[i,j] / a[i,i])
                j = j+i
            b [k] = b[k] - (a[k,i] * b[i] / a[i,i])
            k = k+1
        i = i+1
    det = det * a [n,n]
    if det == 0:
        print 'HAY UN CERO EN LA DIAGONAL'
        return -1
    x[n] = b[n] / a[n,n]
    i = n - 1 
    while i >= 1:
        x[i] = b[i]
        j = i + 1 
        while j <= n :
            x[i] = x[i] - a[i,j]*x[j]
            j = j + 1
    print det
    return x
        
if __name__ == '__main__':
    print "SISTEMAS DE ECUACIONES POR ELIMINACION DE GAUSS"
    n = int(raw_input('Ingrese el numero de filas de la matriz a reducir: '))
    m = int(raw_input('Ingrese el numero de columnas de la matriz a reducir: '))
    
    matrizA = [[]]
    i = 0
    j = 0
    while i < n :
        while j < m :
            matrizA.append(int(raw_input('ingrese un valor de la fila' + str(n))))
    b = []
    print "Reduciendo Matriz"
    Reduccion_Gauss(matrizA, n, b)
    print b[1]
    raw_input("Presione una tecla para finalizar")
    

def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")
    
def appending(A, lista):
    n = len(A)
    for i in range(0, n):

        str1 = " "
        for j in range(0, n+1):
            str1 += str(A[i][j])+ "\t"
            if j == n-1:
                str1 += "| "
        lista.append(str1)
    lista.append("")


def gauss(A, lista):
    n = len(A)
    lista.append("PROCEDIMIENTO DE RESOLUCION DE UNA MATRIZ")
    lista.append("Matriz a Resolver =")
    appending(A, lista)
    
    for i in range(0, n):
        # Search for maximum in this column
        
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k
                
        lista.append("Buscando el maximo de la columna actual...")
        lista.append("maximo = "+str(maxRow))
        
        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp
            
        lista.append("Cambiando de lugar las filas ...")
        appending(A, lista)
        
        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
        lista.append("Haciendo todas las filas debajo de esta = 0")
        appending(A, lista)

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    
    lista.append("Resolviendo la ecuacion Ax=b para la matriz ingresada...")
    appending(A, lista)
    lista.append("Proceso finalizado!")
    return x
    

if __name__ == "__main__":
    
    A = [[1, 1, 1, 3], [2, 3, 7, 0], [1, 3, -2, 17]]
    n = 3

    # Print input
    pprint(A)

    temp = []
    # Calculate solution
    x = gauss(A, temp)

    # Print result
    line = "Result:\t"
    for i in range(0, n):
        line += str(x[i]) + "\t"
    print(line)
'''
Created on 14/12/2014

@author: manuel
'''
def interpolacionNewton(listaXt, listaFxt, lista):
    listaX = eval(listaXt)
    listaFx = eval(listaFxt)
    
    lista.append ('METODO INTERPOLACION POLINOMIAL DE NEWTON)')
    
    lista.append (' ')
    
    #Paso 1
    lista.append ("Paso #1")
    lista.append ("Mientras i sea menor o igual al numero de coeficientes")
    lista.append ("\tMientras j sea menor o igual a i")
    
    F = [ [ 0 for i in range(len(listaFx)) ] for j in range(len(listaFx)) ]
    
    for i in range(len(listaFx)):
        F[i][0] = listaFx[i]
    
    for i in range(1,len(listaX)):
        for j in range(1, i+1):
            lista.append ("-------- i = " + str(i) + " ------- j = "+str(j)+"-----------")
            F[i][j] = (F[i][j-1] - F[i-1][j-1])/(listaX[i]-listaX[i-j])
            lista.append("\tF="+str(F[i][j]))
            
    x= "Respuesta: "
    for i in range(len(listaX)):
        x = x + str(F[i][i])
        for j in range(i):
            if(listaX[j]*-1 >=0):
                x= x+"(x + "+str(listaX[j]*-1)+")"
            else:
                x= x+"(x - "+str(listaX[j])+")"
        x = x +" + "
    lista.append(x)
    
    return x
#lista = []
#print interpolacionNewton("-2, -1, 2, 3", "4, 1, 4, 9", lista)
#print interpolacionNewton("1.0, 1.3, 1.6, 1.9, 2.2", "0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623", lista)
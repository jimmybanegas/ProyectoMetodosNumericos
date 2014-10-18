import parser
from  math import*

def bis(formula, a, b, tol, n_iter,lista):
    p = 0.00001
    code = parser.expr(formula).compile()

    lista.append("Paso #1")
    itera = 1
    lista.append( "Tome i = "+str(itera))

    x = a
    fun_a = eval(code)
    lista.append( "FA = f(a) = "+str(fun_a))

    lista.append( "Paso #2")
    lista.append( "Mientras i sea menor o igual al numero de iteraciones" )
    lista.append( "Hacer los pasos 3, 4, 5 y 6" )
    while itera <= n_iter:
        lista.append( "------------- i = " + str(itera) + " ------------------")

        lista.append( "Paso #3")
        lista.append( "p = "+str(a)+" + ("+str(b)+"-"+str(a)+")/2")
        p = a + float((b - a))/2

        x = p
        fun_p = eval(code)

        lista.append( "FP = "+str(fun_p))
        
        if fun_p == 0 or float((b - a))/2 < tol:
            lista.append( "verdadero")
            lista.append( str(p) )
            return p
            break
        else:
        
            lista.append( "es falso")
        
        itera=itera+1
        if fun_a*fun_p>0:
            a = p
            fun_a = fun_p
        else:
            b = p
            lista.append( "b="+str(b)+" p="+str(p))

    lista.append( "method failed")
    return 0





#bis("x**2 +4*(x**2)-10",1,2,0.00005,50)

#raw_input("Press<enter>")

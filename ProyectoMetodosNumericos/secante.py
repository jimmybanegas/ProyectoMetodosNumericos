import parser
from math import *

def secante(formula, p0, p1, tol, n_iter, lista):
	code = parser.expr(formula).compile()
	valor = 0
	dato =0
	
	lista.append("**********Metodo Secante**********)")
	
	lista.append("       *****Paso 1***** ")
	itera = 2
	lista.append( "Tome i = "+str(itera))
	x = p0
	q0 = eval(code)
	lista.append("Q0 = " + str(q0) )
	x = p1
	q1 = eval(code)	
	lista.append("Q1 = " + str(q1))
	
	lista.append("        *****Paso 2*****")
	lista.append("Mientras i <= a " + str(n_iter))
	lista.append("Hacer los pasos del 3 al 6" + "\n")
	
	while itera <= n_iter:
		lista.append("------------- i = " + str(itera) + " ------------------")
		lista.append("         *****Paso 3*****" )
		p = p1-((q1*(p1-p0))/(q1-q0))
		valor = p
		lista.append("      p = " + str(p) + "\n" )
	
		if(True):
		
			break
	
		lista.append("         *****Paso 4*****" )
		if(abs(p-p1) < tol):
			lista.append("Procedimiento terminado satisfactoriamente  despues de " + str(itera) + " iteracion(es)")
			lista.append("Con resultado : " + str(p))
			return p
		else:
			lista.append("      FALSO")
		
		lista.append("         *****Paso 5*****")
		itera  = itera +1
		lista.append("      i = " + str(itera-1) + "+1=" + str(itera) 	+ "\n" )
		
		lista.append("         *****Paso 6*****" )
		
		p0 = p1
		lista.append("      P0 = " + str(p1) )
		
		q0 = q1
		lista.append("      Q0 = " + str(q1) )
		
		p1 = p
		lista.append("      P1 = " + str(p)  )
		
		x = p
		lista.append("      x = " + str(p) )
		
		q1 = eval(code)
		lista.append("      Q1 = " + str(q1) + "\n")
		
 
	lista.append("Metodo Fallo" )
	

'''		
print "Ingrese ecuacion: "
ecua = raw_input()
print "Ingrese aprox inicial P0: "
p0 = float(raw_input())	
print "Ingrese aprox inicial P1: "
p1 = float(raw_input())
print "Ingrese tolerancia: "
tol = float(raw_input())
print "Ingrese total de iteraciones: "
ite = int(raw_input())

#print secante("cos(x)-x",1,2.0,0.0000	5,50)
print secante(ecua,p0,p1,tol,ite)

'''
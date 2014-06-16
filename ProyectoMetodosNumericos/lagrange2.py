#coding=utf-8

from math import *
import parser
from sympy import *

x = Symbol ('x')




def Lagrange(ecuacion,lx,xin):

		def f(x):
        		return eval(ecuacion)

    		n = (len(lx))-1
    		x_i=[]
    		z=0
    		while z <= n:
         		x_i.append(f(lx[z]))
         		z = z+1
                print ""
                print "Paso #1"
                print "hacer Fxint  = 0"
    		y = 0
		print ""
                print "Paso #2"
                print "hacer i  = 0"
    		i = 0  
		print ""
                print "Paso #3"
                print "mientras i<=N repetir paso 4 a 10"
    		while i <= n:
			print "------------------ i = " + str(i) + " ------------------"
			print ""
                	print "Paso #4"
			print "hacer L = 1"
        		L = 1
			print str(L)
        		j = 0
			print ""
                	print "Paso #5"
			print "hacer j = 0"
			print "J = "+str(j)
			print "Paso #2"
			"Mientras j sea menor o igual al numero de iteraciones"
			print "Hacer los pasos  7 y 8"
			print ""    
        		while j <= n:
				print "------------------ i = " + str(i) + " ------------------"
				print ""
				print " N = "+ str(n)
                		print "Paso #7"
				print "si i es diferente l entonces L=L*Xint-X(j)/X(i)-X(J)"
            			if  j != i:
                			L = L*(xin-lx[j])/(lx[i]-lx[j])
					print "L  = " + str(L)
            			j = j + 1
				print ""
				print "paso #8"
				print "J=J+1"
				print " J = " + str(j)	
        		y = y + L*x_i[i]
			print ""
			print "paso #9"
			print "FXint=Fxint+L*Fx(i)"
			print " FXint = " + str(y)
        		i = i + 1
    		print 'XIN = '+str(y)

	

def Lagrange2(x, lx, ly):
    
  
        		
    		n = (len(lx))-1
    		y = 0
    		i = 0  
    		while i <= n:
        		L = 1
        		j = 0    
        		while j <= n:
            			if  j != i:
                			L = L*(x-lx[j])/(lx[i]-lx[j])
            			j = j + 1
        		y = y + L*ly[i]
        		i = i + 1
    		print 'XIN = '+str(y)  
  
if __name__ == '__main__':
 
 print "METODO DE LAGRANGE"
 o = int(raw_input('presione 1 si desea ingresar la funcion o 2 si desea ingresar la tabla '))
 y=0
 if o == 1:
  ecuacion = raw_input('Introduzca la ecuación a resolver en forma de función: f(x)= ')
  lx = map(float, raw_input("Lista de valores de x: ").split())
  xin= float(eval(raw_input("valor a interpolar:")))
  y= Lagrange(ecuacion, lx, xin)
 elif o == 2: 
  x= float(eval(raw_input("valor a interpolar:")))
  lx = map(float, raw_input("Lista de valores de x: ").split())
  
  ly = map(float, raw_input("Lista de valores de f(x): ").split())
  
  y = Lagrange2(x, lx, ly)
    
 
 
   	
 raw_input("Presione una tecla para finalizar")

                    
                
 
 
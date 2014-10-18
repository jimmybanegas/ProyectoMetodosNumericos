from math import *

def traz_cubico_nat(listaFunciones,listaValores,listaMensajes):
	n=len(listaFunciones)
	h=[]
	alpha=[]
	miu=[]
	l=[]
	z=[]
	c=[]
	b=[]
	d=[]
	listaMensajes.append("\t"+"\t"+"TRAZADOR CUBICO NATURAL\n")
	

	#Paso 1
	listaMensajes.append("\t"+"PASO No. 1 \tTome i = 0 hasta n-1;\n")
	listaMensajes.append("\t"+"\t"+"hi=  (xi+1-xi) \n")

	
	for i in range(0,n-1):
		h.append(listaFunciones[i+1]-listaFunciones[i])
		listaMensajes.append("\t"+"\t"+"-----i = "+str(i)+"------"+"\n")
		listaMensajes.append("\t"+"\t"+"h"+str(i)+" = x"+str(i+1) +"- x"+str(i)+" = "+ str(h[i])+"\n")
	
	#Paso 2

	listaMensajes.append("\t"+"PASO No. 2   Tome i = 1 hasta n-1"+"\n")
	listaMensajes.append("\t"+"\t"+"alphai=  3/hi(ai+1-ai)-3/hi-1(ai-ai-1)"+"\n")
	alpha.append(0.)
	for j in range(1,n-1):
		alpha.append((3/h[j])*(listaValores[j+1]-listaValores[j])-(3/h[j])*(listaValores[j]-listaValores[j-1]))
		listaMensajes.append("\t"+"\t"+"-----i = "+str(j)+"------"+"\n")
		listaMensajes.append("\t"+"\t"+"alpha"+str(j)+"=  3/"+str(h[j])+"("+str(listaValores[j+1])+"-"+str(listaValores[j])
			+")-3/"+str(h[j-1])+"("+str(listaValores[j])+"-"+str(listaValores[j-1])+")"+"\n")


	#Paso 3
	listaMensajes.append("\t"+"PASO No. 3   Tome l0=1    miu=0     z0=0 \n")
	l.append(1.)
	miu.append(0.)
	z.append(0.)

	#Paso 4
	listaMensajes.append("\t"+"PASO No. 4       Tome i = 1 hasta n-1"+"\n")
	for k in range(1,n-1):
		l.append(2*(listaFunciones[k+1]-listaFunciones[k-1])-h[k-1]*miu[k-1])
		miu.append(h[k]/l[k])
		z.append((alpha[k]-h[k-1]*z[k-1])/l[k])
		listaMensajes.append("\t"+"\t"+"-----i = "+str(k)+"------"+"\n")
		listaMensajes.append("\t"+"\t"+"l"+str(k)+" = " "2*"+"("+str(listaFunciones[k+1])+" - "
			+str(listaFunciones[k-1])+")"+" - "+str(h[k-1])+" * "+str(miu[k-1]))
		listaMensajes.append("\t"+"\t"+"miu"+str(k)+" = "+str(h[k])+"/"+str(l[k]))
		listaMensajes.append("\t"+"\t"+"z"+str(k)+" = "+str(alpha[k])+"-"+str(h[k-1])+" * "+str(z[k-1])+" / "+str(l[k])+"\n")

	#Paso 5
	listaMensajes.append("\t"+"PASO No.5     ln=1    miu=0    zn=0"+"\n")


	for i in range(n):
		l.append(1.)
		z.append(0.)
		c.append(0.)

	#Paso 6
	listaMensajes.append("\t"+"PASO No. 6       Tome j = n-1 hasta 0"+"\n")
	for j in range(n-2,-1,-1):
		c[j]=z[j]-miu[j]*c[j+1]
		b.append(((listaValores[j+1]-listaValores[j])/h[j])-h[j]*(c[j+1]+2*c[j])/3)
		d.append((c[j+1]-c[j])/3*h[j])
		listaMensajes.append("\t"+"\t"+"-----j = "+str(j)+"------"+"\n")
		listaMensajes.append("\t"+"\t"+"c"+str(j)+" = "+str(z[j])+" - "+str(miu[j])+" * "+str(c[j+1]))
		listaMensajes.append("\t"+"\t"+"b"+str(j)+" = "+str(listaValores[j+1])+" - "+str(listaValores[j])
			+" / "+str(h[j])+" - "+str(h[j])+" * "+str(c[j+1])+str(2*c[j])+" / 3")
		listaMensajes.append("\t"+"\t"+"d"+str(j)+" = "+str(c[j+1])+" - "+str(c[j])+" / 3 * "+str(h[j])+"\n")

	#Paso 7
	listaMensajes.append("PASO No. 7      Salida")
	salida=[]
	salida.append("\t"+"Valores de a:"+"\n")
	for j in range(0,n-1):
		salida.append("\t"+"\t"+str(listaValores[j]))
	salida.append("\t"+"Valores de b:"+"\n")
	for j in range(0,n-1):
		salida.append("\t"+"\t"+str(b[j]))
	salida.append("\t"+"Valores de c:"+"\n")
	for j in range(0,n-1):
		salida.append("\t"+"\t"+str(c[j]))
	salida.append("\t"+"Valores de d:"+"\n")
	for j in range(0,n-1):
		salida.append("\t"+"\t"+str(d[j]))

	listaMensajes+=salida
	return salida


listamp=[]
lista=[]
listaw=[]

lista.append(0.7651977)
lista.append(0.6200860)
lista.append(0.4554022)
lista.append(0.2818186)
lista.append(0.1103623)

listaw.append(1.0)
listaw.append(1.3)
listaw.append(1.6)
listaw.append(1.9)
listaw.append(2.2)

traz_cubico_nat(listaw,lista,listamp)


for n in listamp:
	print n

a=raw_input('--> ')
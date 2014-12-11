from math import *


def factor_LU(dim,matAd,listaMensajes):
		l=[]
		u=[]
		salida=[]	

		for i in xrange(dim):
			l.append([])
			u.append([])
			for j in xrange(dim):
				u[i].append(0)
				if i==j:
					l[i].append(1)
				else:
					l[i].append(0)

		listaMensajes.append("\t\t\tFactorizacion LU\n")
		listaMensajes.append("\tPASO No.1\tSeleccione L11 y U11 = A11 Si es igual a 0 ")

	
		u[0][0]=matAd[0][0]
		if(u[0][0]==0):
			listaMensajes.append("\t Error U11= "+str(u[0][0])+" \n")
			salida.append('Factorizacion imposible U11 = '+str(u[0][0]))
			return salida
		else:
			listaMensajes.append("\t-------------------------\tU11 = "+str(u[0][0])+"\t-------------------------\n\n")

		listaMensajes.append("\tPASO No.2\tHacer j=2 \n")
		listaMensajes.append("\t mientras j sea menor la dimension tome \n\n")

	

		for j in range(1,dim):
			listaMensajes.append("\t-------------------------\tj = "+str(j+1)+"\t-------------------------\n\n")
			u[0][j]=matAd[0][j]/l[0][0]
			l[j][0]=matAd[j][0]/u[0][0]
			listaMensajes.append("\t U1"+str(j+1)+" = A1"+str(j+1)+"/L11 = "+str(u[0][j])+" \n")
			listaMensajes.append("\t L"+str(j+1)+"1 = A"+str(j+1)+"1/U11 = "+str(l[j][0])+"\n")

		listaMensajes.append("\tPASO No.3\tHacer i=2 \n")
		listaMensajes.append("\t mientras i sea menor la dimension menos 1 hacer pasos 4 y 5 \n\n")

		for i in range(1,dim-1):
			listaMensajes.append("\t-------------------------\ti = "+str(i+1)+"\t-------------------------\n\n")
			listaMensajes.append("\tPASO No.4\tSeleccione L"+str(i+1)+str(i+1)+" y U"+str(i+1)+str(i+1)+" = A"+str(i+1)+str(i+1)+"-Sumatoria(l"+str(i+1)+"k*Uki)")
			
			sumatoria=0
			for e in range(0,i-1):
				sumatoria+=l[i][e]*u[e][i]

			u[i][i]=matAd[i][i]-sumatoria

			listaMensajes.append("\t  L"+str(i+1)+str(i+1)+" = "+str(l[i][i])+" \n")
			listaMensajes.append("\t  U"+str(i+1)+str(i+1)+" = "+str(u[i][i])+" \n")

			if(u[i][i]==0):
				salida.append("\tFactorizacion imposible U"+str(i)+str(i)+" = "+str(u[i][i])+" \n")
				return salida

			listaMensajes.append("\tPASO No.5\tHacer j= i+1 \n")
			listaMensajes.append("\t mientras j sea menor la dimension \n\n")
			for j in range(i+1,dim):
			 	listaMensajes.append("\t-------------------------\tj = "+str(j+1)+"\t-------------------------\n\n")
			 	sumatoria=0
				for e in range(0,i-1):
					sumatoria+=l[i][e]*u[e][j]

				sumatoria2=0
				for e in range(0,i-1):
					sumatoria2+=l[j][e]*u[e][i]

				u[i][j]=(1/l[i][i])*(matAd[i][j]-sumatoria)
				l[j][i]=(1/u[i][i])*(matAd[j][i]-sumatoria2)

				listaMensajes.append("\t U"+str(i)+str(j)+" = 1/L"+str(i)+str(i)+"*(A"+str(i)+str(j)+" - "
					+"(L"+str(i)+str(1)+"*U"+str(1)+str(j)+")) = "+str(u[i][j])+"\n")
				listaMensajes.append("\t L"+str(j)+str(i)+" = 1/U"+str(i)+str(i)+"*(A"+str(j)+str(i)+" - "
					+"(L"+str(j)+str(1)+"*U"+str(1)+str(i)+")) = "+str(l[j][i])+"\n")

		listaMensajes.append("\tPASO No.6\tSeleccione L"+str(dim)+str(dim)+" y U"+str(dim)+str(dim)+" = A"
			+str(dim)+str(dim)+"-(l"+str(dim)+"1"+" * U1"+str(dim)+")")
		
		sumatoria=0
		for e in range(0,dim-1):
			sumatoria+=l[dim-1][e]*u[e][dim-1]

		u[dim-1][dim-1]=matAd[dim-1][dim-1]-sumatoria
		listaMensajes.append("\t  L"+str(dim)+str(dim)+" = "+str(l[dim-1][dim-1])+"\n")
		listaMensajes.append("\t  U"+str(dim)+str(dim)+" = "+str(u[dim-1][dim-1])+"\n")

		listaMensajes.append("\tPASO No.7\t Salida:\n")
		salida.append("\tMatriz L:")
		salida.append("\n")
	
		for i in xrange(dim):
			salida.append("\t"+"\t"+str(l[i]))
			

	
		salida.append("\n")
		salida.append("\tMatriz U:")
		salida.append("\n")
		for i in xrange(dim):
			salida.append("\t"+"\t"+str(u[i]))
		

		listaMensajes+=salida

		return salida








'''mat =[[1,1,0,3],
	  [2,1,-1,1],
	  [3,-1,-1,2],
	  [-1,2,3,1]]'''

mat=[[0,1,-1,1], [1,1,-1,2],[-1,-1,1,0],[1,2,0,2]]

vi=[4,-7,13,-13]
lm=[]
'''
factor_LU(4,mat,lm)
	


for n in lm:
	print n
	
'''
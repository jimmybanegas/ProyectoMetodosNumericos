'''
Created on 09/11/2014

@author: Javier
'''
import os
import collections
from docx import Document

def creartxt(self):
    try: 
        temp = os.path.join(os.path.abspath('datos.txt'))
        #path = os.path.abspath('Ejercicio_'+nombre+'.docx')  
        archi = open(temp,'r')
        archi.close() 
    except: 
        #temp = os.path.join(os.path.dirname(__file__), 'datos.txt')
        temp = os.path.join(os.path.abspath('datos.txt'))
        archi=open(temp,'w')
        archi.write('0\n')
        archi.close()
        
def creartxtfunciones(self):
    try: 
        #temp = os.path.join(os.path.dirname(__file__), 'resueltos.txt')
        temp = os.path.join(os.path.abspath('resueltos.txt'))
        archi = open(temp,'r')
        archi.close() 
    except: 
        #temp = os.path.join(os.path.dirname(__file__), 'resueltos.txt')
        temp = os.path.join(os.path.abspath('resueltos.txt'))
        archi=open(temp,'w')
        archi.close()
      
            
def grabartxt(self, mylist, respuesta, funcion):
    lista = results = [str(i) for i in mylist]
    fn = os.path.join(os.path.abspath('datos.txt'))
    archi=open(fn,'r+')
            
    numero_de_registros = archi.readline()
    number = int(numero_de_registros)+1
          
    pos_ultimo = 50
            
    if number != 1:
        archi.seek(0,2)
        pos_ultimo = archi.tell()
            
    archi.seek(0,0)
    archi.write( str(number) + '\n' )
    archi.write(str(pos_ultimo)+'\n')
            
    archi.seek(pos_ultimo,0)
            
    archi.write('1\n')
    archi.write(respuesta+'\n')
            
    for paso in lista:
        archi.write(paso+'\n')
                
    archi.write('#\n')
    archi.close()
    
    temp = os.path.join(os.path.abspath('resueltos.txt'))
    arch2=open(temp,'a')
    
    arch2.write(str(funcion)+'\n')
    arch2.write(str(pos_ultimo)+'\n')
    
    arch2.close()
    
    
def leerresueltos(self):
    lista = []
    fn = os.path.join(os.path.abspath('resueltos.txt'))
    archi=open(fn,'r')
    archi.seek(0,0)
    linea=archi.readline()
    while linea!="":
        lista.append(linea)
        linea=archi.readline()
        linea = archi.readline()
    archi.close()
    return lista

def leerposiciones(self):
    lista = []
    fn = os.path.join(os.path.abspath('resueltos.txt'))
    archi=open(fn,'r')
    archi.seek(0,0)
    archi.readline()
    linea=archi.readline()
    while linea!="":
        lista.append(linea)
        linea=archi.readline()
        if linea != "":
            linea = archi.readline()
    archi.close()
    return lista


def leerultimotxt(self):
    lista = []
    fn = os.path.join(os.path.abspath('datos.txt'))
    archi=open(fn,'r')
    archi.seek(0,0)
    numero_registros = archi.readline()
    pos = archi.readline()
    
    if numero_registros != '0' :
        archi.seek(int(pos),0)
            
        activo = archi.readline()
            
        if activo == '1\n' :
            resp = archi.readline()
            linea=archi.readline()
            while linea!='#\n':
                lista.append(linea)
                linea=archi.readline()
            
        else:
            lista.append('El ultimo procedimiento fue borrado')
    else:
        lista.append('none')
    archi.close()
    return lista
    
def leerultimarespuesta(self):
    fn = os.path.join(os.path.abspath('datos.txt'))
    archi=open(fn,'r+')
    archi.seek(0,0)
    numero_registros = archi.readline()
    
    if numero_registros != '0' :
        pos = int(archi.readline())
        archi.seek(pos,0)
        archi.readline()
        respuesta = archi.readline()
        archi.close()
        return respuesta
    else:
        archi.close()
        return 'none'
    
def leerespecifico(self, posicion):
    lista = []
    fn = os.path.join(os.path.abspath('datos.txt'))
    archi=open(fn,'r+')
    archi.seek(int(posicion), 0)
    linea=archi.readline()
    while linea!="#\n":
        lista.append(linea)
        linea=archi.readline()
    archi.close()
    return lista
    
def deployaword (self, texto, nombre):
    document = Document()
    
    for n in texto:
        document.add_paragraph(
        str(n), style='ListBullet')
         
    document.save(nombre)
    
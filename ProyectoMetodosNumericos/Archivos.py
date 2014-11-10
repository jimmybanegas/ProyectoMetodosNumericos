'''
Created on 09/11/2014

@author: Javier
'''
def creartxt(self):
    try: 
        archi = open('datos.txt','r')
        archi.close() 
    except: 
        archi=open('datos.txt','w')
        archi.write('0\n')
        archi.close()
      
        
def ubicar (self, jumps):
    archi=open('datos.txt','r+')
            
    archi.seek(0,2)
    size = archi.tell()
    archi.seek(0,0)
    archi.close()
            
def grabartxt(self, lista, respuesta):
    archi=open('datos.txt','r+')
            
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

def leerultimotxt(self, lista, respuesta):
    lista = []
    archi=open('datos.txt','r')
    archi.seek(0,0)
    archi.readline()
    pos = archi.readline()
    archi.seek(int(pos),0)
            
    activo = archi.readline()
            
    if activo == '1' :
        respuesta = archi.readline()
        linea=archi.readline()
        while linea!='#':
            lista.append(linea)
            linea=archi.readline()
            archi.close()
    else:
        respuesta = '0'
        lista.append('')
    
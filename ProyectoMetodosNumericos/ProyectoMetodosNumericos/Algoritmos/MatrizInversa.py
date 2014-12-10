#coding=utf-8
from sympy import Matrix
import json
def MatrizInversa(a, b,lista):    
    ma = json.loads(a)    
    mb = json.loads(b)    
    A = Matrix(ma)    
    B = Matrix(mb)    
    try:    
        A_inv = A.inv()    
    except ValueError:    
        lista.append('\n')    
        lista.append( 'Matriz es singular, no se puede resolver!')    
        lista.append('\n')     
    else:    
        ans = A_inv*B    
        MA = A.tolist()    
        MB = B.tolist()    
        MA_inv = A_inv.tolist()    
        M_ans = ans.tolist()    
        lista.append(' Matriz A = ')    
        lista.append('\t|   '+('|\n\t|   '.join([''.join(['{:4}'.format(item) for item in row]) for row in MA]))+'|')    
        lista.append('\n')    
        lista.append( 'Vector B = ')    
        lista.append( '\t|   '+('|\n\t|   '.join([''.join(['{:4}'.format(item) for item in row]) for row in MB]))+'|')    
        lista.append('\n')    
        lista.append( 'Matriz Inversa de A^-1 =')    
        lista.append('\t|   '+('\t|\n\t|   '.join(['\t'.join(['{:4}'.format(item) for item in row]) for row in MA_inv]))+'\t|')    
        lista.append('\n')    
        lista.append( 'Respuesta A^-1 * B =')    
        lista.append('\t|   '+('|\n\t|   '.join([''.join(['{:4}'.format(item) for item in row]) for row in M_ans]))+'|')
        return 0        



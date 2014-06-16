#coding=utf-8
from sympy import Matrix
import json

a = raw_input('Introduzca la matriz A = ')
ma = json.loads(a)
b = raw_input('Introduzca el vector B = ')
mb = json.loads(b)

A = Matrix(ma)
B = Matrix(mb)
try:
    A_inv = A.inv()
except ValueError:
    print
    print 'Matriz es singular, no se puede resolver!'
    print
else:
    ans = A_inv*B
    MA = A.tolist()
    MB = B.tolist()
    MA_inv = A_inv.tolist()
    M_ans = ans.tolist()

    print
    print 'Matriz A = '
    print'\t|   '+('|\n\t|   '.join([''.join(['{:4}'.format(item) for item in row]) for row in MA]))+'|'
    print
    print 'Vector B = '
    print '\t|   '+('|\n\t|   '.join([''.join(['{:4}'.format(item) for item in row]) for row in MB]))+'|'
    print
    print 'Matriz Inversa de A^-1 ='
    print '\t|   '+('\t|\n\t|   '.join(['\t'.join(['{:4}'.format(item) for item in row]) for row in MA_inv]))+'\t|'
    print
    print 'Respuesta A^-1 * B ='
    print '\t|   '+('|\n\t|   '.join([''.join(['{:4}'.format(item) for item in row]) for row in M_ans]))+'|'
    print
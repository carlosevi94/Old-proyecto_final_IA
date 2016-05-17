# -*- coding: utf-8 -*-
import math
import numpy

class puzzle:
    
    
    def creaEstadoInicial(self,tamano):
        M=math.sqrt(tamano+1)
        matrix=numpy.zeros((M,M))
        lista=[]
        for n in range (tamano+1):
            lista.append(n)
        for i in range (int (M)):
            for j in range (int (M)):
                r=numpy.random.randint(len(lista))
                matrix[i][j]=lista[r]
                lista.pop(r)
        return matrix
        
    def esSolucion(self,estado,tamano):
        res=True
        M=math.sqrt(tamano+1)
        solucion=numpy.zeros((M,M))
        c=0
        lista=[]
        for n in range (tamano+1):
            lista.append(n)
        for i in range (int (M)):
            for j in range (int (M)):
                solucion[i][j]=lista[c]
                c=c+1
        print (solucion)
        print (estado)
        for i in range (int (M)):
            for j in range (int (M)):
                a=solucion[i][j]
                b=estado[i][j]
                if(a!=b):
                    res=False
                    break
        return res
#Pruebas Varias
for n in range (100):
    print(puzzle.creaEstadoInicial(puzzle,8))
    
''''s=numpy.matrix('0.,1.,2.;3.,4.,5.;6.,7.,8.')

print(puzzle.esSolucion(puzzle,puzzle.creaEstadoInicial(puzzle, 8),8))'''


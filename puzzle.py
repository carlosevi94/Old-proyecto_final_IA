# -*- coding: utf-8 -*-
import numpy
import math

class puzzle:
    matrix=""
    estadoFinal=False
    M=""
    tamano=0
    
    def __init__(self,tamano):
        self.tamano=tamano
        self.M = int(math.sqrt(tamano + 1))
        self.estadoFinal = numpy.zeros((self.M, self.M))
        lista = []
        c=0
        for n in range (tamano + 1):
            lista.append(n)
        for i in range (self.M):
            for j in range(self.M):
                self.estadoFinal[i][j] = lista[c]
                c = c + 1
        
    def creaEstadoInicial(self):
        M = math.sqrt(self.tamano + 1)
        self.matrix = numpy.zeros((M, M))
        lista = []
        for n in range (self.tamano + 1):
            lista.append(n)
        for i in range (int (M)):
            for j in range (int (M)):
                r = numpy.random.randint(len(lista))
                self.matrix[i][j] = lista[r]
                lista.pop(r)
        
    def esSolucion(self):
        res = True
        for i in range (self.M):
            for j in range (self.M):
                a = self.estadoFinal[i][j]
                b = self.matrix[i][j]
                if(a != b):
                    res = False
                    break
        return res
    
    def encontrarHueco(self):
        res=(-1,-1)
        for i in range(self.M):
            for j in range(self.M):
                if self.matrix[i][j]==0:
                    res=(i,j)
        return res
            
    
    def expandirNodo(self):
        
        return 
 
 
'''----------------------------------------------------------'''
   
e=puzzle(15)
e.creaEstadoInicial()
print(e.matrix)
print(e.estadoFinal)
print(e.esSolucion())
print(e.encontrarHueco())


    

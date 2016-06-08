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
                self.estadoFinal[i][j] = int(lista[c])
                c = c + 1
        
    def creaEstadoInicial(self):
        M = math.sqrt(self.tamano + 1)
        self.matrix = numpy.zeros((M, M))
        lista = []
        for n in range (self.tamano + 1):
            lista.append(n)
        for i in range (int (M)):
            for j in range (int (M)):
                r = int(numpy.random.randint(len(lista)))
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
        mov=[]
        res=[]
        pos=self.encontrarHueco()
        linea=pos[0]
        col=pos[1]
        if linea>0:
            mov.append((linea-1,col))
        if linea<(self.M-1):
            mov.append((linea+1,col))
        if col>0:
            mov.append((linea,col-1))
        if col<(self.M-1):
            mov.append((linea,col+1))
        print (mov)
        for n in mov:
            copia=self.clonaEstado()
            copia.matrix[n[0]][n[1]],copia.matrix[linea][col]=copia.matrix[linea][col],copia.matrix[n[0]][n[1]]
            res.append(copia)
            
        return res
    

    def clonaEstado(self):
        copia=puzzle(self.tamano)
        copia.matrix=self.matrix
        return copia
        
 
'''----------------------------------------------------------'''
   
e=puzzle(8)
e.creaEstadoInicial()
print(e.matrix)
print(e.estadoFinal)
print(e.esSolucion())
print(e.encontrarHueco())
hijos=e.expandirNodo()
for n in hijos:
    print (n.matrix)


    

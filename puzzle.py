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
        self.matrix = numpy.zeros((self.M, self.M))
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
        lista = []
        for n in range (self.tamano + 1):
            lista.append(n)
        for i in range (self.M):
            for j in range (self.M):
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
    
    def encontrarPos(self,pos,op):
        res=(-1,-1)
        if op==True:
            for i in range(self.M):
                for j in range(self.M):
                    if self.matrix[i][j]==pos:
                        res=(i,j)
        else:
            for i in range(self.M):
                for j in range(self.M):
                    if self.estadoFinal[i][j]==pos:
                        res=(i,j)
        return res
            
    
    def expandirNodo(self):
        mov=[]
        res=[]
        pos=self.encontrarPos(0,True)
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
            a=n[0]
            b=n[1]
            copia=self.clonaEstado()
            copia.matrix[a][b],copia.matrix[linea][col]=copia.matrix[linea][col],copia.matrix[a][b]
            res.append(copia)
            
        return res
    

    def clonaEstado(self):
        copia=puzzle(self.tamano)
        for i in range (self.M):
            for j in range (self.M):
                copia.matrix[i][j]=self.matrix[i][j]
        return copia
      
    def __repr__(self):
        return repr(self.matrix)
    
    def getHeuristica(self):
        res=0
        for n in range(self.tamano+1):
            pos=self.encontrarPos(n,True)
            ideal=self.encontrarPos(n,False)
            res+=abs(pos[0]-ideal[0])+abs(pos[1]-ideal[1])
        return res
'''----------------------------------------------------------'''
   
e=puzzle(8)
e.creaEstadoInicial()
print(e.matrix)
print(e.estadoFinal)
'''print(e.esSolucion())
print(e.encontrarPos(0,True))
hijos=e.expandirNodo()
for n in hijos:
    print (n)'''
print(e.getHeuristica())


    

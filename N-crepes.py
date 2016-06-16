# -*- coding: utf-8 -*-
import numpy
import math

class crepes:
    
    estadoFinal=[]
    crepes=[]
    tamano=0
    
    def __init__(self,tamano):
        self.tamano=tamano 
        self.crepes=[]     
        lista = []
        c=0
        for n in range (1,tamano+1):
            lista.append(n)
        
        self.estadoFinal=lista
        
        
        
    def creaEstadoInicial(self):
        lista = []
        for n in range (1,self.tamano+1):
            lista.append(n)
        for i in range (len(lista)):            
            r = numpy.random.randint(len(lista))
            self.crepes.append(lista[r])
            lista.pop(r)
        
        
    def esSolucion(self):
        res = True
        for i in range (self.tamano):  
            var1=self.crepes[i]                   
            if(var1 != i+1):
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
        res=[]
        for k in range(2,self.tamano+1):
            
            copia=self.clonaEstado()
            sublista=copia.crepes[:k]
            sublistaRestante=copia.crepes[k:]
            sublista.reverse()
            auxiliar1=sublista+sublistaRestante
            copia.crepes=auxiliar1
            res.append(copia)
            res.sort()
            
        return res
    

    def clonaEstado(self):
        copia = crepes(self.tamano) 
        for a in range(len(self.crepes)):
            copia.crepes.append(self.crepes[a])
        return copia
    
      
    def __repr__(self):
        return repr(self.crepes)
    
    def getHeuristica(self):
        resultado=0
        
        for a in range (0,self.tamano-1):
            euris=0
            var1=self.crepes[a]
            var2=self.crepes[a+1]
            euris=abs(var2-var1)
            euris=euris-1
            resultado=resultado+euris
        
        return resultado
    
    
    def __gt__(self,crepe):
        return self.getHeuristica() > crepe.getHeuristica()
'''----------------------------------------------------------'''
   
e=crepes(5)
e.creaEstadoInicial()
print("------ESTADO FINAL------")
print(e.estadoFinal)
print("--------------")

print("------LISTA DE LAS CREPES------")
print(e.crepes)
print("--------------")


#print(e.esSolucion())



print("------CREPE CLONADA------")
f=e.clonaEstado()
print(f.crepes)
print("--------------")

#print(e.esSolucion())
#print(e.encontrarPos(0,True))

print("---------EXPANDIR NODO---------")
hijos=e.expandirNodo()
#el n ya es un crepe
for n in hijos:
    print (n.crepes)
    print (n.getHeuristica())
#print(e.getHeuristica())'''
print("--------------")


print("---------Heuristica---------")
crepeur=crepes(5)
crepeur.creaEstadoInicial()
print(crepeur.crepes)
print(crepeur.getHeuristica())

#print(e.getHeuristica())'''
print("--------------")

  
  


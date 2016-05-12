# -*- coding: utf-8 -*-
import numpy
import math


def main():  
    
    pass

def npuzzle(tamano,algoritmo,tammemoria,tamhaz):
    pass
    

def estado(tamano):
    tamanomatriz=math.sqrt(tamano+1)
    #Creamos aqui la matriz.
    matriz=numpy.zeros((tamanomatriz,tamanomatriz))
    #Creamos una lista con los objetos N
    lista=[]    
    for a in range(tamano):
        lista.append(a)
    
    
    matriz[0][0]=1
    
    print(matriz)



main()
estado(8)
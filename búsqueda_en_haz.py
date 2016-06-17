from Puzzle import puzzle
from crepes import crepes

def BusquedaHaz(self,estadoInicial,memoriaMax,haz):
    memoria=[]
    res=0
    nodoActual=estadoInicial
    memoria.append(estadoInicial)
   
    sol=False
    hijos=nodoActual.expandirNodo()
    while sol==False and len(memoria)<memoriaMax:     
        if(len(memoria)>1):
            for n in hijos:
                p=n.Padre
                igual=True          
                for i in range(n.M):
                    for j in range(n.M):
                        if(n.matrix[i][j])!=p.Padre.matrix[i][j]:
                            igual=False
                            break
                if(igual==True):
                    hijos.remove(n)       
        bloque=hijos[:haz]
        memoria.append(bloque)
        hijos=[]
        for n in bloque:
            if n.esSolucion():
                sol=True
                res=len(memoria)
                break
            else:
                l=n.expandirNodo()
                for i in l:
                    hijos.append(i)
            hijos.sort()
    return res


#p=puzzle(8)
#p.creaEstadoInicial()
#print(BusquedaHaz(puzzle,p,10,2))
        
c=crepes(5)
c.creaEstadoInicial()      
print(BusquedaHaz(crepes,c,10,2)) 
        
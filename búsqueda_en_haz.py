from Puzzle import puzzle

def BusquedaHaz(self,estadoInicial,memoriaMax,haz):
    memoria=[]
    res=0
    nodoActual=estadoInicial
    memoria.append(estadoInicial)
    sol=False
    hijos=nodoActual.expandirNodo()
    while sol==False and len(memoria)<memoriaMax:
        print ("------------------- ITERACION ----------")
        bloque=hijos[:haz]
        
        print("Longitud de memoria "+str(len(memoria)))
        if(len(memoria)!=1):
            for aux in bloque:
                aux.pop(nodoActual.Padre) 
            #print(nodoActual.Padre)
            #bloque.remove(nodoActual.Padre)           
            #bloque.rem           
        
        
        memoria.append(bloque)
        hijos=[]
        for n in bloque:
            print(n)
            
            print("La heuristica es "+str(n.getHeuristica()))
            if n.esSolucion():
                sol=True
                res=len(memoria)
                break
            else:
                l=n.expandirNodo()
                for i in l:
                    hijos.append(i)
            hijos.sort()
            print("LOS HIJOS SON")
            
            for n in hijos:
                print (n)
            #print(hijos)
    return res

p=puzzle(8)
p.creaEstadoInicial()

print(BusquedaHaz(puzzle,p,10,1))
        
        
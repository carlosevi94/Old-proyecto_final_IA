from Puzzle import puzzle
def BusquedaHaz(self,estadoInicial,memoriaMax,haz):
    memoria=[]
    res=0
    nodoActual=estadoInicial
    memoria.append(estadoInicial)
    sol=False
    hijos=nodoActual.expandirNodo()
    while sol==False and len(memoria)<memoriaMax:
        bloque=hijos[:haz]
        memoria.append(bloque)
        hijos=[]
        for n in bloque:
            print(n)
            print(n.getHeuristica())
            if n.esSolucion():
                sol=True
                res=len(memoria)
                break
            else:
                l=n.expandirNodo()
                for i in l:
                    hijos.append(i)
            hijos.sort()
            print(hijos)
    return res

p=puzzle(8)
p.creaEstadoInicial()

print(BusquedaHaz(puzzle,p,10,1))
        
        
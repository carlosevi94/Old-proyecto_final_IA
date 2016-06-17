from Puzzle import puzzle
from crepes import crepes


archivo = open("puzzles.txt", "r") 
#linea1 = archivo.readline()
#print (linea1)
contenido = archivo.readlines()



archivo2 = open("puzzles15.txt", "r") 
contenido2 = archivo2.readlines()

archivo3 = open("puzzles24.txt", "r") 
contenido3 = archivo3.readlines()








listaDePuzzlesde8=[]

aux1=0
aux2=0
aux3=0
aux4=0
aux5=0
listitaPaLaMatriz=[]
objeto=0

def rellenarMatrices1(puzzle,auxilio1,auxilio2,auxilio3):
    for a in auxilio1:       
        if(a.isdigit()):           
            listitaPaLaMatriz.append(a)            
    for b in auxilio2:
        if(b.isdigit()):
            listitaPaLaMatriz.append(b)   
    for c in auxilio3:
        if(c.isdigit()):
            listitaPaLaMatriz.append(c)
    
            
    
    p=puzzle
    p.matrix[0][0] = int(listitaPaLaMatriz[0])
    p.matrix[0][1] = int(listitaPaLaMatriz[1])
    p.matrix[0][2] = int(listitaPaLaMatriz[2])
    p.matrix[1][0] = int(listitaPaLaMatriz[3])
    p.matrix[1][1] = int(listitaPaLaMatriz[4])
    p.matrix[1][2] = int(listitaPaLaMatriz[5])
    p.matrix[2][0] = int(listitaPaLaMatriz[6])
    p.matrix[2][1] = int(listitaPaLaMatriz[7])
    p.matrix[2][2] = int(listitaPaLaMatriz[8])
    

def rellenarMatrices2(puzzle,auxilio1,auxilio2,auxilio3,auxilio4):
    for a in auxilio1:       
        if(a.isdigit()):           
            listitaPaLaMatriz.append(a)            
    for b in auxilio2:
        if(b.isdigit()):
            listitaPaLaMatriz.append(b)   
    for c in auxilio3:
        if(c.isdigit()):
            listitaPaLaMatriz.append(c)
    for d in auxilio4:
        if(c.isdigit()):
            listitaPaLaMatriz.append(d)
    
            
    
    p=puzzle
    p.matrix[0][0] = int(listitaPaLaMatriz[0])
    p.matrix[0][1] = int(listitaPaLaMatriz[1])
    p.matrix[0][2] = int(listitaPaLaMatriz[2])
    p.matrix[0][3] = int(listitaPaLaMatriz[3])
    p.matrix[1][0] = int(listitaPaLaMatriz[4])
    p.matrix[1][1] = int(listitaPaLaMatriz[5])
    p.matrix[1][2] = int(listitaPaLaMatriz[6])
    p.matrix[1][3] = int(listitaPaLaMatriz[7])
    p.matrix[2][0] = int(listitaPaLaMatriz[8])
    p.matrix[2][1] = int(listitaPaLaMatriz[9])
    p.matrix[2][2] = int(listitaPaLaMatriz[10])
    p.matrix[2][3] = int(listitaPaLaMatriz[11])
    p.matrix[3][0] = int(listitaPaLaMatriz[12])
    p.matrix[3][1] = int(listitaPaLaMatriz[13])
    p.matrix[3][2] = int(listitaPaLaMatriz[14])
    p.matrix[3][3] = int(listitaPaLaMatriz[15])

def rellenarMatrices3(puzzle,auxilio1,auxilio2,auxilio3,auxilio4,auxilio5):
    for a in auxilio1:       
        if(a.isdigit()):           
            listitaPaLaMatriz.append(a)            
    for b in auxilio2:
        if(b.isdigit()):
            listitaPaLaMatriz.append(b)   
    for c in auxilio3:
        if(c.isdigit()):
            listitaPaLaMatriz.append(c)
    for d in auxilio4:
        if(d.isdigit()):
            listitaPaLaMatriz.append(d)
    for e in auxilio5:
        if(e.isdigit()):
            listitaPaLaMatriz.append(e)        
    
   p=puzzle
    p.matrix[0][0] = int(listitaPaLaMatriz[0])
    p.matrix[0][1] = int(listitaPaLaMatriz[1])
    p.matrix[0][2] = int(listitaPaLaMatriz[2])
    p.matrix[0][3] = int(listitaPaLaMatriz[3])
    p.matrix[0][4] = int(listitaPaLaMatriz[3])
    p.matrix[1][0] = int(listitaPaLaMatriz[4])
    p.matrix[1][1] = int(listitaPaLaMatriz[5])
    p.matrix[1][2] = int(listitaPaLaMatriz[6])
    p.matrix[1][3] = int(listitaPaLaMatriz[7])
    p.matrix[1][4] = int(listitaPaLaMatriz[7])
    p.matrix[2][0] = int(listitaPaLaMatriz[8])
    p.matrix[2][1] = int(listitaPaLaMatriz[9])
    p.matrix[2][2] = int(listitaPaLaMatriz[10])
    p.matrix[2][3] = int(listitaPaLaMatriz[11])
    p.matrix[3][4] = int(listitaPaLaMatriz[7])
    p.matrix[3][0] = int(listitaPaLaMatriz[12])
    p.matrix[3][1] = int(listitaPaLaMatriz[13])
    p.matrix[3][2] = int(listitaPaLaMatriz[14])
    p.matrix[3][3] = int(listitaPaLaMatriz[15])
    p.matrix[3][4] = int(listitaPaLaMatriz[7])
    p.matrix[4][0] = int(listitaPaLaMatriz[12])
    p.matrix[4][1] = int(listitaPaLaMatriz[13])
    p.matrix[4][2] = int(listitaPaLaMatriz[14])
    p.matrix[4][3] = int(listitaPaLaMatriz[15])
    p.matrix[4][4] = int(listitaPaLaMatriz[7])

for a in contenido:
    if(objeto==0):        
        aux1=a
        objeto=objeto+1
    elif(objeto==1):
        aux2=a
        objeto=objeto+1
    elif(objeto==2):
        aux3=a
            
        puzleaux=puzzle(8)        
        rellenarMatrices1(puzleaux, aux1, aux2, aux3)
        listaDePuzzlesde8.append(puzleaux)
        puzleaux=0
        objeto=0
        aux1=0
        aux2=0
        aux3=0
        listitaPaLaMatriz=[]
    
 
    
'''        
print ("ESTO ES AUX1")        
print (aux1)  
print ("ESTO ES AUX2")  
print (aux2)
print ("ESTO ES AUX3")  
print (aux3)      
'''
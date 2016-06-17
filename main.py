from Puzzle import puzzle
from crepes import crepes


archivo = open("puzzles.txt", "r") 
contenido = archivo.readlines()

archivo2 = open("puzzles15.txt", "r") 
contenido2 = archivo2.readlines()

archivo3 = open("puzzles24.txt", "r") 
contenido3 = archivo3.readlines()








listaDePuzzlesde8=[]
listaDePuzzlesde15=[]
listaDePuzzlesde24=[]

aux1=0
aux2=0
aux3=0
aux4=0
aux5=0
listitaPaLaMatriz=[]
listitaPaLaMatriz2=[]
listitaPaLaMatriz3=[]
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
            listitaPaLaMatriz2.append(a)            
    for b in auxilio2:
        if(b.isdigit()):
            listitaPaLaMatriz2.append(b)   
    for c in auxilio3:
        if(c.isdigit()):
            listitaPaLaMatriz2.append(c)
    for d in auxilio4:
        if(d.isdigit()):
            listitaPaLaMatriz2.append(d)
            
            
            
    print (listitaPaLaMatriz2)
    print (len(listitaPaLaMatriz2))
            
    
    p=puzzle
    p.matrix[0][0] = int(listitaPaLaMatriz2[0])
    p.matrix[0][1] = int(listitaPaLaMatriz2[1])
    p.matrix[0][2] = int(listitaPaLaMatriz2[2])
    p.matrix[0][3] = int(listitaPaLaMatriz2[3])
    p.matrix[1][0] = int(listitaPaLaMatriz2[4])
    p.matrix[1][1] = int(listitaPaLaMatriz2[5])
    p.matrix[1][2] = int(listitaPaLaMatriz2[6])
    p.matrix[1][3] = int(listitaPaLaMatriz2[7])
    p.matrix[2][0] = int(listitaPaLaMatriz2[8])
    p.matrix[2][1] = int(listitaPaLaMatriz2[9])
    p.matrix[2][2] = int(listitaPaLaMatriz2[10])
    p.matrix[2][3] = int(listitaPaLaMatriz2[11])
    p.matrix[3][0] = int(listitaPaLaMatriz2[12])
    p.matrix[3][1] = int(listitaPaLaMatriz2[13])
    p.matrix[3][2] = int(listitaPaLaMatriz2[14])
    p.matrix[3][3] = int(listitaPaLaMatriz2[15])

def rellenarMatrices3(puzzle,auxilio1,auxilio2,auxilio3,auxilio4,auxilio5):
    for a in auxilio1:       
        if(a.isdigit()):           
            listitaPaLaMatriz3.append(a)            
    for b in auxilio2:
        if(b.isdigit()):
            listitaPaLaMatriz3.append(b)   
    for c in auxilio3:
        if(c.isdigit()):
            listitaPaLaMatriz3.append(c)
    for d in auxilio4:
        if(d.isdigit()):
            listitaPaLaMatriz3.append(d)
    for e in auxilio5:
        if(e.isdigit()):
            listitaPaLaMatriz3.append(e)        
    
    p=puzzle
    p.matrix[0][0] = int(listitaPaLaMatriz3[0])
    p.matrix[0][1] = int(listitaPaLaMatriz3[1])
    p.matrix[0][2] = int(listitaPaLaMatriz3[2])
    p.matrix[0][3] = int(listitaPaLaMatriz3[3])
    p.matrix[0][4] = int(listitaPaLaMatriz3[4])
    p.matrix[1][0] = int(listitaPaLaMatriz3[5])
    p.matrix[1][1] = int(listitaPaLaMatriz3[6])
    p.matrix[1][2] = int(listitaPaLaMatriz3[7])
    p.matrix[1][3] = int(listitaPaLaMatriz3[8])
    p.matrix[1][4] = int(listitaPaLaMatriz3[9])
    p.matrix[2][0] = int(listitaPaLaMatriz3[10])
    p.matrix[2][1] = int(listitaPaLaMatriz3[11])
    p.matrix[2][2] = int(listitaPaLaMatriz3[12])
    p.matrix[2][3] = int(listitaPaLaMatriz3[13])
    p.matrix[3][4] = int(listitaPaLaMatriz3[14])
    p.matrix[3][0] = int(listitaPaLaMatriz3[15])
    p.matrix[3][1] = int(listitaPaLaMatriz3[16])
    p.matrix[3][2] = int(listitaPaLaMatriz3[17])
    p.matrix[3][3] = int(listitaPaLaMatriz3[18])
    p.matrix[3][4] = int(listitaPaLaMatriz3[19])
    p.matrix[4][0] = int(listitaPaLaMatriz3[20])
    p.matrix[4][1] = int(listitaPaLaMatriz3[21])
    p.matrix[4][2] = int(listitaPaLaMatriz3[22])
    p.matrix[4][3] = int(listitaPaLaMatriz3[23])
    p.matrix[4][4] = int(listitaPaLaMatriz3[24])


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


for a in contenido2:
    if(objeto==0):        
        aux1=a
        print(aux1)
        objeto=objeto+1
    elif(objeto==1):
        aux2=a
        objeto=objeto+1
    elif(objeto==2):
        aux3=a
        objeto=objeto+1
    elif(objeto==3):
        aux4=a              
       
        puzleaux2=puzzle(15)        
        rellenarMatrices2(puzleaux2, aux1, aux2, aux3, aux4)
        listaDePuzzlesde15.append(puzleaux2)
        puzleaux=0
        objeto=0
        aux1=0
        aux2=0
        aux3=0
        aux4=0
        listitaPaLaMatriz2=[]
       

for a in contenido3:
    if(objeto==0):        
        aux1=a
        objeto=objeto+1
    elif(objeto==1):
        aux2=a
        objeto=objeto+1
    elif(objeto==2):
        aux3=a
        objeto=objeto+1
    elif(objeto==3):
        aux4=a
        objeto=objeto+1
    elif(objeto==4): 
        aux5=a               
        puzleaux3=puzzle(24)        
        rellenarMatrices3(puzleaux3, aux1, aux2, aux3, aux4,aux5)
        listaDePuzzlesde24.append(puzleaux3)
        puzleaux=0
        objeto=0
        aux1=0
        aux2=0
        aux3=0
        aux4=0
        aux5=0
        listitaPaLaMatriz3=[] 
 

     


print(listaDePuzzlesde8)
print(listaDePuzzlesde15)
print(listaDePuzzlesde24)
    

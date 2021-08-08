files = open("Cuentos.txt","r") #Abriendo el archivo
tamano =  files.readlines() #ya que readlines() se vuelve inutil lo guardo
try:
    for x in range(len(tamano)): #el tamaño de la lista con len
        xd=str(len(tamano[x])-1) #Obteniendo el tamaño de cada linea -1 por el "\n"
        if x <len(tamano):
            print(tamano[x][0], end=xd) #Las listas de strings es una matriz :v
            print()
        else:
            xd=str(len(tamano[x])) #El ultimo no tiene "\n"
            print(tamano[x][0], end=xd)
            print()       
finally:
    files.close()
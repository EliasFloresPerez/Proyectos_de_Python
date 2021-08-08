archivo = open("archivito.txt","w")
archivo.write("108 150 0")
archivo.close()
archivo2 = open("archivito.txt","r")
tamano=archivo2.readlines()

tamano = "".join(map(str,tamano))
tamano = tamano.split(' ')
print(tamano[1])


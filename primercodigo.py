#archivos
palabra="Hola todo el mundo"
Archivo = open("Archivo.txt","w")
cont = Archivo.write(palabra)
print(cont)
Archivo.close()
Archivo =  open("Archivo.txt","r")
print(Archivo.read())
Archivo.close()
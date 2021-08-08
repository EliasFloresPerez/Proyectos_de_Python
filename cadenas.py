cadena_separada=[]
datos=[]
n=1
cadena=""

for i in range(n):
    cadena = input()
    cadena_separada.append(cadena.split(' '))


for i in range(n):
    for j in range(n):
        if cadena_separada[i][j]==" ":
            a=a+1
        else:
            datos.append(int(cadena_separada[i][j]))

print(datos)
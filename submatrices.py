lista = []
lista1 = []
lista2 = []
producto = []
cadena2=[]
cadena_separada=[]
datos=[]
contador=0

n=0
dato = 0
q=0
z=0
#Bucle para que la columna sea par en un rango dado 4-100
while n<4 or n>100 or not(n%2==0):
    n = int(input())

#Se crea la matriz :D
for x in range(n):
    lista.append([0]*n)

#Creo los dos vectores
for x in range(int(n/2)):
    lista1.append([0]*int(n/2))

for x in range(int(n/2)):
    lista2.append([0]*int(n/2))

for x in range(int(n/2)):
    producto.append([0]*int(n/2))


#Se leen los valores dados por el usuario
for i in range(n):
    cadena = input()
    cadena_separada.append(cadena.split(' '))


for i in range(n):
    for j in range(n):
        if cadena_separada[i][j]==" ":
            a=a+1
        else:
            datos.append(int(cadena_separada[i][j]))

for i in range(n):
    for j in range(n):
        lista[i][j]=datos[contador]
        contador=contador+1


cadena_separada.clear()
datos.clear()
for i in range(1):
    cadena = input()
    cadena_separada.append(cadena.split(' '))


for i in range(1):
    for j in range(2):
        if cadena_separada[i][j]==" ":
            a=a+1
        else:
            datos.append(int(cadena_separada[i][j]))

q= datos[0]
z=datos[1]

#Evaluando la matriz del vector 1
if q == 1:
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            lista1[i][j]= lista[i][j]
elif q == 2:
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            lista1[i][j]= lista[i][j+int(n/2)]
elif q == 3:
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            lista1[i][j]= lista[i+int(n/2)][j]
else:
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            lista1[i][j]= lista[i+int(n/2)][j+int(n/2)]

#Evaluando la matriz del vector 2
if z == 1:
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            lista2[i][j]= lista[i][j]
elif z == 2:
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            lista2[i][j]= lista[i][j+int(n/2)]
elif z == 3:
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            lista2[i][j]= lista[i+int(n/2)][j]
else:
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            lista2[i][j]= lista[i+int(n/2)][j+int(n/2)]

#Multiplicando matrices
for i in range(int(n/2)):
    for j in range(int(n/2)):
        for k in range(int(n/2)):
            producto[i][j]+=lista1[i][k]*lista2[k][j]

for i in range(int(n/2)):
    for j in range(int(n/2)):
        print(producto[i][j], end=" ")
    print()

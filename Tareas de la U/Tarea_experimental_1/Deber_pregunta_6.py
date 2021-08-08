#Codigo
lista = []
miLista = [1, 2, 44, 4, 1, 44, 2, 6, 2, 9]
des = "n"
des = input("Deseas poner los datos y/n?: ")

#Pidiendo datos si el quiso poner datos 
if des=="y":
    miLista.clear()
    total = int(input("cuantos datos vas a poner ?:"))
    numero = 0
    for x in range(total):
        print("Número ",x+1," :",end="")
        numero = int(input())
        miLista.append(numero)

#Eliminar datos repetidos
for x in miLista:
    if x not in lista:
        lista.append(x)

#Salida
print(lista)
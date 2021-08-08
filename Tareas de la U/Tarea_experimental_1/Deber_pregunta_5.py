#Mayor de una lista

total = int(input("cuantos datos vas a poner ?:"))
lista = []
numero = 0
for x in range(total):
    print("Número ",x+1," :",end="")
    numero = int(input())
    lista.append(numero)

#Podria usar los metodos burbuja :v pero pa que?

lista.sort() #la ordena ascendentemente
lista.reverse() #Por comodidad de buscar el primer valor
print("El numero mayor es :",lista[0])
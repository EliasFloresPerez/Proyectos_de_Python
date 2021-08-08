#funcion pura [Trabajan con su argumentos]
def funcion(x):
    return x*2


#funcion impura [Modifican algo de afuera o llaman a otras funciones]
array = []
def funcionI(x):
    array.append(x)
    array.append(5)

funcionI(4)
print(array)

#Lambdas
double= lambda x: x*2 #interesante :v
print(double(4))
#MAP
def sumar(x):
    #numeros.append(x)
    return x+5
numeros = [1,2,3,4,5]
resultado = list(map(sumar,numeros))
print(resultado)
'''
for x in range(len(numeros)):
    numeros[x] = sumar(numeros[x])
print(numeros)
'''

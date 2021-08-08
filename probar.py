import numpy as np
from sympy import *
from matplotlib import pyplot as plt
from itertools import product

lista_funciones = []
def graficiar2(B):
    def funcion_2(x):
        
        return eval(str(B))
    
    mu= range(0,10)
    plt.plot(mu,[funcion_2(i) for i in mu])

def graficar(A):
    if A[0]==0:
        return
    else:
        m = (0-A[1])/(A[0]-0)
        b= -(m*A[0])+0
        funcion = str(m)+"*x+"+str(b)
    lista_funciones.append(funcion)
    

lista_restric = [[6,9],[4,'i'],['i',6]]

for i in range(3):
    graficar(lista_restric[i])

for i in range(3):
    graficiar2(lista_funciones[i])
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
'''
t = (poo[1]-coo[1])/(poo[0]-coo[0])
b = -(t*coo[0])+coo[1]
print("y="+str(t)+"x"+"+"+str(b))
'''
from matplotlib import pyplot as plt
from itertools import product
from Metodo_Grafico import lista_r ,lista_p,permutacion,restricciones
import numpy as np

plt.axhline(y=0, xmin=0, xmax=9,color="k")
plt.axvline(x=0, ymin=0, ymax=9,color="k")
aux_x = 0
while aux_x < (len(restricciones)):
    
    if lista_r[aux_x][0][0]=="i":
        
        plt.axhline(y=lista_r[aux_x][1][1], xmin=0, xmax=1)
        aux_x = aux_x+1
        continue
    if lista_r[aux_x][1][1]=="i":    
        plt.axvline(x=lista_r[aux_x][0][0], ymin=0, ymax=1)
        aux_x = aux_x+1
        continue
    plt.plot(lista_r[aux_x][0],lista_r[aux_x][1])
    aux_x = aux_x+1

for i in range(len(lista_p)):
    
    plt.plot(lista_p[i][0],lista_p[i][1], marker="o", color="red")

#plt.fill_between(,color="green")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")

plt.show()
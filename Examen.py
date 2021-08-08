import numpy as np
from matplotlib import pyplot as plt
def f(t):
    return t

t = np.arange(0,10,1/1000.)
section = np.arange(0,4, 1/1000.)
plt.fill_between([0, 0,3,0],[6, 9, 6,6],color="green") #Esto toma el valor de cada array y lo pinta con el otra array 4,4 y 5,5 :)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(t,f(t))
plt.show()
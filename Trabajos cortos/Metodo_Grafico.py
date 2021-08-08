from sympy import *
init_printing()

lista_p = []
lista_r = []
lista_region=[]

restricciones = ['3*x+2*y-(18)','0*x+0*y-(0)','0*x+0*y-(0)']
valores = [1,1,1,1,1]
max_mini = 1
funcion_t = ""


def puntos(funcion):

    global lista_r
    x=symbols('x')
    y = symbols('y')
    #Despejamos cada funcion una en x y otra en y
    puntos_z = []
    puntos_z.append(solve(funcion,x))
    puntos_z.append(solve(funcion,y))
    
    #La evaluamos con respecto a "x" y "y"
    x,y=1,0
    puntos_z[0]=eval(str(puntos_z[0]))
    
    try:
        lista_p.append([puntos_z[0][0],0])
    except:
        print(puntos_z[0])
    x,y=0,1
    puntos_z[1]=eval(str(puntos_z[1]))
    try:
        lista_p.append([0,puntos_z[1][0]])
    except:
        print(puntos_z[1])
    
    
    if puntos_z[0]==[]:
        puntos_z[0]="i"

    if puntos_z[1]==[]:
        puntos_z[1]="i"
    
    lista_r.append([[puntos_z[0][0],0],[0,puntos_z[1][0]]])


def puntos_combinados(funcion_1,funcion_2):
    global lista_p
    x=symbols('x')
    y = symbols('y')
    puntos_com= solve([funcion_1,funcion_2])
    lista_p.append([puntos_com[x],puntos_com[y]])
     
def puntos_validos(funcion,lista,valores_1):
    aux = 0
    global lista_region
    for i in range(len(lista)):
        for j in range(len(funcion)):
            if valores_1[j] == 1:
                x = lista[i][0]
                y = lista[i][1]
                if not(eval(funcion[j])<=0):
                    aux = 1

            if valores_1[j] == 0:
                x = lista[i][0]
                y = lista[i][1]
                if not(eval(funcion[j])>=0):
                    aux = 1

        if aux == 0:
            lista_region.append(lista[i])
        aux=0

for i in range(restricciones.count('0*x+0*y-(0)')):
    restricciones.remove('0*x+0*y-(0)')


for i in range(len(restricciones)):
        puntos(restricciones[i])

permutacion = 1
aux = 0

while(aux<permutacion):
    a=aux
    
    while(a+1<=permutacion):
        if len(restricciones)!=1:
            puntos_combinados(restricciones[aux],restricciones[a+1])
        a=a+1
    aux=aux+1
lista_p.append([0,0])

puntos_validos(restricciones,lista_p,valores)

print(lista_p)
print(lista_r)
print(lista_region)
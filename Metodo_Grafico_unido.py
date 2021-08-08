import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter.constants import END, TRUE
import os
from matplotlib import pyplot as plt
from itertools import product
import numpy as np

from sympy import *
init_printing()

ventana = tk.Tk()


ventana.title("Metodo Grafico")
ventana.geometry("450x420")
ventana.resizable(width=False, height=False)
#Backend

lista_restric = []
lista_m = []
max_min = 0
funcion = ""
p_solucion = []
lista_funciones = []
lim_x = 0
lim_y = 0

def errores():
    
    global lista_restric,lista_m,max_min,funcion
    lista_restric.clear()
    try:
        if Funcion_x.get()=="":Funcion_x.delete(0,"end"),Funcion_x.insert(0,"0")
        if Funcion_y.get()=="":Funcion_y.delete(0,"end"),Funcion_y.insert(0,"0")


        if restriccion_x1.get()=="":restriccion_x1.delete(0,"end"),restriccion_x1.insert(0,"0")
        if restriccion_x2.get()=="":restriccion_x2.delete(0,"end"),restriccion_x2.insert(0,"0")
        if restriccion_x12.get()=="":restriccion_x12.delete(0,"end"),restriccion_x12.insert(0,"0")
        if restriccion_x22.get()=="":restriccion_x22.delete(0,"end"),restriccion_x22.insert(0,"0")
        if restriccion_x13.get()=="":restriccion_x13.delete(0,"end"),restriccion_x13.insert(0,"0")    
        if restriccion_x23.get()=="":restriccion_x23.delete(0,"end"),restriccion_x23.insert(0,"0")
        if restriccion_x14.get()=="":restriccion_x14.delete(0,"end"),restriccion_x14.insert(0,"0")
        if restriccion_x24.get()=="":restriccion_x24.delete(0,"end"),restriccion_x24.insert(0,"0")
        if restriccion_x15.get()=="":restriccion_x15.delete(0,"end"),restriccion_x15.insert(0,"0")    
        if restriccion_x25.get()=="":restriccion_x25.delete(0,"end"),restriccion_x25.insert(0,"0")

        if restriccion_resultado1.get()=="":restriccion_resultado1.delete(0,"end"),restriccion_resultado1.insert(0,"0")
        if restriccion_resultado2.get()=="":restriccion_resultado2.delete(0,"end"),restriccion_resultado2.insert(0,"0")
        if restriccion_resultado3.get()=="":restriccion_resultado3.delete(0,"end"),restriccion_resultado3.insert(0,"0")
        if restriccion_resultado4.get()=="":restriccion_resultado4.delete(0,"end"),restriccion_resultado4.insert(0,"0")
        if restriccion_resultado5.get()=="":restriccion_resultado5.delete(0,"end"),restriccion_resultado5.insert(0,"0")



        funcion=str(Funcion_x.get())+"*x+"+str(Funcion_y.get())+"*y"
        
        if restriccion_x1.get() == "0" and restriccion_x2.get() == "0":
            restriccion_resultado1.delete(0,"end")
            restriccion_resultado1.insert(0,"0")

        if restriccion_x12.get() == "0" and restriccion_x22.get() == "0":
            restriccion_resultado2.delete(0,"end")
            restriccion_resultado2.insert(0,"0")

        if restriccion_x13.get() == "0" and restriccion_x23.get() == "0":
            restriccion_resultado3.delete(0,"end")
            restriccion_resultado3.insert(0,"0")

        if restriccion_x14.get() == "0" and restriccion_x24.get() == "0":
            restriccion_resultado4.delete(0,"end")
            restriccion_resultado4.insert(0,"0")
        if restriccion_x15.get() == "0" and restriccion_x25.get() == "0":
            restriccion_resultado5.delete(0,"end")
            restriccion_resultado5.insert(0,"0")   
                    
        lista_restric.append(str(restriccion_x1.get())+"*x"+"+"+str(restriccion_x2.get())+"*y"+"-("+str(restriccion_resultado1.get())+")")
        lista_restric.append(str(restriccion_x12.get())+"*x"+"+"+str(restriccion_x22.get())+"*y"+"-("+str(restriccion_resultado2.get())+")")
        lista_restric.append(str(restriccion_x13.get())+"*x"+"+"+str(restriccion_x23.get())+"*y"+"-("+str(restriccion_resultado3.get())+")")
        lista_restric.append(str(restriccion_x14.get())+"*x"+"+"+str(restriccion_x24.get())+"*y"+"-("+str(restriccion_resultado4.get())+")")
        lista_restric.append(str(restriccion_x15.get())+"*x"+"+"+str(restriccion_x25.get())+"*y"+"-("+str(restriccion_resultado5.get())+")")
        
        lista_m.clear()

        lista_m.append(combo1.current())
        lista_m.append(combo2.current())
        lista_m.append(combo3.current())
        lista_m.append(combo4.current())
        lista_m.append(combo5.current())

        max_min =combo.current()
        x=0
        y=0
        for i in lista_restric:
            eval(i)-1

        #La funcion debe tener valores mayores o iguales a 0
        vbb = float(Funcion_x.get())
        vbc = float(Funcion_y.get())
        #if vbb<0 or vbc<0:
        #    eval(0/0)
        #La funcion principal las dos no pueden ser 0

        if vbb==0 and vbc==0:
            eval(0/0)
        eval(funcion)
        
    except:
        cartel013["fg"]="red"
        cartel013["text"]="Datos erroneos , reviselos porfavor"
    ejecutar()    


#Frontend
#Colores
color = '#%02x%02x%02x' % (133, 193, 233)
color2 = '#%02x%02x%02x' % (133, 193, 233)
#Imagen
imga = tk.PhotoImage(file="fondo_grafico.png")
panel = tk.Label(ventana, image = imga)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Letras
letra = tkFont.Font(family="Lucida Grande", size=10)
letra2 = tkFont.Font(family="Lucida Grande", size=15)
#Carteles

#Titulo
titulo = tk.Label(ventana,text="Metodo Grafico",bg=color,fg ="black",width=15,font=letra2)
titulo.place(x=150,y=5)
pregunta = tk.Label(ventana,text="¿Cual es el objetivo de la función?",bg=color,fg ="black",width=27,font=letra)
pregunta.place(x=70,y=40)
combo = ttk.Combobox(ventana, state="readonly",width=11)
combo["values"] = ["Maximizar","Minimizar"]
combo.set("Maximizar")
combo.place(x=295, y=40)

cartel1= tk.Label(ventana,text="Función:",bg=color,fg ="black",width=8,font=letra)
cartel1.place(x=60,y=75)
cartel2= tk.Label(ventana,text="X1 +",bg=color,fg ="black",width=3,font=letra)
cartel2.place(x=235,y=75)
cartel3= tk.Label(ventana,text="X2",bg=color,fg ="black",width=2,font=letra)
cartel3.place(x=370,y=75)
#Titulo Entry
Funcion_x =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
Funcion_y =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
Funcion_x.place(x=135,y=75)
Funcion_y.place(x=270,y=75)
#Restricciones
titulo_re = tk.Label(ventana,text="Restricciones:",bg=color,fg ="black",width=13,font=letra)
titulo_re.place(x=180,y=105)

#Carteles x1 +
cartel01= tk.Label(ventana,text="X1 +",bg=color,fg ="black",width=3,font=letra)
cartel01.place(x=130,y=145)
cartel02= tk.Label(ventana,text="X1 +",bg=color,fg ="black",width=3,font=letra)
cartel02.place(x=130,y=175)
cartel03= tk.Label(ventana,text="X1 +",bg=color,fg ="black",width=3,font=letra)
cartel03.place(x=130,y=205)
cartel04= tk.Label(ventana,text="X1 +",bg=color,fg ="black",width=3,font=letra)
cartel04.place(x=130,y=235)
cartel05= tk.Label(ventana,text="X1 +",bg=color,fg ="black",width=3,font=letra)
cartel05.place(x=130,y=265)

#Carteles X2
cartel021= tk.Label(ventana,text="X2",bg=color,fg ="black",width=2,font=letra)
cartel021.place(x=265,y=145)
cartel022= tk.Label(ventana,text="X2",bg=color,fg ="black",width=2,font=letra)
cartel022.place(x=265,y=175)
cartel023= tk.Label(ventana,text="X2",bg=color,fg ="black",width=2,font=letra)
cartel023.place(x=265,y=205)
cartel024= tk.Label(ventana,text="X2",bg=color,fg ="black",width=2,font=letra)
cartel024.place(x=265,y=235)
cartel025= tk.Label(ventana,text="X2",bg=color,fg ="black",width=2,font=letra)
cartel025.place(x=265,y=265)

#Restricciones x1 y x2
restriccion_x1 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_x2 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_x1.place(x=30,y=145)
restriccion_x2.place(x=165,y=145)

restriccion_x12 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_x22 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_x12.place(x=30,y=175)
restriccion_x22.place(x=165,y=175)

restriccion_x13 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_x23 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_x13.place(x=30,y=205)
restriccion_x23.place(x=165,y=205)

restriccion_x14 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_x24 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_x14.place(x=30,y=235)
restriccion_x24.place(x=165,y=235)

restriccion_x15 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_x25 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_x15.place(x=30,y=265)
restriccion_x25.place(x=165,y=265)

#Desplegables
combo1 = ttk.Combobox(ventana, state="readonly",width=2)
combo1["values"] = ["≥","≤"]
combo1.set("≤")
combo1.place(x=295, y=145)

combo2 = ttk.Combobox(ventana, state="readonly",width=2)
combo2["values"] = ["≥","≤"]
combo2.set("≤")
combo2.place(x=295, y=175)

combo3 = ttk.Combobox(ventana, state="readonly",width=2)
combo3["values"] = ["≥","≤"]
combo3.set("≤")
combo3.place(x=295, y=205)

combo4 = ttk.Combobox(ventana, state="readonly",width=2)
combo4["values"] = ["≥","≤"]
combo4.set("≤")
combo4.place(x=295, y=235)

combo5 = ttk.Combobox(ventana, state="readonly",width=2)
combo5["values"] = ["≥","≤"]
combo5.set("≤")
combo5.place(x=295, y=265)

#Restriccion Resultado
restriccion_resultado1 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_resultado1.place(x=335,y=145)

restriccion_resultado2 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_resultado2.place(x=335,y=175)

restriccion_resultado3 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_resultado3.place(x=335,y=205)

restriccion_resultado4 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_resultado4.place(x=335,y=235)

restriccion_resultado5 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
restriccion_resultado5.place(x=335,y=265)

#Botones y finales
cartel012= tk.Label(ventana,text="X1,X2 ≥ 0 ",bg=color,fg ="black",width=7,font=letra)
cartel012.place(x=200,y=300)

button_enviar = tk.Button(ventana,text="Enviar",width=10,fg="black",bg=color,heigh=2,command=errores)
button_enviar.place(x=190,y=330)

cartel013= tk.Label(ventana,text="Resultado:",bg=color,fg ="black",width=35,font=letra2,anchor="nw")
cartel013.place(x=30,y=380)

#METODO GRAFICO

lista_p = []
lista_r = []
lista_region=[]

def buscar(AB):
    
    global lim_x , lim_y
    if AB[0]=='i' or AB[1]=='i':
        return
    
    if AB[0]>lim_x:
        lim_x = AB[0]
    if AB[1]>lim_y:
        lim_y = AB[1]

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
        pass
    x,y=0,1
    puntos_z[1]=eval(str(puntos_z[1]))
    try:
        lista_p.append([0,puntos_z[1][0]])
    except:
        pass
    if puntos_z[0]==[]:
        puntos_z[0]="i"

    if puntos_z[1]==[]:
        puntos_z[1]="i"
 
    lista_r.append([[puntos_z[0][0],0],[0,puntos_z[1][0]]])


def puntos_combinados(funcion_1,funcion_2):
    global lista_p
    x=symbols('x')
    y = symbols('y')
    try:
        puntos_com= solve([funcion_1,funcion_2])
        
        lista_p.append([puntos_com[x],puntos_com[y]])
    except:
        return
     
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
                if x<0 or y<0:
                    aux = 1

            if valores_1[j] == 0:
                x = lista[i][0]
                y = lista[i][1]
                if not(eval(funcion[j])>=0):
                    aux = 1
                if x<0 or y<0:
                    aux = 1
    
        if aux == 0:
            lista_region.append(lista[i])
        aux=0


def ejecutar():
    lista_p.clear()
    lista_r.clear()
    lista_region.clear()
    
    permutacion = 0

    for i in range(lista_restric.count('0*x+0*y-(0)')):
        lista_m.pop(lista_restric.index('0*x+0*y-(0)'))

        lista_restric.remove('0*x+0*y-(0)')
        
    
    for i in range(len(lista_restric)):
        puntos(lista_restric[i])
        
    
    if len(lista_restric)==1:
        permutacion = 0
    elif len(lista_restric)==2:
        permutacion = 1
    elif len(lista_restric)==3:
        permutacion = 3
    elif len(lista_restric)==4:
        permutacion = 6
    elif len(lista_restric)==5:
        permutacion = 10
        
    aux = 0

    while(aux<permutacion):
        a=aux
        
        while(a+1<len(lista_restric)):
            if len(lista_restric)!=1:
                puntos_combinados(lista_restric[aux],lista_restric[a+1])
            a=a+1
        aux=aux+1
    lista_p.append([0,0])

    puntos_validos(lista_restric,lista_p,lista_m)

 
    if len(lista_region)>0:
        for i in range(len(lista_r)):
            
            buscar(lista_r[i][0])
            buscar(lista_r[i][1])
        
        calcular()
    else:
        cartel013["fg"]="red"
        cartel013["text"]="El problema no tiene solucion"

    graficar()
    

#Ordenador burbuja condicionado
def burbuja(A):
    bandera = 0
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1][0] < A[j][0]):
                aux=A[j]
                A[j]=A[j+1]
                A[j+1]=aux
            elif (A[j+1][0] == A[j][0]):
                if(A[j+1][1] > A[j][1]):
                    aux=A[j]
                    A[j]=A[j+1]
                    A[j+1]=aux
                if (A[j][0]==0 and A[j][1]==0)or(A[j+1][0]==0 and A[j+1][1]==0):
                    bandera = 1
    if bandera == 1:
        A.remove([0,0])
        A.insert(0,[0,0])


def graficar():
    global lim_y,lim_x,lista_funciones
    plt.close("all")
    plt.axhline(y=0, xmin=0, xmax=9,color="k")
    plt.axvline(x=0, ymin=0, ymax=9,color="k")
    aux_x = 0
    while aux_x < (len(lista_restric)):

        if lista_r[aux_x][0][0]=="i":
            
            plt.axhline(y=lista_r[aux_x][1][1], xmin=0, xmax=1)
            aux_x = aux_x+1
            continue
        if lista_r[aux_x][1][1]=="i":    
            plt.axvline(x=lista_r[aux_x][0][0], ymin=0, ymax=1)
            aux_x = aux_x+1
            continue
        #Prueba 1
        def graficiar_3(B,b):
            b = int(b)
            def funcion_2(x):
                
                return eval(str(B))
            
            mu= range(0,10+b)
            plt.plot(mu,[funcion_2(i) for i in mu])

        def graficar_2(A):
            
            if A[0][0]==0 or A[1][1]==0:
                return
            else:
                m = (float(A[1][1]-0))/(-(float(A[0][0])))
                b= -(m*float(A[0][0]))+0
                funcion = str(m)+"*x+"+str(b)
            
            graficiar_3(funcion,b)        

        graficar_2(lista_r[aux_x])
        
        #Fin de prueba
        #plt.plot(lista_r[aux_x][0],lista_r[aux_x][1])
        aux_x = aux_x+1

    for i in range(len(lista_p)):
        if lista_p[i][0]>=0 and lista_p[i][1]>=0 :
            plt.plot(lista_p[i][0],lista_p[i][1], marker="o", color="red")


    burbuja(lista_region)
    #print(lista_region)
    lista_c_x=[]
    lista_c_y=[]

    for i in range(len(lista_region)):
        lista_c_x.append(float(lista_region[i][0]))
        lista_c_y.append(float(lista_region[i][1]))

    if len(lista_region)>1:
        lista_c_x.append(lista_c_x[0])
        lista_c_y.append(lista_c_y[0])

        plt.fill_between(lista_c_x,lista_c_y,color="cyan")

        plt.plot(p_solucion[0][0],p_solucion[0][1], marker="o", color="green")

    p_solucion.clear()
    lista_c_x.clear()
    lista_c_y.clear()
    #plt.fill_between(,color="green")
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")

  

    lim_x = int(round(lim_x))
    lim_y = int(round(lim_y))

    lim_x = int(lim_x + (lim_x))
    lim_y = int(lim_y + (lim_y))

    if lim_x>10  and lim_y>10:
        plt.xlim(0,lim_x)
        plt.ylim(0,lim_y)
    lim_x=0
    lim_y=0
    plt.show()

def calcular():
    
    mayor_c=-9999
    mini_c = 9999
    posicion = 0
    #print(lista_region)
    if max_min == 0:
        for i in range(len(lista_region)):
            x= lista_region[i][0]
            y= lista_region[i][1]
            if eval(funcion)>mayor_c:
                
                mayor_c = eval(funcion)
                posicion = i
    elif max_min == 1:
        for i in range(len(lista_region)):
            x= lista_region[i][0]
            y= lista_region[i][1]
            if eval(funcion)<mini_c:
                
                mini_c = eval(funcion)
                posicion = i
    cartel013["fg"]="green"
    cartel013["text"]="La solucion es : "+str(lista_region[posicion])

    if len(lista_region)==1 and max_min == 0:
        cartel013["fg"]="yellow"
        cartel013["text"]="La solucion es : "+str(lista_region[posicion]) + "Pero no esta acotado"

    p_solucion.append(lista_region[posicion])

ventana.mainloop()
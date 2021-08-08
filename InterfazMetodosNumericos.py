import tkinter as tk
import tkinter.font as tkFont
from math import *
#import numpy as np Esta libreria esta rara



ventana = tk.Tk()

color  = '#%02x%02x%02x' % (174, 214, 241)
ventana.title("Biseccion +Regula Falsi")
ventana.geometry("390x500")
ventana.resizable(width=False, height=False)
ventana.configure(bg=color)


imga = tk.PhotoImage(file="fondo_1.gif")
panel = tk.Label(ventana, image = imga)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#backend
def close_window(): 
    ventana.destroy()

def f(x):
    funcion = real_cartel.get()
    return eval(funcion)

def metodo_biseccion():
    a=float(min.get())
    b=float(max.get())
    tol = float(error.get())
    m1 = a
    m = b
    k = 0

    
    while(abs(m1-m)>tol):
        m1=m
        m = (a+b)/2
        if(f(a)*f(m)<0): #Cambia de signo en [a,m]
            b = m
        if(f(m)*f(b)<0): #Cambia de signo en [m,b]
            a = m
        k = k+1

    pasos["text"]="x"+str(k)
    resultado["text"]=str(round(m,5))
    segmento["text"]=str(round(abs(a-b),8))
    

def metodo_regla_f():
    m_1 = float(min.get())
    m_2 = float(max.get())
    error_1 = float(error.get())
    k = 0
    seg=abs(m_2-m_1)
    #Procedimiento
    while not(seg<=error_1):
        fa = f(m_1)
        fb = f(m_2)
        c = m_2 - fb*(m_1-m_2)/(fa-fb)
        fc = f(c)
        
        cambio =  fa*fc
        
        if cambio>0:
            seg = abs(c-m_1)
            m_1 = c
        else:
            seg = abs(c-m_2)
            m_2 = c
        k = k +1
        
    pasos["text"]="x"+str(k)
    resultado["text"]=str(round(c,5))
    segmento["text"]=str(round(abs(m_2-m_1),8))

def verificacion():
    try:
        x= 1
        funcion = real_cartel.get()
        y=eval(funcion)
        a=float(min.get())
        b=float(max.get())
        des = int(variable.get())
        error_1 = float(error.get())
    except:
        nota["fg"]="red"
        nota["text"]= "Nota:            Datos erroneos   "
        pasos["text"]=" "
        resultado["text"]=" "
        segmento["text"]=" "
        return 0

    if(f(a)*f(b)>0):
        nota["fg"]="red"
        nota["text"]="Nota:  La funcion no cambia de signo  "
        pasos["text"]=" "
        resultado["text"]=" "
        segmento["text"]=" "
        return 0
    return 1

def resolucion():
    if verificacion() != 1:
        return
    nota["fg"]="green"
    nota["text"]="Nota de error:   Sin errores   "
    des = int(variable.get())
    if des == 1 :
        metodo_biseccion()
    else :
        metodo_regla_f()


#Front-end
#Titulo
letra = tkFont.Font(family="Lucida Grande", size=12)
letra2 = tkFont.Font(family="Lucida Grande", size=8)
letra3 = tkFont.Font(family="Lucida Grande", size=21)
letra4 = tkFont.Font(family="Lucida Grande", size=15)
titulo = tk.Label(ventana,text="Metodo de Bisección y La Regla Falsa",bg=color,fg ="black",width=31,font=letra4,anchor="nw")
titulo.place(x=22,y=5)

#Pedir datos
cartel1 = tk.Label(ventana,text="Formula [f(x)]",bg=color,fg ="black",width=13,font=letra2)
real_cartel =  tk.Entry(ventana,text="",bg="white",width=21,font=letra3)
cartel1.place(x=25,y=55)
real_cartel.place(x=25,y=80)
#Limites y error
min_1 = tk.Label(ventana,text="Valor inicial x0",bg=color,fg ="black",width=13,font=letra2)
max_1 = tk.Label(ventana,text="Valor final x1",bg=color,fg ="black",width=13,font=letra2)
error_1 = tk.Label(ventana,text="Error min",bg=color,fg ="black",width=13,font=letra2)

min =  tk.Entry(ventana,text="",bg="white",width=9,font=letra)
max =  tk.Entry(ventana,text="",bg="white",width=9,font=letra)
error =  tk.Entry(ventana,text="",bg="white",width=9,font=letra)

min_1.place(x=25,y=135)
max_1.place(x=155,y=135)
error_1.place(x=280,y=135)

min.place(x=25,y=160)
max.place(x=155,y=160)
error.place(x=280,y=160)

#Metodos
variable = tk.StringVar()
variable.set(None)
radiobutton1 = tk.Radiobutton(text="Bisección", variable=variable, value=1,bg=color)
radiobutton2 = tk.Radiobutton(text="Regla Falsa", variable=variable, value=2,bg=color)
radiobutton1.place(x=95,y=200)
radiobutton2.place(x=215,y=200)

#Botones
calcular = tk.Button(ventana,text="Calcular",width=10,fg="black",heigh=2,bg=color,command=lambda :resolucion())
calcular.place(x=155,y=240)
Salir = tk.Button(ventana,text="Salir",width=10,fg="black",bg=color,heigh=2,command=lambda : close_window())
Salir.place(x=155,y=425)

#Resultados
cartel1 = tk.Label(ventana,text="Paso xn",bg=color,fg ="black",width=13,font=letra2)
cartel2 = tk.Label(ventana,text="  x  ",bg=color,fg ="red",width=13,font=letra2)
cartel3 = tk.Label(ventana,text="|x(i) - x(i-1)|",bg=color,fg ="black",width=13,font=letra2)


pasos = tk.Label(ventana,text=" ",bg="white",fg ="black",width=13,font=letra2)
resultado = tk.Label(ventana,text=" ",bg="white",fg ="red",width=13,font=letra2)
segmento = tk.Label(ventana,text=" ",bg="white",fg ="black",width=13,font=letra2)

cartel1.place(x=25,y=300)
cartel2.place(x=155,y=300)
cartel3.place(x=280,y=300)

pasos.place(x=25,y=325)
resultado.place(x=155,y=325)
segmento.place(x=280,y=325)

#Nota
nota = tk.Label(ventana,text="Nota de error:   Sin errores   ",bg="white",fg ="Green",width=30,font=letra4,anchor="nw")
nota.place(x=22,y=380)


ventana.mainloop()

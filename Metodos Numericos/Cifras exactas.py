import tkinter as tk
from tkinter.constants import END, TRUE
import tkinter.font as tkFont
from decimal import Decimal

import os


ventana = tk.Tk()

color = '#%02x%02x%02x' % (31, 97, 141)
color2 = '#%02x%02x%02x' % (133, 193, 233)
ventana.title("Cifras Exactas")
ventana.geometry("300x330")
ventana.resizable(width=False, height=False)
ventana.configure(bg=color)

imga = tk.PhotoImage(file="Fondo2.gif")
panel = tk.Label(ventana, image = imga)
panel.pack(side = "bottom", fill = "both", expand = "yes")

def close_window(): 
    ventana.destroy()

def borrar_button():
    resultado_cartel3["text"]=""
    resultado_cartel2["text"]=""
    real_cartel.delete(0, END)
    aproximado_cartel.delete(0, END)

#back-end
def calcular_button():

    exacta = Decimal(real_cartel.get())
    aproximado = Decimal(aproximado_cartel.get())
    error=abs(exacta-aproximado)
    notacion = 0
    aux_n=0
    if error >=1:
        notacion = len(str(exacta))
        exacta = exacta/(10**notacion)
        aproximado = aproximado/(10**notacion)
        error = abs(exacta-aproximado)
        aux_n=1
    
    auxiliar = 0
    contador = 0
    numero = ""
    contador_cifras = 0
    contador_decimales = 0
    
    y = len(str(int(aproximado)))
    
    for x in range(len(str(format(error,'.10f')))-1):
        
        if error <= 0.05/((10**x)):
            contador +=1

    if contador>=1:
        auxiliar = contador + y

    for x in range(auxiliar+1):
        try:
            numero +=str(aproximado)[x]
        except:
            contador_cifras= y
            contador_decimales = 0
            contador = 0
            break
    
    resultado_cartel2["text"]=numero
    if contador>=1:
        contador_cifras = y +contador
        contador_decimales =  contador
    if aux_n==1:
        numero = Decimal(numero) * (10**notacion)
        resultado_cartel2["text"]=numero
        contador_cifras = len(str((1*10**notacion-1)))
        contador_decimales = 0
    frase = "Hay "+str(contador_cifras)+" cifras exactas y Hay  "+str(contador_decimales)+" cifras de decimales exactas"
    resultado_cartel3["text"]=frase
    

#Front-end

#Titulo
letra = tkFont.Font(family="Lucida Grande", size=15)
letra2 = tkFont.Font(family="Lucida Grande", size=8)
letra3 = tkFont.Font(family="Lucida Grande", size=9)
titulo = tk.Label(ventana,text="Cifras Exactas",bg=color,fg ="white",width=13,font=letra)
titulo.place(x=70,y=5)

#Pedir datos
cartel1 = tk.Label(ventana,text="Medida real (x*)",bg=color,fg ="white",width=13,font=letra2)
real_cartel =  tk.Entry(ventana,text="",bg="white",width=16,font=letra3)
cartel1.place(x=25,y=55)
real_cartel.place(x=10,y=80)
cartel2 = tk.Label(ventana,text="Medida aproximada (x)",bg=color,fg ="white",width=17,font=letra2)
aproximado_cartel =  tk.Entry(ventana,text="",bg="white",width=16,font=letra3)
cartel2.place(x=167,y=55)
aproximado_cartel.place(x=165,y=80)
#Boton
calcular = tk.Button(ventana,text="Calcular",width=10,fg="black",bg=color2,heigh=2,command=lambda : calcular_button())
calcular.place(x=105,y=120)
borrar = tk.Button(ventana,text="Borrar",width=10,fg="black",bg=color2,heigh=2,command=lambda : borrar_button())
#borrar.place(x=165,y=120)
Salir = tk.Button(ventana,text="Salir",width=10,fg="black",bg=color2,heigh=2,command=lambda : close_window())
Salir.place(x=105,y=280)

#Resultados
resultado_cartel = tk.Label(ventana,text="Cifras Exactas del numero(x)",bg=color,fg ="white",width=22)
resultado_cartel.place(x=3,y=200)
resultado_cartel2 = tk.Label(ventana,text="",bg="white",fg ="black",width=15)
resultado_cartel2.place(x=180,y=200)
resultado_cartel3 = tk.Label(ventana,text="",bg=color,fg ="white",width=41,anchor="nw")
resultado_cartel3.place(x=3,y=250)

ventana.mainloop()
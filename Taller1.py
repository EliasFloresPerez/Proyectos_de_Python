import tkinter as tk
from tkinter.constants import END, TRUE
import tkinter.font as tkFont
from decimal import Decimal
ventana = tk.Tk()

color = '#%02x%02x%02x' % (31, 97, 141)
color2 = '#%02x%02x%02x' % (133, 193, 233)
ventana.title("Cifras Exactas")
ventana.geometry("350x300")
ventana.resizable(width=False, height=False)
ventana.configure(bg=color)

def borrar_button():
    cuadro1["text"]=""
    cuadro2["text"]=""
    cuadro3["text"]=""
    real_cartel.delete(0, END)
    aproximado_cartel.delete(0, END)

#back-end
def calcular_button():
    numero = Decimal(real_cartel.get())
    aprox =  Decimal(aproximado_cartel.get())
    error = abs(numero-aprox)
 
    n2=0
    punto = 0

    for i in range(len(str(error))):
        if str(error)[i]=="." or n2 !=0:
            if str(error)[i]==".":
                punto = i
            continue 

        if str(error)[i]!="0":
            n2 = i


    
    cuadro1["text"]=str(aprox)[0:n2-1+len(str(int(aprox)))]
    cuadro2["text"]=n2-2+len(str(int(aprox)))
    cuadro3["text"]=len(str(aprox)[str(aprox).index("."):n2-1+len(str(int(aprox)))])-1
    if punto == 0:
        cuadro3["text"]=""

#Front-end

#Titulo
letra = tkFont.Font(family="Lucida Grande", size=20)
letra2 = tkFont.Font(family="Lucida Grande", size=11)
letra3 = tkFont.Font(family="Lucida Grande", size=13)
titulo = tk.Label(ventana,text="Cifras Exactas",bg=color,fg ="white",width=13,font=letra)
titulo.place(x=70,y=5)

#Pedir datos
cartel1 = tk.Label(ventana,text="Medida real (x*)",bg=color,fg ="white",width=13,font=letra2)
real_cartel =  tk.Entry(ventana,text="",bg="white",width=16,font=letra3)
cartel1.place(x=25,y=55)
real_cartel.place(x=10,y=80)
cartel2 = tk.Label(ventana,text="Medida aproximada (x)",bg=color,fg ="white",width=17,font=letra2)
aproximado_cartel =  tk.Entry(ventana,text="",bg="white",width=16,font=letra3)
cartel2.place(x=180,y=55)
aproximado_cartel.place(x=185,y=80)
#Boton
calcular = tk.Button(ventana,text="Calcular",width=10,fg="black",bg=color2,heigh=2,command=lambda : calcular_button())
calcular.place(x=50,y=120)
borrar = tk.Button(ventana,text="Borrar",width=10,fg="black",bg=color2,heigh=2,command=lambda : borrar_button())
borrar.place(x=220,y=120)

#Resultados
cifras_cartel = tk.Label(ventana,text="Cifras Exactas:",bg=color,fg ="black",width=13,font=letra2,anchor ="nw")
digitos_cartel2 = tk.Label(ventana,text="#Cifras exactas:",bg=color,fg ="black",width=13,font=letra2,anchor ="nw")
duda_cartel = tk.Label(ventana,text="#Dec exactas:",bg=color,fg ="black",width=13,font=letra2,anchor ="nw")
cifras_cartel.place(x=30,y=180)
digitos_cartel2.place(x=30,y=210)
duda_cartel.place(x=30,y=240)

cuadro1 = tk.Label(ventana,text="",bg="white",fg ="black",width=15,font=letra2,anchor ="nw")
cuadro2 = tk.Label(ventana,text="",bg="white",fg ="black",width=15,font=letra2,anchor ="nw")
cuadro3 = tk.Label(ventana,text="",bg="white",fg ="black",width=15,font=letra2,anchor ="nw")
cuadro1.place(x=160,y=180)
cuadro2.place(x=160,y=210)
cuadro3.place(x=160,y=240)

ventana.mainloop()
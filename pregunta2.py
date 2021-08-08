import tkinter as tk
from tkinter.constants import END, TRUE
import tkinter.font as tkFont
from decimal import Decimal
ventana = tk.Tk()

color = '#%02x%02x%02x' % (133, 193, 233)
color2 = '#%02x%02x%02x' % (31, 97, 141)
ventana.title("Numeros aproximados")
ventana.geometry("325x400")
ventana.resizable(width=False, height=False)
ventana.configure(bg=color)

imga = tk.PhotoImage(file="Fondo2.gif")
panel = tk.Label(ventana, image = imga)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#back-end
def close_window(): 
    ventana.destroy()

def error_ab(num):
    numero = Decimal(medida_cartel.get())
    error =  error_cartel.get()
    if num == 2 or num ==4:
        error= Decimal(error_cartel.get()) * Decimal(medida_cartel.get()) 


    n2=0
    punto = 0

    for i in range(len(str(error))):
        if str(error)[i]=="." or n2 !=0:
            if str(error)[i]==".":
                punto = i
            continue 

        if str(error)[i]!="0":
            n2 = i

    if num == 3 or num == 4:
        if Decimal(error) <= (Decimal(error)/5*(10**n2))*10:
            n2 +=1

       
    cuadro2["text"]=str(numero)[str(numero).index("."):n2-1+len(str(int(numero)))]
    cuadro1["text"]=str(numero)[0:n2-1+len(str(int(numero)))]
    cuadro3["text"]=str(numero)[n2-1+len(str(int(numero))):]


def desicion():
    des = int(variable.get())
    
    if des == 1:
        error_ab(1)
    elif des ==2:
        error_ab(2)
    elif des==3:
        error_ab(3)
    elif des==4:
        error_ab(4)
    else:
        print("escoja una opcion")


#Titulo
letra = tkFont.Font(family="Lucida Grande", size=20)
letra2 = tkFont.Font(family="Lucida Grande", size=11)
letra3 = tkFont.Font(family="Lucida Grande", size=13)
titulo = tk.Label(ventana,text="Números Aprox",bg=color,fg ="black",width=13,font=letra)
titulo.place(x=70,y=5)

#Label del valor exacto
variable = tk.StringVar()
variable.set(None)
cartel1 = tk.Label(ventana,text="Medida (x):",bg=color,fg ="black",width=13,font=letra2,anchor ="nw")
medida_cartel =  tk.Entry(ventana,text="",bg="white",width=16,font=letra3)
cartel1.place(x=55,y=55)
medida_cartel.place(x=130,y=55)

cartel2 = tk.Label(ventana,text="Error:",bg=color,fg ="black",width=13,font=letra2,anchor ="nw")
error_cartel =  tk.Entry(ventana,text="",bg="white",width=16,font=letra3)
cartel2.place(x=55,y=85)
error_cartel.place(x=130,y=85)
radiobutton1 = tk.Radiobutton(text="E(x)", variable=variable, value=1,bg=color)
radiobutton2 = tk.Radiobutton(text="e(x)", variable=variable, value=2,bg=color)
radiobutton3 = tk.Radiobutton(text="Em(x)", variable=variable, value=3,bg=color)
radiobutton4 = tk.Radiobutton(text="em(x)", variable=variable, value=4,bg=color)
radiobutton1.place(x=75,y=120)
#radiobutton2.place(x=175,y=115)
radiobutton3.place(x=175,y=120)
#radiobutton3.place(x=75,y=135)
#radiobutton4.place(x=175,y=135)

#Boton
calcular = tk.Button(ventana,text="Calcular",width=10,fg="black",heigh=2,bg=color2,command=desicion)
calcular.place(x=118,y=170)
Salir = tk.Button(ventana,text="Salir",width=10,fg="black",bg=color2,heigh=2,command=lambda : close_window())
Salir.place(x=118,y=330)

#Resultados
cifras_cartel = tk.Label(ventana,text="Cifras Exactas:",bg=color,fg ="black",width=13,font=letra2,anchor ="nw")
digitos_cartel2 = tk.Label(ventana,text="Cifras decimales:",bg=color,fg ="black",width=13,font=letra2,anchor ="nw")
duda_cartel = tk.Label(ventana,text="Cifras dudosas",bg=color,fg ="black",width=13,font=letra2,anchor ="nw")
cifras_cartel.place(x=30,y=240)
#digitos_cartel2.place(x=30,y=260)
duda_cartel.place(x=30,y=270)

cuadro1 = tk.Label(ventana,text="",bg="white",fg ="black",width=15,font=letra2,anchor ="nw")
cuadro2 = tk.Label(ventana,text="",bg="white",fg ="black",width=15,font=letra2,anchor ="nw")
cuadro3 = tk.Label(ventana,text="",bg="white",fg ="black",width=15,font=letra2,anchor ="nw")
cuadro1.place(x=160,y=240)
#cuadro2.place(x=160,y=260)
cuadro3.place(x=160,y=270)

ventana.mainloop()
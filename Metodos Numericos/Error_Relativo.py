import tkinter as tk
from tkinter.constants import END, TRUE
import tkinter.font as tkFont
from decimal import Decimal
import math
 


ventana = tk.Tk()

color = '#%02x%02x%02x' % (245, 176, 65)
color2 = '#%02x%02x%02x' % (230, 126, 34)
ventana.title("Relativo Absoluto y Relativo minimo")
ventana.geometry("325x400")
ventana.resizable(width=False, height=False)
ventana.configure(bg=color)


#Back-end


def calcular_b():
        numero1=medida_cartel.get()
        numero2=numero_cartel.get()
        des=int(variable.get())
        

        numero2=int(numero2)
        n1_1=float(numero1)
        total = 0
        exacto = 0
        error_max = 0
        desp =""
        decimal, entera = math.modf(n1_1)
        if des==1:
            
            if entera>0 and decimal==0:
                total=len(numero1)
                exacto=numero2
                error_max=0.5*10**(len(numero1)-numero2)
            elif entera==0 and decimal>0:
                total=len(numero1)
                exacto=2+numero2
                error_max=0.5*10**-numero2
            elif decimal>0 and entera>0:
                total=len(str(numero1))
                exacto=numero2+1
                aux=len(str(entera))-2
                error_max=0.5*10**-(numero2-aux)
        
        elif des==2:
            total=len(str(numero1))
            exacto=len(str(entera))+numero2-1
            error_max=0.5*10**-numero2
        else:
            cuadro3["text"]=(str("Selecione un #N"))
            return 

        em=error_max/float(numero1)

        for i in range(total):
            if i >= exacto:
                desp +=str(numero1)[i]
 


        cuadro1["text"]=(str(error_max)) 
        cuadro2["text"]=(str(format(em,'.9f'))) 
        cuadro3["text"]=(str(desp)) 

def borrar_all():
    cuadro1["text"]=""
    cuadro2["text"]=""
    cuadro3["text"]=""
    variable.set(None)
    medida_cartel.delete(0, END)
    numero_cartel.delete(0, END)


#Titulo
letra = tkFont.Font(family="Lucida Grande", size=20)
letra2 = tkFont.Font(family="Lucida Grande", size=11)
letra3 = tkFont.Font(family="Lucida Grande", size=13)
titulo = tk.Label(ventana,text="Números Aprox",bg=color,fg ="black",width=13,font=letra)
titulo.place(x=70,y=5)

#Label del valor exacto
variable = tk.StringVar()
variable.set(None)
cartel1 = tk.Label(ventana,text="Numeros Aproximados",bg=color,fg ="black",width=17,font=letra2,anchor ="nw")
medida_cartel =  tk.Entry(ventana,text="",bg="white",width=16,font=letra3)
cartel1.place(x=5,y=55)
medida_cartel.place(x=160,y=55)
numero_cartel =  tk.Entry(ventana,text="",bg="white",width=5,font=letra)
numero_cartel.place(x=130,y=120)


radiobutton1 = tk.Radiobutton(text="N Cifras Exactas", variable=variable, value=1,bg=color)
radiobutton2 = tk.Radiobutton(text="N Cifras Decimales Exactas", variable=variable, value=2,bg=color)
radiobutton1.place(x=110,y=80)
radiobutton2.place(x=110,y=100)


#Boton
calcular = tk.Button(ventana,text="Calcular",width=10,fg="black",heigh=2,bg=color2,command=calcular_b)
calcular.place(x=75,y=165)
borrar = tk.Button(ventana,text="Borrar",width=10,fg="black",heigh=2,bg=color2,command = borrar_all)
borrar.place(x=175,y=165)

cifras_cartel = tk.Label(ventana,text="Em(x)",bg=color,fg ="black",width=13,font=letra2,anchor ="ne")
digitos_cartel2 = tk.Label(ventana,text="em(x)",bg=color,fg ="black",width=13,font=letra2,anchor ="ne")
duda_cartel = tk.Label(ventana,text="Cifras dudosas",bg=color,fg ="black",width=13,font=letra2,anchor ="ne")
cifras_cartel.place(x=30,y=230)
digitos_cartel2.place(x=30,y=260)
duda_cartel.place(x=30,y=290)

cuadro1 = tk.Label(ventana,text="",bg="white",fg ="black",width=10,font=letra2,anchor ="nw")
cuadro2 = tk.Label(ventana,text="",bg="white",fg ="black",width=10,font=letra2,anchor ="nw")
cuadro3 = tk.Label(ventana,text="",bg="white",fg ="black",width=10,font=letra2,anchor ="nw")
cuadro1.place(x=160,y=230)
cuadro2.place(x=160,y=260)
cuadro3.place(x=160,y=290)

ventana.mainloop()
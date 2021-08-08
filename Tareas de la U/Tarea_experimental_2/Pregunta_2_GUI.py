import tkinter as tk
import tkinter.font as tkFont
from tkinter.constants import END, TRUE
import os


# Namek Colors rgb(51, 166, 229)
ventana = tk.Tk()
color = '#%02x%02x%02x' % (171, 235, 198)
color2 = '#%02x%02x%02x' % (133, 193, 233)
ventana.title("Calculadora De Impuestos - Sede Namekusei")
ventana.geometry("300x400")
ventana.resizable(width=False, height=False)
ventana.configure(bg=color)

#Imagen
imga = tk.PhotoImage(file="namek.png")
panel = tk.Label(ventana, image = imga)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#back-end
def salir():
    ventana.destroy()

def impuesto():
    try:
        ingreso = float(cartel_1.get())
    except:
        cartel_resultado["text"]="Error al ingresar datos"
        return
    impuesto = 0
    

    #Extencion fiscal
    if ingreso <= 35000:
        impuesto = (ingreso*0.12)-399.2
        
    #Para añiñados
    if ingreso > 35000:
        impuesto = ((ingreso - 35000)*0.24)+3500.2
    
    #Para pobres
    if impuesto < 0:
        impuesto = 0
    
    cartel_resultado["text"]=("El impuesto es: "+str(float(round(impuesto))))


#Frot-end
letra = tkFont.Font(family="Lucida Grande", size=30)
letra2 = tkFont.Font(family="Lucida Grande", size=15)

#Botones
cartel_impues = tk.Label(ventana,text="Ingrese el valor de sus ingresos",bg=color,fg ="black",width=25,font=letra2,anchor="nw")
cartel_1 =  tk.Entry(ventana,text="",bg="white",width=13,font=letra)
button = tk.Button(ventana,text="Calcular",width=10,fg="black",bg=color,heigh=2, command=impuesto)
salir_1 = tk.Button(ventana,text="Salir",width=10,fg="black",bg=color,heigh=2, command=salir)
cartel_resultado = tk.Label(ventana,text="Impuesto :",bg=color,fg ="black",width=25,font=letra2,anchor="nw")

cartel_impues.place(x=5,y=20)
cartel_1.place(x=5,y=50)
button.place(x=120,y=150)
cartel_resultado.place(x=13,y=250)
salir_1.place(x=120,y=320)


ventana.mainloop()
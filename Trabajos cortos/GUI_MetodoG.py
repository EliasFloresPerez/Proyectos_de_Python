import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter.constants import END, TRUE
import os


ventana = tk.Tk()


ventana.title("Metodo Grafico")
ventana.geometry("450x375")
ventana.resizable(width=False, height=False)
#Backend

lista_restric = []
lista_m = []
max_min = 0
funcion = ""

def errores():
    global lista_restric,lista_m,max_min,funcion

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
        
        lista_restric.append(str(restriccion_x1.get())+"*x"+"+"+str(restriccion_x2.get())+"*y"+"-("+str(restriccion_resultado1.get())+")")
        lista_restric.append(str(restriccion_x12.get())+"*x"+"+"+str(restriccion_x22.get())+"*y"+"-("+str(restriccion_resultado2.get())+")")
        lista_restric.append(str(restriccion_x13.get())+"*x"+"+"+str(restriccion_x23.get())+"*y"+"-("+str(restriccion_resultado3.get())+")")
        lista_restric.append(str(restriccion_x14.get())+"*x"+"+"+str(restriccion_x24.get())+"*y"+"-("+str(restriccion_resultado4.get())+")")
        lista_restric.append(str(restriccion_x15.get())+"*x"+"+"+str(restriccion_x25.get())+"*y"+"-("+str(restriccion_resultado5.get())+")")
        
        lista_m.append(combo1.current())
        lista_m.append(combo2.current())
        lista_m.append(combo3.current())
        lista_m.append(combo4.current())
        lista_m.append(combo5.current())

        max_min =combo.current()
        x=0
        y=0
        for i in lista_restric:
            eval(i)
        eval(funcion)
        return lista_restric,lista_m,max_min,funcion
    except:
        print("Error")
        lista_restric.clear()
        return 1



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

button_enviar = tk.Button(ventana,text="Enviar",width=10,fg="black",bg=color,heigh=2)
button_enviar.place(x=190,y=330)

#METODO GRAFICO




ventana.mainloop()
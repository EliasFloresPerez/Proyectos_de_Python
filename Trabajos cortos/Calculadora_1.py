import tkinter as tk
import tkinter.font as tkFont
import math

ventana = tk.Tk()

color = mycolor = '#%02x%02x%02x' % (20, 40, 51)
ventana.title("Calculadora")
ventana.geometry("390x500")
ventana.resizable(width=False, height=False)
ventana.configure(bg=color)

#Frontend
a = 35
letra = tkFont.Font(family="Lucida Grande", size=35)
letra2 = tkFont.Font(family="Lucida Grande", size=15)
barra = tk.Label(ventana,text="",anchor="se",font=letra,bg="white",width=13)
barra.place(x=20,y=50)
barra2 =tk.Label(ventana,text="",anchor="se",fg="white",font=letra2,bg=color,width=32)
barra2.place(x=20,y=17)

#Botones limpiadores
colora= '#%02x%02x%02x' % (52, 152, 219)
colorx= '#%02x%02x%02x' % (26, 82, 118)
botonC = tk.Button(ventana,text="C",width=18,heigh=3,fg="white",bg=colora, command= lambda : eliminar())
botonC.place(x=20,y=100+a)
botonCE = tk.Button(ventana,text="CE",width=18,heigh=3,fg="white",bg=colora,command= lambda :eliminar_parcial())
botonCE.place(x=160,y=100+a)
botonBack = tk.Button(ventana,text="<--",width=9,fg="white",heigh=3,bg=colora,command = lambda : retroceder())
botonBack.place(x=300,y=100+a)

#Botones de operaciones
colorb = '#%02x%02x%02x' % (33, 97, 140)
#Horizontal
botonsqr = tk.Button(ventana,text="²√",width=11,heigh=3,bg=colorb,fg="white",command=lambda:operacion(5))
botonsqr.place(x=20,y=160+a)
botonpow = tk.Button(ventana,text="x²",width=11,heigh=3,bg=colorb,fg="white",command=lambda:operacion(6))
botonpow.place(x=115,y=160+a)
botonper = tk.Button(ventana,text="%",width=11,heigh=3,bg=colorb,fg="white",command=lambda:operacion(7))
botonper.place(x=210,y=160+a)
#Vertical
botonadd = tk.Button(ventana,text="+",width=9,heigh=3,bg=colorb,fg="white",command=lambda:operacion(1))
botonadd.place(x=300,y=160+a)
botonsub = tk.Button(ventana,text="-",width=9,heigh=3,bg=colorb,fg="white",command=lambda:operacion(2))
botonsub.place(x=300,y=220+a)
botonmul = tk.Button(ventana,text="x",width=9,heigh=3,bg=colorb,fg="white",command=lambda:operacion(3))
botonmul.place(x=300,y=280+a)
botondiv = tk.Button(ventana,text="÷",width=9,heigh=3,bg=colorb,fg="white",command=lambda:operacion(4))
botondiv.place(x=300,y=340+a)
botoneq = tk.Button(ventana,text="=",width=9,heigh=3,bg=colorb,fg="white",command=lambda:igual())
botoneq.place(x=300,y=400+a)

#Botones numerales
#1
boton7 = tk.Button(ventana,text="7",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(7))
boton7.place(x=20,y=220+a)
boton8 = tk.Button(ventana,text="8",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(8))
boton8.place(x=115,y=220+a)
boton9 = tk.Button(ventana,text="9",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(9))
boton9.place(x=210,y=220+a)
#2
boton4 = tk.Button(ventana,text="4",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(4))
boton4.place(x=20,y=280+a)
boton5 = tk.Button(ventana,text="5",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(5))
boton5.place(x=115,y=280+a)
boton6 = tk.Button(ventana,text="6",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(6))
boton6.place(x=210,y=280+a)
#3
boton1 = tk.Button(ventana,text="1",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(1))
boton1.place(x=20,y=340+a)
boton2 = tk.Button(ventana,text="2",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(2))
boton2.place(x=115,y=340+a)
boton3 = tk.Button(ventana,text="3",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(3))
boton3.place(x=210,y=340+a)
#4
boton0 = tk.Button(ventana,text="0",width=38,heigh=3,bg=colora,fg="white",command=lambda: boton(0))
boton0.place(x=20,y=400+a)

#Backend
cadena2 = 0
contador = 0
auxiliar = 1
cadena = []
resultado = "0+"
i =0
#Botones
def boton(num):
    global contador
    global cadena2
    global cadena
    global auxiliar
    global resultado
    global i
    

    if auxiliar  == 2:
       resultado = "" 
       auxiliar = 1

    if auxiliar==1 or auxiliar ==3:
        cadena = []
        cadena2 = ""
        auxiliar = 0
    
    if i == 1:
        cadena.append("-")
        i=0

    if (contador < 13):
        cadena.append(num)
        cadena2 = "".join(map(str,cadena))
        cadena2 = str(int(cadena2))
        barra["text"]=cadena2
        contador = contador +1
    
def operacion(nume):
    global cadena2
    global resultado 
    global auxiliar
    global i
    global contador

    #Para que no marque dos signos al mismo tiempo

    if (auxiliar == 1 or auxiliar==3) and nume==2:
        i=1
        return 

    if auxiliar==1 or auxiliar ==3:
        return

    auxiliar =  1

    contador = 0

    resultado = resultado + cadena2

    try:
        barra["text"] = round(eval(resultado),11)
        resultado = str(eval(resultado))
        barra2["text"] = resultado
    except:
        barra["text"] = "No divida para 0"
        resultado = "0+"

    if nume == 1:
        resultado = resultado + "+"

    if nume == 2:
        resultado = resultado +"-"

    if nume == 3:
        resultado = str(eval(resultado))
        resultado = resultado +"*"

    if nume == 4:
        resultado = str(eval(resultado))
        resultado = resultado +"/"
    if nume == 5:
        resultado = eval(resultado)
        resultado = str(round(math.sqrt((resultado)),11))
        cadena2 = ""
        auxiliar = 0
        igual()
    if nume == 6:
        resultado = eval(resultado)
        resultado = str((resultado**2))
        cadena2 = ""
        auxiliar = 0
        igual()

    if nume == 7:
        resultado = str(eval(resultado))
        resultado = resultado +"%"

    barra2["text"] = resultado


def igual():
    global resultado
    global auxiliar
    global cadena2
    global contador
    global colora
    global color
    global colorb

    if auxiliar == 1 or auxiliar == 3:
        return 

    resultado = resultado + cadena2 

    try:
        barra["text"] = round(eval(resultado),11)
        barra2["text"] = resultado

    except:
        barra["text"] = "No divida para 0"
        resultado = "0+0"

    if round(eval(resultado),11)== 0.00031818182:
        cambia_color(202, 111, 30 ,230, 126, 34,244, 208, 63)

    if round(eval(resultado),11)== 0.00041645844:
        cambia_color(14, 102, 90  ,69, 179, 157,17, 122, 101)

    auxiliar = 2
    cadena2=""
    resultado = str(eval(resultado))
    contador = 0

def eliminar():
    global cadena
    global cadena2
    global resultado
    global auxiliar
    global contador

    cadena = []
    cadena2 = ""
    resultado ="0+"
    auxiliar = 1
    contador = 0
    barra["text"]="0"
    barra2["text"]= ""   



def eliminar_parcial():

    global auxiliar
    global contador


    if auxiliar == 2:
        eliminar()

    contador = 0
    auxiliar = 3
    barra["text"]="0"

def retroceder():
    global auxiliar
    global cadena2
    global contador
    global cadena

    if auxiliar == 2:
        eliminar()
    else:
        if contador > 0:
            contador = contador -1
        if len(cadena) != 0:
            cadena.pop()
            cadena2 = "".join(map(str,cadena))
            barra["text"]=cadena2

def cambia_color(a,b,c,d,e,f,g,h,i):
    color_w =  '#%02x%02x%02x' % (a, b, c)
    color_i =  '#%02x%02x%02x' % (d, e, f)
    color_e =  '#%02x%02x%02x' % (g, h, i)

    ventana.configure(bg=color_w)
    ventana.title("Calculadora _Premium_")
    barra2["bg"]=color_w

    #Color_i
    botonC["bg"]=color_i
    botonCE["bg"]=color_i
    botonBack["bg"]=color_i
    boton9["bg"]=color_i
    boton8["bg"]=color_i
    boton7["bg"]=color_i
    boton6["bg"]=color_i
    boton5["bg"]=color_i
    boton4["bg"]=color_i
    boton3["bg"]=color_i
    boton2["bg"]=color_i
    boton1["bg"]=color_i
    boton0["bg"]=color_i

    #Color_e
    botonsqr["bg"]=color_e
    botonpow["bg"]=color_e
    botonper["bg"]=color_e
    botonadd["bg"]=color_e
    botondiv["bg"]=color_e
    botonmul["bg"]=color_e
    botonsub["bg"]=color_e
    botoneq["bg"]=color_e

    #Negro
        #Color_i
    botonC["fg"]="black"
    botonCE["fg"]="black"
    botonBack["fg"]="black"
    boton9["fg"]="black"
    boton8["fg"]="black"
    boton7["fg"]="black"
    boton6["fg"]="black"
    boton5["fg"]="black"
    boton4["fg"]="black"
    boton3["fg"]="black"
    boton2["fg"]="black"
    boton1["fg"]="black"
    boton0["fg"]="black"

    #Color_e
    botonsqr["fg"]="black"
    botonpow["fg"]="black"
    botonper["fg"]="black"
    botonadd["fg"]="black"
    botondiv["fg"]="black"
    botonmul["fg"]="black"
    botonsub["fg"]="black"
    botoneq["fg"]="black"




ventana.mainloop()
from Calculadora import cambia_color
import tkinter as tk
from tkinter.constants import COMMAND
import tkinter.font as tkFont

def pyScale2():
    root = tk.Tk()
    root.geometry("350x410")
    color_fon = '#%02x%02x%02x' % (67, 30, 250)
    root.configure(bg=color_fon)
    root.resizable(width=False, height=False)

    
    def ver(i,j,k):
        color_c='#%02x%02x%02x' % (i, j, k)
        caja_rgb2=tk.Label(root,text="",bg=color_c,width=25,height=5)
        caja_rgb2.place(x=90,y=210)

    def click(self):
        i=0
        j=0
        k=0
        try:
            s1.set(int(rojo_F.get()))
            i=int(rojo_F.get())
            if i > 250 : i = 250
            if i < 0 :  i = 0
        except:
            s1.set(0)
            i=0
        try:
            s2.set(int(verde_F.get()))
            j=int(verde_F.get())
            if j > 250 : j = 250
            if j < 0 :  j = 0
        except:
            s2.set(0)
            j=0
        try:
            s3.set(int(azul_F.get()))
            k=int(azul_F.get())
            if k > 250 : k = 250
            if k < 0 :  k = 0
        except:
            s3.set(0)
            k=0
        ver(i,j,k)


    def formularios(auxiliar,num):
        if auxiliar == 1:
            rojo_F.delete(0,tk.END)
            rojo_F.insert(0,num)
        if auxiliar == 2:
            verde_F.delete(0,tk.END)
            verde_F.insert(0,num)
        if auxiliar == 3:
            azul_F.delete(0,tk.END)
            azul_F.insert(0,num)
        click("Hola")
    
    def recoger(labe):
        lista = [s1.get(),s2.get(),s3.get()]
        labe["text"]=lista

    def enviar_datos(tipo):
        listo = ""
        color_ui="white"
        color_ue="white"
        if tipo == 0:
            listo = (fondo["text"]+" "+color_bo["text"])
            archivo = open("Colores.txt","w")
            archivo.write(listo)
            archivo.close()
            listo = listo.split(' ')
            print(listo)
            if((int(listo[0])+int(listo[1])+int(listo[2]))>=250):
                color_ue = "black"
            if((int(listo[3])+int(listo[4])+int(listo[5]))>=250):
                color_ui = "black"

            cambia_color(int(listo[0]),int(listo[1]),int(listo[2]),int(listo[3]),int(listo[4]),int(listo[5]),color_ue,color_ui)
        if tipo == 1:
            cambia_color(230, 126, 34,244, 208, 63,"black","black")
        if tipo == 2:
            cambia_color(20, 40, 51,33, 97, 140,"black","black")
        if tipo == 3:
            cambia_color(17, 122, 101,69, 179, 157,"black","black")
        if tipo == 4:
            cambia_color(["text"])
            cambia_color(["text"])        
    
    color_back = '#%02x%02x%02x' % (71, 76, 250)
    letra2 = tkFont.Font(family="Lucida Grande", size=15)
    tema = tk.Label(root,text="Colores de la Calculadora (RGB)",fg="white",bg=color_fon,font=letra2,width=32)
    tema.place(x=0,y=10)

    caja_rbg=tk.Label(root,text="",bg=color_back,width=46,height=17)
    caja_rbg.place(x=10,y=45)

    ver(250,250,250)
    #Rojo
    rojo = tk.Label(root,text="R:",font=letra2,fg="white",bg=color_back,width=2)
    rojo.place(x=10,y=55)
    rojo_F = tk.Entry(root,text="",bg="white",width=5,font=letra2)
    rojo_F.place(x=50,y=55)
    s1 = tk.Scale(root, from_=0, to=250, tickinterval=0, bg="red",fg="white", orient=tk.HORIZONTAL, length=200,command=lambda x: formularios(1,s1.get()))
    s1.place(x=120,y=50)

    #Verde
    verde = tk.Label(root,text="G:",font=letra2,fg="white",bg=color_back,width=2)
    verde.place(x=10,y=105)
    verde_F = tk.Entry(root,text="",bg="white",width=5,font=letra2)
    verde_F.place(x=50,y=105)
    s2 = tk.Scale(root, from_=0, to=250, tickinterval=0, bg="green",fg="white", orient=tk.HORIZONTAL, length=200,command=lambda x: formularios(2,s2.get()))
    s2.place(x=120,y=100)

    #Azul
    azul = tk.Label(root,text="B:",font=letra2,fg="white",bg=color_back,width=2)
    azul.place(x=10,y=155)
    azul_F = tk.Entry(root,text="",bg="white",width=5,font=letra2)
    azul_F.place(x=50,y=155)
    s3 = tk.Scale(root, from_=0, to=250, tickinterval=0, bg="blue",fg="white", orient=tk.HORIZONTAL, length=200,command=lambda x: formularios(3,s3.get()))
    s3.place(x=120,y=150)

    #N1 Guardar color de backgroung
    n1 = tk.Button(root,text="Color fondo",width=10,fg="white",heigh=1,bg=color_back ,command= lambda : recoger(fondo))
    n1.place(x=10,y=310)
    fondo = tk.Label(root,text="",bg="white",width=9,height=1)
    fondo.place(x=95,y=312)

    #N2 Guardar Colores de los Botones
    n2 = tk.Button(root,text="Color Botones",width=10,fg="white",heigh=1,bg=color_back,command= lambda : recoger(color_bo))
    n2.place(x=180,y=310)
    color_bo = tk.Label(root,text="",bg="white",width=9,height=1)
    color_bo.place(x=265,y=312)

    
    #Calido
    calido = tk.Button(root,text="Calido",width=9,fg="white",heigh=1,bg=color_back,command= lambda: enviar_datos(1))
    calido.place(x=10,y=345)
    #Frio
    frio = tk.Button(root,text="Frio",width=9,fg="white",heigh=1,bg=color_back,command= lambda: enviar_datos(2))
    frio.place(x=90,y=345)
    #Bosque
    bosque = tk.Button(root,text="Bosque",width=9,fg="white",heigh=1,bg=color_back,command= lambda: enviar_datos(3))
    bosque.place(x=10,y=375)
    #Rainbow
    rainbow = tk.Button(root,text="Rainbow",width=9,fg="white",heigh=1,bg=color_back,command= lambda: enviar_datos(4))
    rainbow.place(x=90,y=375)
    #enviar
    enviar = tk.Button(root,text="Enviar",width=9,fg="white",heigh=2,bg=color_back,command= lambda: enviar_datos(0))
    enviar.place(x=268,y=360)

    
    #rojo_F.bind('<FocusIn>',click)
    rojo_F.bind("<KeyRelease>",click)
    verde_F.bind("<KeyRelease>",click)
    azul_F.bind("<KeyRelease>",click)
    
    
    tk.mainloop()



pyScale2()

from tkinter import *
from tkinter import messagebox
def mensaje():
    messagebox.showinfo(message="Hola soy un mensaje")
    #showerror


raiz = Tk()
raiz.title('Taller Gratuito')
raiz.iconbitmap('calculadora.ico')
raiz.geometry('600x400')
#Frame
miframe = Frame()

miframe.pack(expand=True,fill="both")
miframe.config(bg="red")

miframe.config(width=400,height=200)

#Label
Label(miframe,text="hola mundo").grid(row=1,column=0)

Entry(miframe).grid(row=1,column=1)

Button(miframe,text="Guardar",command=mensaje).grid(row=5,column=3)

raiz.mainloop()
import tkinter as tk
from tkinter.constants import RIGHT
ventana = tk.Tk()

ventana.title("python+ TKinter")
ventana.geometry("400x400")

def saludo():
    text2=caja.get()
    etiqueta ["text"]=text2
    etiqueta.pack(fill=tk.X)

etiqueta = tk.Label(ventana,text = "Aqui va ir tu texto",bg="yellow")
etiqueta.place(x=200,y=100)

caja = tk.Entry(ventana)
caja.pack()

boton = tk.Button(ventana,text = "Enviar",command=saludo)
boton.pack()

ventana.mainloop()
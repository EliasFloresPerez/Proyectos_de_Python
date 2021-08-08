numero = 4.1255
error =  0.002
n2=0
for i in range(len(str(error))):
    if str(error)[i]=="." or n2 !=0:
        continue 

    if str(error)[i]!="0":
         n2 = i
         
logo = tk.PhotoImage(file='fondo.gif')
fondo = tk.Label(ventana,width=350,image=logo)
fondo.pack()
        
cifras_exactas = str(numero)[0:n2]
print(cifras_exactas)
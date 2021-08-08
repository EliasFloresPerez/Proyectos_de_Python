'''Calcule y muestre el promedio de un grupo de datos que se ingresa por teclado.
Deberá solicitar la cantidad de datos a ingresar y luego se pedirá esa cantidad de veces
los datos para hacer el cálculo correspondiente'''

#logica : Pedir datos y ese dato ponerlo en un bucle , usaremos lista para el ingreso de datos

total_de_notas = int(input("Dame la cantidad de notas que vas a poner :"))
notas = []
calificacion = 0
contador = 0
for x in range(total_de_notas):
    #Pedimos los datos
    print("Deme la nota #",x+1," del alumno")
    calificacion = int(input("Nota :"))
    #Lo guardamos
    notas.append(calificacion) 
    contador += calificacion


print("Notas : ",notas)
print("Promedio : ",round(contador/len(notas),2))



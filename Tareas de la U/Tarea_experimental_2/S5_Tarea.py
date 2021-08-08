'''
.:Integrantes:.

Flores Pérez Abraham Elías
Fajardo Cruz Alex Geancarlo
García Campodónico Raúl Alberto
Rivera Ruiz Joan Presley
Andrade Vera Melanie Gisella
'''

#En la descripcion de la tarea dice que hay que mostrar los nombres en la salida del programa
print("\n.:Integrantes:.\nFlores Pérez Abraham Elías\nFajardo Cruz Alex Geancarlo\nGarcía Campodónico Raúl Alberto\nRivera Ruiz Joan Presley\nAndrade Vera Melanie Gisella")

print("\nEjercicio 1\n")

numero = int(input("Dame un numero :"))
print(numero>100)


print("\nEjercicio 2\n")

x=  float(input("Dame el valor de x :"))
y = 3*x**3- 2*x**2 + 3*x- 1
print(y)

print("\nEjercicio 3\n")

numero_1 =  float(input("Dame un numero a: "))
numero_2 =  float(input("Dame un numero b: "))

print(".:1:.  ",numero_1,"+",numero_2,"=",numero_1+numero_2)

print(".:2:.  ",numero_1,"-",numero_2,"=",numero_1-numero_2)

print(".:3:.  ",numero_1,"x",numero_2,"=",numero_1*numero_2)

if numero_2!=0 :
    print(".:4:.  ",numero_1,"/",numero_2,"=",numero_1/numero_2)
else:
    print("No existe la division entre 0")




print("\nEjercicio 4\n")

x = 0
while(x==0):
    x = float(input("Dame el valor de x :"))
    if x == 0:
        print("No existe la division entre  0 ingrese un valor valido")

total_f = 1/(x+1/(x+1/(x+1/x)))
print(total_f)


print("\nEjercicio 5\n")

hora = int(input("Hora de inicio (horas): "))
minuto = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

#Logica todo lo transformo a segundos y lo sumo

hh=hora*3600
mm=minuto*60
dd = duracion * 60
total = hh+mm+dd

#Luego si es mayor a un dia le resto un dia para que vuelva a las  0:00 horas
while(total>86400):
    total =  total-86400


#Luego lo vuelvo a transformar a horas y minutos
hor=(int(total/3600))
minu=int((total-(hor*3600))/60)


print(hor,":",minu)


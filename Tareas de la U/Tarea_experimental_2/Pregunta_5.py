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


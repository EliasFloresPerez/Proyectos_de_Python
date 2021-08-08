
#Pidiendo datos

litros = float(input("¿Cúantos litros de leche desea va a convertir a galones? :"))#Pido los litros con float.
galones = 0 #inicializo la variable galones en  0 para luego poder usarla.

#Conversion de litros a galones

galones = round(litros/3.785,3) #Divido los litros por el equivalente en galones para sacar los galones equivalentes.
#Uso la funcion round para redondear y que solo me de 3 decimales. 
#Impresion de datos
print("Lo equivalente a ",litros,"L a galones es :", galones,"gal.") #imprimo los datos en pantalla.



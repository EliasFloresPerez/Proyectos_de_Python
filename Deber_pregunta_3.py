#Codigo

#La logica es facil dada el numero ingresado solo debemos restar en un bucle 1-n asi hasta que el numero ingresado sea
# menor o igual a 0.

def piramide(bloques):
    total = bloques
    contador = 0
    while(total>0):
        total = total -contador
        if total - contador > 0:
            contador +=1
        
    print("La altura es de :", bloques , "bloques es de :", contador)

piramide(int(input("Dame el total de bloques :")))
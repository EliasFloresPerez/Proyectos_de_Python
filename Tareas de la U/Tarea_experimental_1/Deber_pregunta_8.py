def promedio(alumnos):
    print(".:Promedios:.")
    contador_calificaciones = 0
    for x in alumnos.keys():
        contador_calificaciones = 0
        for valores in range(len(alumnos[x])):
            contador_calificaciones+=alumnos[x][valores]
        alumnos[x]=contador_calificaciones/len(alumnos[x])
        print(x," : ",alumnos[x])
        


def alumnos_f():
    alumnos = {}
    palabra = ""
    nota = -1
    nota_aux = []
    while(palabra != "exit"):
        palabra =""
        nota = -1
        nota_aux = []
        palabra=input("Ingresa el nombre del estudiante (o exit para detenerse):")
        if palabra == "exit":
            break

        while(nota<0 or nota>10):
            nota = int(input("Ingresa la calificación del alumno (0-10):"))
            if nota<0 or nota>10:
                print("La nota no esta en el intervalo deseado")

        if not(palabra in alumnos):
            alumnos[palabra]=[nota]
        else:
            
            nota_aux = alumnos[palabra]
            nota_aux.append(nota)
            alumnos[palabra]=nota_aux
            
    promedio(alumnos)
    
    

alumnos_f()
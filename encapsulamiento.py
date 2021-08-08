class estudiantes:
    def __init__(self,nombre,edad,nota):
        self.nombre = nombre
        self.edad = edad
        self.__nota = nota
    def __repr__(self): #modifico la funcion print
        return "Notas  de {0} son :{1}".format(self.nombre,self.__nota)

estudiante = estudiantes("Elias",20,[10,10,10])
print(estudiante)
print(estudiante._estudiantes__nota) #Especificando la clase si se puede llegar
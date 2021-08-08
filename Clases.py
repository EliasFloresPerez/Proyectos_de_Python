class estudiante:
    nombre = "Pa" # las modifica
    edad = 19
    def __init__(self,nombre,edad,curso,notas):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.notas = notas
    def promedio(self):
        return sum(self.notas)/len(self.notas)
    
note = [10,10,10,10,9]
elias = estudiante("Elias",20,"Tics",note)

print("Promedio :",elias.promedio())
print(elias.nombre, elias.edad)
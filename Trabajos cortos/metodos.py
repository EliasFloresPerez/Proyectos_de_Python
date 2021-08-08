class estudiantes:
    def __init__(self,nombre,edad,carrera,curso):
        self.nombre  = nombre
        self.edad = edad
        self.carrera = carrera
        self.curso = curso
    def info(self):
        print("Estudiante {} con {} años , Carrera : {} , '{}'".format(self.nombre ,self.edad ,self.carrera ,self.curso))
    @classmethod
    def Ambiental(cls, nombre, edad):
        return cls(nombre, edad, "Ambiental", "A")
    @classmethod
    def Industrial(cls, nombre, edad):
        return cls(nombre, edad, "Industrial","B")



a = estudiantes("Elias",20,"Tics","A")
b = estudiantes.Industrial("Joseph",20)
c =  estudiantes.Ambiental("Alex",19)
a.info()
b.info()
c.info()
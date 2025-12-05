
class Profesor():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

class Alumno():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

alumno1 = Alumno("Rodrigo","Menendez Molina","aja@gmail.com")
print(alumno1)

profesor1 = Profesor("Pedro","Calatrava","ojo@gmail.com")
print(profesor1)
#Superclase
class Persona():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
    def dameDatos(self):
        return self.nombre+self.apellidos



# Ademas de indicar de que calse heredamos
class Profesor(Persona):
    def __init__(self,nombre,apellidos,email):
        # En python hay que indicar que nos traemos, si no ponemos nada dentro del super lo trae todo 
        super().__init__(nombre,apellidos,email)

class Alumno(Persona):
    def __init__(self,nombre,apellidos,email):
        super().__init__(nombre,apellidos,email)



# Subclases
class AlumnoOnline(Alumno):
    def __init__(self,nombre,apellidos,email):
        super().__init__(nombre,apellidos,email)

class AlumnoPresencial(Alumno):
    def __init__(self,nombre,apellidos,email):
        super().__init__(nombre,apellidos,email)



alumno1 = Alumno("Rodrigo","Menendez Molina","aja@gmail.com")
print(alumno1.dameDatos)

profesor1 = Profesor("Pedro","Calatrava","ojo@gmail.com")
print(profesor1.dameDatos)
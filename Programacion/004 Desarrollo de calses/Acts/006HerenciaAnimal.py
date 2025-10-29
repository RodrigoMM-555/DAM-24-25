
'''
Rodrigo Menéndez Molina
004/006 Utilización de clases heredadas
Herencia de animal sobre la clase perro y gato
'''

#Creamos la clase madre y las que heredan
class Animal():
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.raza = ""

class Gato(Animal):
    def __init__(self):
        super().__init__()

class Perro(Animal):
    def __init__(self):
        super().__init__()

#Definimos objetos y propiedades
gato1 = Gato()
gato1.edad = 10

perro1 = Perro()
perro1.edad = 7

#Mostramos por pantalla
print(gato1.edad)
print(perro1.edad)
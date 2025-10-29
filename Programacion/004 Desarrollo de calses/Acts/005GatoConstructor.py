
'''
Rodrigo Menéndez Molina
004/005 Creación de constructores
Gatos, metodos y propiedades
'''

#Creamos la calse, sus metodos y propiedades
class Gato():
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.raza = ""

    def maulla(self):
        return("Gato maullando")

#Inicializamos los objetos en la clase
gato1 = Gato()
gato2 = Gato()
gato3 = Gato()

#Definimos las propiedades de cada gato
gato1.edad = 5
gato1.nombre = "Misifu" 
gato1.raza = "Siames"

gato2.edad = 3
gato2.nombre = "Galahad" 
gato2.raza = "Tortuga"

gato3.edad = 7
gato3.nombre = "Ron" 
gato3.raza = "Persa"

#Mostramos valores y hacemos que maullen
print(gato1.nombre,gato1.edad,gato1.raza)
print(gato1.maulla())
print(gato2.nombre,gato2.edad,gato2.raza)
print(gato2.maulla())
print(gato3.nombre,gato3.edad,gato3.raza)
print(gato3.maulla())

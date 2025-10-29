
#Creamos la clase
class Gato():
    def __init__(self):
        self.color = ""
        self.edad = 0

#Combertimos a jagger en un gato y le asignamos unas caracteristicas
jagger = Gato()
jagger.color = "crema"
jagger.edad = 9

#hacemos lo mismo con lana
lana = Gato()
lana.color = "gris"
lana.edad = 11

#Mostramos sus propiedades por pantalla
print(jagger.color, jagger.edad)
print(lana.color, lana.edad)
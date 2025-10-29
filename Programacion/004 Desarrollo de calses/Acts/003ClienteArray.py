
#Definimos la clase
class Cliente():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = []

#Metemos a cliente1 en la clase
cliente1 = Cliente()

#Definimos sus propiedades
cliente1.nombre = "Paco"
cliente1.edad = 29
cliente1.telefonos = 123456789,987654321

#Y las mostramos por pantalla
print(cliente1.nombre)
print(cliente1.edad)
print(cliente1.telefonos)


'''
Rodrigo Menéndez Molina
004/004 Creación de métodos
Seters y geters en la clase cliente
'''

class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""

    #Definimos los setters 
    def setNom(self,nombrecompleto):
        self.__nombrecompleto = nombrecompleto
    def setEmail(self,email):
        self.__email = email

    #Definimos los getters
    def getNom(self):
        return self.__nombrecompleto
    def getEmail(self):
        return self.__email

#Creamos la lista
lista_clientes = []

#Metetmos al cliente 1 y 2 en la clase
cliente1 = Cliente()
cliente1.setNom("Paco")
cliente1.setEmail("aja@gmail.com")

cliente2 = Cliente()
cliente2.setNom("Juanjo")
cliente2.setEmail("ojo@gmail.com")

#Y los añadimos a las listas
lista_clientes.append(cliente1)
lista_clientes.append(cliente2)

print(lista_clientes[0].getNom(), lista_clientes[0].getEmail())
print(lista_clientes[1].getNom(), lista_clientes[1].getEmail())

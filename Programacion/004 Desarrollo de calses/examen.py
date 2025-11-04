
'''
Actividad de final de unidad - Desarrollo de clases
1.-Crea una clase Cliente
2.-Añadele propiedades (nombre, apellidos, email, etc)
3.-Crea al menos un metodo set y un metodo get para una de las propiedades
4.-Crea un constructor con parametros (nombre, apellidos etc en la instanciación del objeto)
5.-Una vez creada la clase, crea tres instancias de la clase, cada una de ellas con sus propias propiedades
6.-Demuestra que los métodos set y get funcionan para cada una de las instancias
'''

'''
Rodrigo Menéndez Molina
examen clases cliente v0.1
Creador y modificador de clientes
'''

#Creamos la calase cliente
class Cliente():
    def __init__(self,nombre,apellidos,email):
        #Propiedades
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
    
    #Setters
    def setNombre(self,nuevoNombre):
        self.nombre = nuevoNombre

    #Getters
    def getNombre(self):
        return self.nombre

    #Creamos un metodo para mostrar mas facilmente los clientes
    def mostrarCliente(self):
        print(self.getNombre())
        print(self.apellidos)
        print(self.email)

#Declaramos los clientes
cliente1 = Cliente("Augusto","comino","aja@gmail.com")
cliente2 = Cliente("Sandra","Puente Rodríguez","ojo@gmail.com")
cliente3 = Cliente("Pepe","Bas Santos","eje@gmail.com")

#Mostramos los clientes iniciales
print("----------------------")
cliente1.mostrarCliente()
print("----------------------")
cliente2.mostrarCliente()
print("----------------------")
cliente3.mostrarCliente()
print("----------------------")
print("")

#Seteamos los clientes
cliente1.setNombre("Tú",)
cliente2.setNombre("Yo")
cliente3.setNombre("Él")


#Mostramos los clientes cambiados
print("----------------------")
cliente1.mostrarCliente()
print("----------------------")
cliente2.mostrarCliente()
print("----------------------")
cliente3.mostrarCliente()
print("----------------------")

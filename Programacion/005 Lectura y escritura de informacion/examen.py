'''
-Crea una mini-aplicacion CRUD
-Crea una mini-clase de Cliente, solo con propiedades, sin métodos
-Crea una lista vacia de clientes
-Ofrece un menu, en el que el usuario podrá, crear clientes, o listar los clientes existentes (dentro de un bucle infinito while, atrapa los dos casos con if-elif)
-Utiliza la librería pickle para guardar la lista de clientes cada vez que se crea uno
-Utiliza la libreria pickle para abrir los clientes, si existen, al abrir la aplicación (es recomendable introducir ese intento de lectura en un try-except)
'''

'''
Rodrigo Menéndez Molina
examen archivos v0.1
mini-CRUD
'''

#Importamos la libreria pickle
import pickle

#Creamos la clase cliente
class Cliente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

#Creamos la lista vacia clientes
clientes = []

#Cargamos la lista de clientes y abrimos el archivo binario y sacamos la lista, sino existe avisara
try:
    archivo = open("clientesEX.bin","rb")
    clientes = pickle.load(archivo)
    archivo.close()
except:
    print("No se ha encontrado el archivo clientesEX.bin, no se podra listar los clientes")

#Empezamos el bucle de la aplicacion
while True:
    #Menu
    print("-------- Menu --------")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar un cliente")
    print("4. Eliminar un cliente")
    opcion = int(input("Que quieres hacer: "))

    #Opcion uno crear cliente
    if opcion == 1:
        print("----------------------------")
        nombre = input("Nombre del cliente: ")
        apellidos = input("Apellidos del cliente: ")
        email = input("Email del cliente: ")

        #Creamos un cliente y le definimos sus caracteristicas
        cliente1 = Cliente(nombre,apellidos,email)
        #Metemos al cliente en la lista
        clientes.append(cliente1)

        #Metemos la lista en un archivo binario, sobreescribiendo todo lo que habia antes
        archivo = open("clientesEX.bin","wb")
        pickle.dump(clientes,archivo)
        archivo.close()

    #Opcion dos listar los clientes
    elif opcion == 2:
        print("----------------------------")
        #Metemos un aviso si no existe el archivo necesario y no mostraremos la lista por si no esta actualizada
        try:
            archivo = open("clientesEX.bin","rb")
            archivo.close()
        except:
            print("No se ha encontrado el archivo clientesEX.bin")
            continue

        #Mostramos cada elemento de la lista con un print distinto
        for cliente in clientes:
            print(cliente.nombre, cliente.apellidos, cliente.email)

#El programa guardara todas las modificaciones de la lista echas mientras se esta ejecutando, de esta foma incluso si 
#se borra el archivo mientras se esta ejecutando bastara con crear otro cliente o archivo con el mismo nombre para poder 
#reescribirlo.


#Extras
    
    #Opcion tres modificar un cliente
    elif opcion == 3:
        print("----------------------------")
        #Pedimos que cliente se quire modificar
        identificaor = int(input("Dame la posicon del cliente que quieres modificar: "))
        cliente = clientes[identificaor-1]

        #Modificamos los valores        
        cliente.nombre = input("Nuevo nombre del cliente: ")
        cliente.apellidos = input("Nuevos apellidos del cliente: ")
        cliente.email = input("Nuevo email del cliente: ")

        #Sobreescribimos el archivo, esto se podria hacer una vz cada vez que se inicia el menu de nuevo
        archivo = open("clientesEX.bin","wb")
        pickle.dump(clientes,archivo)
        archivo.close()


    #Opcion cuatro eliminar uncliente
    elif opcion == 4:
        print("----------------------------")
        #Pedimos que cliente se quire eliminar
        identificaor = int(input("Dame la posicon del cliente a eliminar: "))
        
        #Eliminamos el cliente indicado
        clientes.pop(identificaor-1)

        #Sobreescribimos el archivo, esto se podria hacer una vz cada vez que se inicia el menu de nuevo
        archivo = open("clientesEX.bin","wb")
        pickle.dump(clientes,archivo)
        archivo.close()



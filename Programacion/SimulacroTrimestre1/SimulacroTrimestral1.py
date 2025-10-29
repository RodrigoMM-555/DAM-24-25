
import pickle

class Cliente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

print("------------------------------------")
print("##### Gestion de clientes v0.1 #####")
print("##### Rodrigo Menendez Molina  #####")

clientes = []

try:
    archivo = open("clientes.bin","rb")
    clientes = pickle.load(archivo)
    archivo.close()
except:
    print("No existen datos anteriores")

while True:
    print("------------------------------------")
    print("1. Insertar un cliente")
    print("2. Listar clientes")
    print("3. Actualizar uncliente")
    print("4. Eliminar un cliente")
    opcion = int(input("Escoge una opcion: "))
    print("------------------------------------")

    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")

        clientes.append(Cliente(nombre,apellidos,email))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("ID =",identificador+1)
            print(cliente.nombre, cliente.apellidos, cliente.email)
            identificador += 1

    elif opcion == 3:
        identificador = int(input("Introduce el id para modificar: "))
        nombre = input("Introduce el nuevo nombre: ")
        apellidos = input("Introduce los nuevos apellidos: ")
        email = input("Introduce el nuevo email: ")

        clientes[identificador-1].nombre = nombre
        clientes[identificador-1].apellidos = apellidos
        clientes[identificador-1].email = email
        #Al añadir los clientes se les pone en orden por lo que con el identificador 
        #podemos coger un numero concreto de la lista

    elif opcion == 4:
        identificador = int(input("Introduce el id para eliminar: "))
        confirmacion = input("Estas seguro (s/n): ").lower()

        if confirmacion == "s":
            clientes.pop(identificador-1)

        elif confirmacion == "n":
            print("Cancelado")

        else:
            print("Opcion no valida")
    
    else:
        break
    
    archivo = open("clientes.bin","wb")
    pickle.dump(clientes,archivo)           #Este ,archivo es para indicar donde dumpear la informacion
    archivo.close()

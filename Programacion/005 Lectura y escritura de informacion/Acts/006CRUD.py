'''
005/006 Entrada desde teclado. Salida a pantalla. Formatos de visualización
Rodrigo Menedez Molina
Gestion de clientes con  opciones adicionales
'''

#Definimos la clase
class Cliente():
    def __init__(self,nombre,apellidos,email):
        self.email = email
        self.nombre = nombre
        self.apellidos = apellidos

#Mensaje de inicio
print("------------------------------------")
print("##### Gestión de clientes v0.2 #####")
print("##### Rodrigo Menéndez Molina  #####")

#Declaramos la lista de clientes
clientes = []

#Menu
while True:
    print("------------------------------------")
    print("1. Insertar un cliente")
    print("2. Listar clientes")
    print("3. Actualizar un cliente")
    print("4. Eliminar un cliente")
    opcion = int(input("Escoge una opción: "))
    print("------------------------------------")

    #Opcion 1 añadir un cliente
    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")

        #Los convertimos en mayusculas
        apellidos = apellidos.upper()
        nombre = nombre.upper()

        clientes.append(Cliente(nombre,apellidos,email))
    
    #Opcion 2 Mostrar lista de clientes
    elif opcion == 2:
        identificador = 1
        for cliente in clientes:

            print(identificador,".", cliente.nombre, cliente.apellidos, cliente.email)
            identificador += 1
    
    #Opcion 3 modificar un cliente
    elif opcion == 3:
        identificador = int(input("Introduce el identificador a modificar: "))
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")

        #Los convertimos en mayusculas
        apellidos = apellidos.upper()
        nombre = nombre.upper()

        clientes[identificador-1].nombre = nombre
        clientes[identificador-1].apellidos = apellidos
        clientes[identificador-1].email = email

    #Opcion 4 eliminar un cliente
    elif opcion == 4:
        identificador = int(input("Introduce el identificador a borrar: "))
        seguro = input("Estás seguro (s/n): ").lower()
        if seguro == "n":
            print("Operacion cancelada")
        elif seguro == "s":
            clientes.pop(identificador-1)
        else:
            print("Selección invalida, operación cancelada")

    else:
        break

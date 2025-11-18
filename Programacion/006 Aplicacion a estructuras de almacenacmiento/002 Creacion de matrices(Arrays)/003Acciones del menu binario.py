#Importamos librerias
import pickle

#Creamos menu vacío
menu = []

print("Gestor de menus v0.1")
#Empezamos programa
while True:
    #Menu de opciones
    print("-------------------")
    print("1. Agregar comida al menu")
    print("2. Listar comidas del menu")
    print("3. Guardar en archivo")
    print("4. Cargar menu")
    opcion = int(input("Selecciona una opcion: "))
    print("-------------------")

    #Añadir comida
    if opcion == 1:
        comida = input("Introduce el nombre de la comida: ")
        menu.append(comida)

    #Listar comidas
    elif opcion == 2:
        if menu == []:
            print("El menu esta vacio")
        else:
            print("Las comidas del menu son: ")
            for elemento in menu:
                print(elemento)

    #Guardar en archivo
    elif opcion == 3:
        archivo = open("menu.bin", "wb")
        pickle.dump(menu, archivo)
        archivo.close()
        print("Menu guardado")

    #Cragamos el menu, esto estaria mejor al inicio del programa pero lo ponemos como funcion opcional
    elif opcion == 4:
        archivo = open("menu.bin", "rb")
        menu = pickle.load(archivo)
        close = archivo.close
        print("Menu cargado")
#Creamos lista
menu = []

#Empezamos programa
while True:
    #Menu de opciones
    print("-------------------")
    print("Opciones:")
    print("1. Agregar comida al menu")
    print("2. Listar comidas del menu")
    print("3. Guardar en archivo")
    print("4. ")
    opcion = int(input("Selecciona una opcion: "))
    print("-------------------")

    #Añadir comida
    if opcion == 1:
        comida = input("Introduce el nombre de la comida: ")
        menu.append(comida)
        print("Tu comida hasta el momento es: ")

    #Listar comidas
    elif opcion == 2:
        print("Las comidas en el menu son: ")
        for elemento in menu:
            print(elemento)

    #Guardar en archivo
    elif opcion == 3:
        
        #No podemos guardar listas en un txt, solo deja strings
        archivo = open("menu.txt", "w")
        archivo.write(menu)
        archivo.close()
        print("Menu guardado en menu.txt")


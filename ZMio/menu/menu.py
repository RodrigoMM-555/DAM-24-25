
import json, sys, random

menu = {}
comida = {}
cena = {}

with open("menu.json", "r") as archivo:
    menu = json.load(archivo)

# Numero de platos por tipo de comida
num_carne = len(menu["carne"])
num_pescado = len(menu["pescado"])
num_pasta = len(menu["pasta"])
num_legumbre = len(menu["legumbre"])

#Menu de navegacion
def menuNavegacion():
    option = 0
    print("Menú de navegación:")
    print("1. Ver menú")
    print("2. Añadir plato")
    print("3. Editar plato")
    print("4. Eliminar plato")
    print("5. Generar menú")
    print("6. Guardar y salir")

    option = int(input("Seleccione una opción: "))
    print("-" * 30)
    return option

# 1 Añadir un plato
def añadirPlato(tipo, nombre, momento):
    if tipo not in menu:
        print("Tipo de comida no válido. Por favor, ingrese carne, pescado, pasta o legumbre.")
    elif momento not in [1, 2, 3]:
        print("Momento del día no válido. Por favor, ingrese 1 para desayuno, 2 para comida o 3 para cena.")
    for plato in menu[tipo]:
        if plato["nombre"].lower() == nombre.lower():
            print("El plato ya existe en el menú.")
    else:
        menu[tipo].append({"nombre": nombre, "momento": momento})

# 2 Editar un plato
def editarPlato(tipo, nombre, nuevo_nombre, nuevo_momento):
    if tipo.lower() not in menu:
        print("Tipo de comida no válido. Por favor, ingrese carne, pescado, pasta o legumbre.")
    elif nuevo_momento not in [1, 2, 3]:
        print("Momento del día no válido. Por favor, ingrese 1 para desayuno, 2 para comida o 3 para cena.")
    for plato in menu[tipo]:
        if plato["nombre"].lower() == nombre.lower():
            plato["nombre"] = nuevo_nombre
            plato["momento"] = nuevo_momento
            break
    else:
        print("El plato no existe en el menú.")



# 6 Guardar y salir
def salir():
    with open("menu.json", "w") as archivo:
        json.dump(menu, archivo, indent=2)

    sys.exit(0)


while True:
    print("-" * 30)
    option = menuNavegacion()

    # Opcion 1: Ver menú
    if option == 1:
        print("Menú actual:")
        print(json.dumps(menu, indent=2))

    # Opcion 2: Añadir plato
    elif option == 2:
        tipo = input("Ingrese el tipo de comida (carne, pescado, pasta, legumbre): ")
        nombre = input("Ingrese el nombre del plato: ")
        momento = int(input("Ingrese el momento del día (1: comida, 2: cena, 3: ambos): "))
        añadirPlato(tipo, nombre, momento)

    # Opcion 3: Editar plato
    elif option == 3:
        tipo = input("Ingrese el tipo de comida del plato a editar (carne, pescado, pasta, legumbre): ")
        nombre = input("Ingrese el nombre del plato a editar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del plato: ")
        try:
            nuevo_momento = int(input("Ingrese el nuevo momento del día (1: comida, 2: cena, 3: ambos): "))
        except ValueError:
            print("Momento del día no válido. Por favor, ingrese un número.")
            continue
        editarPlato(tipo, nombre, nuevo_nombre, nuevo_momento)

    # Opcion 4: Eliminar plato
    elif option == 4:
        tipo = input("Ingrese el tipo de comida del plato a eliminar (carne, pescado, pasta, legumbre): ")
        nombre = input("Ingrese el nombre del plato a eliminar: ")
        if tipo.lower() not in menu:
            print("Tipo de comida no válido. Por favor, ingrese carne, pescado, pasta o legumbre.")
        else:
            for plato in menu[tipo]:
                if plato["nombre"].lower() == nombre.lower():
                    menu[tipo].remove(plato)
                    print(f"Plato '{nombre}' eliminado del menú.")
                    break
            else:
                print("El plato no existe en el menú.")

    # Opcion 5: Generar menu
    elif option == 5:
        # Crear la lista con las cantidades
        comidas = (
            ["carne"] * 4 +
            ["pescado"] * 4 +
            ["legumbre"] * 3 +
            ["pasta"] * 3
        )
        # Mezclar aleatoriamente
        random.shuffle(comidas)

        i = 0
        while i < 14:
            tipo = comidas[i]
            if menu[tipo]:  # Verificar que hay platos disponibles para ese tipo
                plato = random.choice(menu[tipo])
                if i <= 6 and plato["momento"] in [1, 3]:  # Si el plato es para comida o ambos
                    comida[f"{tipo}_{i+1}"] = plato["nombre"]
                    i += 1
                if i > 6 and plato["momento"] in [2, 3]:  # Si el plato es para cena o ambos
                    cena[f"{tipo}_{i+1}"] = plato["nombre"]
                    i += 1
            else:
                print(f"No hay platos disponibles para el tipo '{tipo}' en el menú.")
                comida[f"{tipo}_{i+1}"] = "No disponible"
                cena[f"{tipo}_{i+1}"] = "No disponible"
        print("Menú generado para la semana:")
        print("Comida:")
        for key, value in comida.items():
            print(f"{key}: {value}")
        print("\nCena:")
        for key, value in cena.items():
            print(f"{key}: {value}")


    # Opcion 6: Guardar y salir
    elif option == 6:
        salir()
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
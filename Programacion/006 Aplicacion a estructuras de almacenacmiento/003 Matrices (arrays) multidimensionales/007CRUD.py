import pickle

try:
    archivo = open("CRUD.bin", "rb")
    ropa = pickle.load(archivo)
    archivo.close()
except:
    ropa = []

while True:
    print("----------------------------------")
    print("1. Añadir ropa")
    print("2. Ver ropa")
    print("3. Modificar ropa")
    print("4. Eliminar ropa")
    print("5. Salir")
    try:
        opcion = int(input("Elige una opción: "))
    except:
        opcion = 0
    print("----------------------------------")

    if opcion == 1:
        prenda = input("Prenda: ")
        talla = input("Talla: ")
        color = input("Color: ")
        ropa.append([prenda, talla, color])
        archvio = open("CRUD.bin", "wb")
        pickle.dump(ropa, archvio)
        archvio.close()
        print("Prenda añadida")

    elif opcion == 2:
        if len(ropa) == 0:
            print("No hay ropa en la lista.")
        else:
            n = 1
            for prenda in ropa:
                print(n, prenda)
                n += 1
    
    elif opcion == 3:
        if len(ropa) == 0:
            print("No hay ropa en la lista.")
        else:
            identificador = int(input("Dime el número de la prenda a modificar: "))
            prenda = input("Prenda: ")
            talla = input("Talla: ")
            color = input("Color: ")
            ropa[identificador - 1] = [prenda, talla, color]
            archvio = open("CRUD.bin", "wb")
            pickle.dump(ropa, archvio)
            archvio.close()
            print("Prenda modificada")

    elif opcion == 4:
        if len(ropa) == 0:
            print("No hay ropa en la lista.")
        else:
            identificador = int(input("Dime el número de la prenda a eliminar: "))
            ropa.pop(identificador - 1)
            archvio = open("CRUD.bin", "wb")
            pickle.dump(ropa, archvio)
            archvio.close()
            print("Prenda eliminada")

    elif opcion == 5:
        break
    
    else:
        print("Opción no válida")


print("Cubos de acero v0.1")
import json

try:
    archivo = open("007Cubos.json" ,"r")
    contenido = json.load(archivo)
    lista_cubos = contenido
    archivo.close()
except:
    lista_cubos = []

while True:
    print("------------------------------")
    print("Seleccione una opcion")
    print("1.Añadir un cubo")
    print("2.Ver lista de cubos")
    opcion = int(input("Opcion: "))
    print("------------------------------")

    if opcion == 1:
        print("Añadir cubo")
        largo = input("Largo: ")
        ancho = input("Ancho: ")
        profundidad = input("Profundidad: ")
        lista_cubos.append(
            {
                "largo": largo,
                "ancho": ancho,
                "profundidad": profundidad
            }
        )
        archivo = open("007Cubos.json" ,"w")
        json.dump(lista_cubos, archivo)
        archivo.close()

    elif opcion == 2:
        print("Lista de cubos")
        n = 0
        for elemento in lista_cubos:
            n += 1
            print("Cubo",n)
            print("Largo:", elemento["largo"], "- Ancho:", elemento["ancho"], "- Profundidad:", elemento["profundidad"])

    elif opcion == 3:
        print("Modificar cubo")
        iden = int(input("Que cubo quieres modificar(1,2,3,4...): "))
        largo = input("Largo: ")
        ancho = input("Ancho: ")
        profundidad = input("Profundidad: ")

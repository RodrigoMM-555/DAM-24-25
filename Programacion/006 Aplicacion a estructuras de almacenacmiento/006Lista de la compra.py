
print("Lista de la compra v0.1")
import json

lista_de_la_compra = []

while True:
    print("------------------------------")
    print("Seleccione una opcion")
    print("1.Añadir producto")
    print("2.Ver lista de la compra")
    opcion = int(input("Opcion: "))
    print("------------------------------")

    if opcion == 1:
        print("Añadir producto")
        producto = input("Producto: ")
        cantidad = input("Cantidad: ")
        lista_de_la_compra.append(
            {
                "producto": producto,
                "cantidad": cantidad
            }
        )
        archivo = open("006lista.json" ,"w")
        json.dump(lista_de_la_compra, archivo)
        archivo.close()


    elif opcion == 2:
        print("Lista de la compra:")
        for elemento in lista_de_la_compra:
            print("Producto:", elemento["producto"], "- Cantidad:", elemento["cantidad"])

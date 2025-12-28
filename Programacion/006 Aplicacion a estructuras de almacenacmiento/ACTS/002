import pickle

#Inicializamos la lista de comidas
menu_comidas = []

try:
    #Intentamos cargar la lista desde el archivo binario
    with open("menu_comidas.bin", "rb") as archivo:
        menu_comidas = pickle.load(archivo)
    print("Menú de comidas cargado desde 'menu_comidas.bin'.")
except:
    print("No se encontró el archivo 'menu_comidas.bin'. Se creará uno nuevo.")


#Bucle para introducir nuevas comidas
while True:
    comida = input("Introduce el nombre de una comida (o escribe 'salir' para terminar): ")
    if comida.lower() == "salir":
        break
    menu_comidas.append(comida)
    print("\nMenú actual:")
    for c in menu_comidas:
        print("-", c)

#Guardar la lista en un archivo binario
with open("menu_comidas.bin", "wb") as archivo:
    pickle.dump(menu_comidas, archivo)

print("\nEl menú se ha guardado correctamente en 'menu_comidas.bin'.")
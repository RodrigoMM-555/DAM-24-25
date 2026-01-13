import pickle

#Lista para almacenar contactos
contactos = []

#Bucle para introducir nuevos contactos
while True:
    nombre = input("Introduce el nombre del contacto (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    telefono = input("Introduce el teléfono: ")
    contactos.append([nombre, apellidos, email, telefono])
    print("\nAgenda actualizada:")
    for c in contactos:
        print("-", c)

#Guardar la lista en un archivo binario
with open("agenda.bin", "wb") as archivo:
    pickle.dump(contactos, archivo)

#Función para cargar la agenda desde el archivo
def cargar_agenda():
    try:
        with open("agenda.bin", "rb") as archivo:
            return pickle.load(archivo)
    except:
        print("El archivo de agenda no existe.")
        return []

#Mostrar contactos cargados
agenda = cargar_agenda()
print("\nContactos guardados:")
for contacto in agenda:
    print(contacto)
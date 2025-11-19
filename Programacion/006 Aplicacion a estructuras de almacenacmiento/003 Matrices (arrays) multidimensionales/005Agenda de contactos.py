
import pickle

agenda = []

while True:
    print("----------------------------------")
    nombre = input("Dime tu nombre: ")
    apellidos = input("Dime tu apellidos: ")
    email = input("Dime tu email: ")
    telefono = input("Dime tu teléfono: ")
    agenda.append([nombre, apellidos, email, telefono])
    archvio = open("agenda.bin", "wb")
    pickle.dump(agenda, archvio)
    archvio.close()

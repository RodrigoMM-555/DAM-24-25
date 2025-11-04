'''
Rodrigo Menéndez Molina
005/001 Flujos. Tipos, bytes y caracteres. Clases relacionadas
Agenda electrónica
'''

print("Dime lo que quieres hacer")
while True:
    print("1.-Introduce un nuevo contacto")
    print("2.-Leer todos los contactos")
    try:
        opcion = int(input("Qué opción quieres: "))
    except:
        print("Opción invalida")
        continue

    if opcion == 1:
        nombre = input("Introduce tu nombre: ")
        email = input("Introduce tu email: ")

        agenda = open("agenda.txt","a")
        agenda.write(f"{nombre}, {email}\n")

        agenda.close
    
    elif opcion == 2:
        agenda = open("agenda.txt","r")
        lineas = agenda.readlines()
        for linea in lineas:
            print(linea)
        
        agenda.close
    
    else:
        break


'''
Rodrigo Menedez Molina
005/005Creación y eliminación de ficheros y directorios
Crear y destruir archivo
'''

import os

opcion = int(input("Opcion: "))

if opcion == 1:
    archivo = open("progreso_juego.txt","w")
    archivo.write("Rodrigo_MM")
    archivo.close()

elif opcion == 2:
    os.remove("progreso_juego.txt")
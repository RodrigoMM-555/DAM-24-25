
import os

#Ejercicio 1. Suma del tamaño de los archivos
carpeta = input("Indica una carpeta: ")

suma = 0

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            suma += os.path.getsize(ruta)
        except:
            pass  # Evita errores si un archivo no se puede leer
  
print("La carpeta ocupa:")
print(suma/(1024*1024),"MB")


#Ejercicio 2. Muestra de los archivos de mas de un 1GB
carpeta = input("Indica una carpeta: ")

grande = 1024*1024*1024                 #1 giga

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            if os.path.getsize(ruta) > grande:
                print(ruta, os.path.getsize(ruta)/(1024/1024),"MB")
        except:
            pass                       


#Ejercicio 3. Mostrar todos los archivos en una carpeta
carpeta = input("Indica una carpeta: ")
grande = 1024*1024*1024                 #1 giga

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        print(ruta+"\n")


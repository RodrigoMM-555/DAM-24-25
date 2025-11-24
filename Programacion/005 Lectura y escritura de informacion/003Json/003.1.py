
#Esto importa desde el archivo de texto blog

archivo = open("003.1blog.txt","r")

lineas = archivo.readlines()

for linea in lineas:
    print(linea)
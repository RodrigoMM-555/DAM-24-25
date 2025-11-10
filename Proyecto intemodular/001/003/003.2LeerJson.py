
import  json        #Esto importa desde el archivo json dentro de la carpeta del proyecto

archivo = open("003.2.json","r")

contenido = json.load(archivo)

for linea in contenido:
    print("-------------------ARTICULO---------------------")
    print(linea["titulo"])
    print(linea["fecha"])
    print(linea["autor"])
    print(linea["contenido"])
    print("------------------------------------------------")
    print("")
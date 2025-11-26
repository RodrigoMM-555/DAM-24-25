#argparse es para datos con conmbre, sys es para datos sencillos
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--nombre")
parser.add_argument("--apellidos")

#Los convierte en argumentos
args = parser.parse_args()

print(args)
#Namespace(nombre=None, apellidos=None)

#Lo convertimos en un diccionario
diccionario = vars(args)
print(diccionario)
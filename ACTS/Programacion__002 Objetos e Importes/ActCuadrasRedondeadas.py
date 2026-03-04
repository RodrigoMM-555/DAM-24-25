
'''
Rodrigo Menendez Molina
002/007 Destrucción de objetos y liberación de memoria
Calculadora de cuadras
'''

#0
import math

#1
num_caballos = int(input("Numero de caballos: "))

#2
cuadras = num_caballos/3
cuadras_redondeadas = math.ceil(cuadras)

#3
print("Necesitas",cuadras_redondeadas,"cuadras")

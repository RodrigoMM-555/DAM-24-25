
'''
Rodrigo Menéndez Molina
003/001 Estructuras de repeticion
Categoria según edad
'''

edad=15
# Comienza tu codigo aquí

categoria=""

#De pendiendo el rango de edad la categoria sera una u otra
if edad<10:
    categoria="Niño"
elif edad>=10 and edad<20:
    categoria="Adolescente"
else:
    categoria="Adulto"

#Mostraremos la categoria a la que pertenece el ususario
print("Estas en la categoria",categoria)

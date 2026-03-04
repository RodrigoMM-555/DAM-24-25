
'''
Rodrigo Menéndez Molina
003/005 Aserciones
Edad y nivel suficiente
'''

#1. Declaracion de vaiables y asignacion de valores
edad = 47
nivel_jugador = 5

#2 Aseert
try:
    assert edad == 48, "Error determinado"
    assert nivel_jugador > 3, "Nivel insuficioente"
except:
    print("Error")


'''
Rodrigo Menéndez Molina
Examen U3 v0.1
Número aleatorio
'''

#Inicializacion
print("------------------------------------")
print("#####    Numero random v0.1    #####")
print("##### Rodrigo Menendez Molina  #####")

#Importamos librerías
import random

#Declaramos los intentos
intentos = 6

#Generamos el número random
numero_random = random.randint(0, 50)
#Muestro el número para hacer pruebas de funcionamiento
print(numero_random)

print("Averigua el número entero entre 0 y 50")

#Iniciamos el bucle
while True:
    print("---------------------------------------")

    #Avisamos de los intentos y damos una pista en el tercer intento
    print("Te quedan", intentos,"intentos")
    if intentos ==3:
        if numero_random % 2 == 0:
            print("El número secreto es PAR.")
        else:
            print("El número secreto es IMPAR.")
    
    #Pedimos el número
    numero = input("Que número crees que es: ")

    #Probamos a convertirlo a entero
    try:
        numero = int(numero)
    except:
        print("Número no válido")
        continue

    #Probamos si el numero esta dentro del rango
    try:
        assert numero < 51 and numero > -1
    except:
        print("Número fuera de rango")
        continue
    
    #Pedimos confimracion
    confirmacion = input("Estás seguro s/n: ")
    
    #Informamos si acierta o si falla y si falla le decimos si el número es más alto o más bajo
    if confirmacion == "s":
        if numero == numero_random:
            print("Felicidades has acertado, el número era",numero_random)
            break
        elif numero < numero_random:
            print("Demasiado bajo")
            intentos -= 1
        elif numero > numero_random:
            print("Demasiado alto")
            intentos -= 1
    elif confirmacion == "n":
        print("Número cancelado")

    #Vemos cuantos intentos quedan y si los intentos son negativos
    try:
        assert intentos < 0, ("Intentos negativos")
    except:
        if intentos == 0:
            print("Te has quedado sin intentos, el número era",numero_random)
            break
        else:
            continue

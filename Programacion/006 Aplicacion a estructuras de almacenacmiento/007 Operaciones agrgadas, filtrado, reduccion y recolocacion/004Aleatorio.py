
import random
import os

os.system("clear")

patron = {1,2,3,4,5,6,7,8,9}
n = 0

while True:
    lista = []

    #Generamos los valores de la lista
    for i in range(1,10):
        lista.append(random.randint(1,9))

    #Convertimos la lista en un conunto, se pierden los duplicados
    conjunto = set(lista)

    #Ponemos condicion
    if conjunto == patron:
        print("El conjunto es correcto, Numero de intentos:",n)
        #Mostramos la lista y el patron
        print(patron)
        print(conjunto)
        break
    else:
        n += 1



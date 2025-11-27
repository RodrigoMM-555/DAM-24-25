import random

patron = {1,2,3,4,5,6,7,8,9}

#Cuando no se usa un avariable como "celda" se recomienda usar un _
for celda in range(1,10):
    while True:
        lista = []

        for i in range(1,10):
            lista.append(random.randint(1,9))

        conjunto = set(lista)

        if conjunto == patron:
            print("El conjunto es correcto")
            print(conjunto)
            print(lista)
            break

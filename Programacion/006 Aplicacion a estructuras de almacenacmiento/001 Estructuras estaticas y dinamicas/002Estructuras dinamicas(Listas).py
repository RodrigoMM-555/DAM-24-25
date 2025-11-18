#Creamos la lista
agenda = []

#Metemos dos nombres
agenda.append("Jose Vicente")
agenda.append("Juan")

#Mostramos la lista
print(agenda)

#Metemos otro nombre
agenda.append("Jorge")

#Mostramos la lista y el primer elemento
print(agenda)
print(agenda[0])

#Modificamos el primer elemento y mostramos la lista
agenda[0] = "Jaime"
print(agenda)

#Comportamiento de pila, con append añadimos un plato y con pop lo quitamos, pero siempre lo añadimos y quitamos de arriba
#Esto solo con el comportamiento estandar de pop
agenda.pop()
print(agenda)

#LIFO - Last In First Out

#Elimina el elemento que le digamos
agenda.pop(1)
print(agenda)

#Lista
lista = ["manzana", "banana", "cereza"]
print(lista)
print(type(lista))

#Tupla
tupla = ("zanahoria", "col", "cebolla")
print(tupla)
print(type(tupla))

#Creamos una lista con los datos de la tupla, no se elimina la tupla original
lista = list(tupla)
print(tupla)
print(lista)

#Creamos una tupla con los datos de la lista, no se elimina la lista original
tupla_nueva = tuple(lista)
print(lista)
print(tupla_nueva)
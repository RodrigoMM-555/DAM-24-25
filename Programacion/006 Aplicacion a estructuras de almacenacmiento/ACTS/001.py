'''
Una lista es una estructura dinámica que permite almacenar varios elementos y acceder a ellos mediante un índice.
Los diccionarios permiten organizar información usando claves y valores, lo que resulta muy útil para representar objetos de un videojuego, como su nombre y sus coordenadas.

Por ejemplo, para acceder a un objeto dentro de la lista se utiliza su índice, como ocurre al acceder al primer elemento de la lista objetos_juego[0]. Una vez obtenido el objeto, se puede acceder a sus datos mediante las claves del diccionario, como el nombre o las coordenadas. También es posible modificar la información almacenada, cambiando las coordenadas de un objeto concreto, o eliminar elementos de la lista cuando ya no son necesarios. Finalmente, utilizando un bucle for, se pueden recorrer todos los objetos del juego y mostrar su información por pantalla.

El ejercicio propuesto quedaria asi:
'''
#Crear una lista de objetos del juego
objetos_juego = [
    {"nombre": "Jugador", "coordenadas": (10, 20, 5)},
    {"nombre": "Enemigo", "coordenadas": (30, 15, 0)},
    {"nombre": "Tesoro", "coordenadas": (5, 25, 10)}
]

#Acceder al primer objeto e imprimir su información
print("Primer objeto:")
print("Nombre:", objetos_juego[0]["nombre"])
print("Coordenadas:", objetos_juego[0]["coordenadas"])

#Modificar las coordenadas del segundo objeto
objetos_juego[1]["coordenadas"] = (40, 10, 2)

#Eliminar el tercer objeto de la lista
del objetos_juego[2]

#Recorrer la lista y mostrar todos los objetos
print("\nObjetos restantes en el juego:")
for objeto in objetos_juego:
    print("Nombre:", objeto["nombre"])
    print("Coordenadas:", objeto["coordenadas"])

'''    
En conclusión, en esta actividad se ha trabajado con listas y diccionarios para gestionar objetos dentro de un juego.
Estos conceptos son fundamentales en programación, ya que permiten organizar y manejar información de forma clara en aplicaciones y videojuegos reales.
'''
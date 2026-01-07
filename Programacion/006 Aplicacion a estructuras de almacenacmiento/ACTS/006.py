#Diccionario para representar un personaje con habilidades
personaje = {
    "nombre": "Aventurero",
    "edad": 25,
    "habilidades": {
        "fuerza": 7,
        "destreza": 5,
        "magia": 3
    }
}

#Solicitar al usuario una nueva habilidad y su nivel
nueva_habilidad = input("Introduce el nombre de la nueva habilidad: ")
nivel_habilidad = int(input("Introduce el nivel de la habilidad: "))

#Añadir la nueva habilidad al diccionario de habilidades
personaje["habilidades"][nueva_habilidad] = nivel_habilidad

#Mostrar la información completa del personaje
print("\nInformación completa del personaje:")
print("Nombre:", personaje["nombre"])
print("Edad:", personaje["edad"])
print("Habilidades:")
for habilidad, nivel in personaje["habilidades"].items():
    print("-", habilidad + ":", nivel)
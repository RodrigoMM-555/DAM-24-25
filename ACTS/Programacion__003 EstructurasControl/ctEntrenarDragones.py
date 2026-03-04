
'''
Rodrigo Menendez Molina
003/007
Entrenamiento de dragones
'''

#1
nomDragonA = input("Nombre del dragon A: ")
edadDragonA=  int(input("Edad del dragon A: "))

nomDragonB = input("Nombre del dragon B: ")
edadDragonB =  int(input("Edad del dragon B: "))

#2
def clasificacion(edadDragon):
    if edadDragon <= 50:
        return "Joven"
    if edadDragon > 50 and edadDragon <= 199:
        return "Adulto"
    if edadDragon >= 200:
        return "Anciano"
        
clasificacionA = clasificacion(edadDragonA)
clasificacionB = clasificacion(edadDragonB)

#3
def entrenamiento(clasificacion):
    fuerza = 0
    resistencia = 0
    print(clasificacion)
    for dia in range(1,4):
        if clasificacion == "Joven":
            fuerza += 3
            resistencia += 2
        elif clasificacion == "Adulto":
            fuerza += 2
            resistencia += 2
        elif clasificacion == "Anciano":
            fuerza += 1
            resistencia += 1

    return(fuerza,resistencia)

fuerzaA,resistenciaA = entrenamiento(clasificacionA)
fuerzaB,resistenciaB = entrenamiento(clasificacionB)

#4
print("Nombre:",nomDragonA)
print("Edad:",edadDragonA)
print("Clasificacion:",clasificacionA)
print("Fuerza:",fuerzaA)
print("Resistencia:",resistenciaA)

print("Nombre:",nomDragonB)
print("Edad:",edadDragonB)
print("Clasificacion:",clasificacionB)
print("Fuerza:",fuerzaB)
print("Resistencia:",resistenciaB)











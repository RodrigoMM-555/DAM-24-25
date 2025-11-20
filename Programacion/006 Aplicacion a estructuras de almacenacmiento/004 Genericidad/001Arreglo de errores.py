#Primer caso
numeros = [
    1,
    2,
    "3",
    4,
]

print(numeros)

def calculadorDoble():
    for numero in numeros:
        print(numero * 2)

calculadorDoble()

print("--------------------")

#Segundo caso
def calculadorDoble():
    for numero in numeros:
        numero = int(numero)
        print(numero * 2)

calculadorDoble()

print("--------------------")
#Tercer caso

numeros = [1,2,"3",4,"cinco"]

print(numeros)

def calculadorDoble():
    for numero in numeros:
        try:
            numero = int(numero)
            print(numero * 2)
        except:
            print("Nop")

calculadorDoble()

print("--------------------")

#Cuarto caso
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]

def calculadorDoble():
    for numero in numeros:
        try:
            numero = int(numero)
            print(numero * 2)
        except:
            for i in range(0,len(numeros_etiquetas)):
                if numero == numeros_etiquetas[i]:
                    print(i * 2)

calculadorDoble()

print("--------------------")

#Quinto caso
numeros = [1,2,"3",4,"cinco","patata"]

print(numeros)

def calculadorDoble():
    for numero in numeros:
        try:
            numero = int(numero)
            print(numero * 2)
        except:
            centinela = False
            for i in range(0,len(numeros_etiquetas)):
                if numero == numeros_etiquetas[i]:
                    print(i * 2)
                    centinela = True
            if centinela == False:
                print("Nop")

calculadorDoble()

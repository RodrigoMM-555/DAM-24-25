
'''
Rodrigo Menéndez Molina
003/004 ontrol de excepciones
TryDivision
'''

#Definir la variable
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("No puedo dividir entre cero")
        return None

#Probar la función
print(dividir(10, 2))  # Debería imprimir 5.0
print(dividir(10, 0))  # Debería imprimir "No puedo dividir entre cero" y None

#Los argumentos son forma de meter informacion sin usar imput, asi otros codigos pueden usar el programa
import sys
print(sys.argv)
#['006ArgumentoArchivo.py', 1, 2, 3]
#Argumentos es como una lista en el que el elemento 0 es el nombre de archivo y el 1,2,3 son argumentos que pueden pasar


#Doble edad
argumentos = sys.argv
edad = argumentos[1]

entero = int(edad)
doble = entero*2
print(doble)


#python3 006ArgumentoArchivo.py 12
#['006ArgumentoArchivo.py', '12']
#24
import random

#Generar un Sudoku 9x9 lleno con números del 1 al 9 en cada fila aleatoriamente
def generar_sudoku():
    sudoku = []
    numeros = list(range(1, 10))
    for i in range(9):
        fila = numeros[:]
        random.shuffle(fila)
        sudoku.append(fila)
    return sudoku

#Función para eliminar un número específico del tablero
def eliminar_numero(sudoku, numero, cantidad):
    eliminados = 0
    while eliminados < cantidad:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        if sudoku[fila][columna] == numero:
            sudoku[fila][columna] = "_"
            eliminados += 1
    return sudoku

#Generar el tablero original
tablero = generar_sudoku()

print("Sudoku original:")
for fila in tablero:
    print(fila)

#Eliminar 5 números al azar del tablero
for _ in range(5):
    num_aleatorio = random.randint(1, 9)
    tablero = eliminar_numero(tablero, num_aleatorio, 1)

print("\nSudoku modificado:")
for fila in tablero:
    print(fila)
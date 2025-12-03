
#Importamos libreria
import sqlite3

#Nos conectamos a la base de datos
conexion = sqlite3.connect("empresa.db")

#Creamos un cursor
cursor = conexion.cursor()

#Ejecutamos una sentencia
cursor.execute('''
    INSERT INTO clientes VALUES(
        NULL, 'Jorge','Menendez Molina','xd@gmail.com'
    );
''')

#Lanzamos la peticion
conexion.commit()

cursor.execute ('''
    SELECT * FROM CLIENTES;
''')

filas = cursor.fetchall()

for fila in filas:
    print(fila)

import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "Uclientes",
    password = "Contra1$",
    database = "clientes"
)

cursor = conexion.cursor()
cursor.execute('''
    SELECT COUNT(color), color
    FROM productos
    GROUP BY color
    ORDER BY COUNT(color) ASC;
''')

filas = cursor.fetchall()
print(filas)

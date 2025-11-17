
import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "Uclientes",
    password = "Contra1$",
    database = "clientes"
)

cursor = conexion.cursor(dictionary=True)
cursor.execute('''
   SELECT
    nombre AS "Nombre del cliente",
    apellidos AS "Apellidos del cliente",
    edad AS "Edad del cliente"
    FROM
    clientes
    ORDER BY
    edad DESC;        
''')

filas = cursor.fetchall()

print(filas)
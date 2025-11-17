import mysql.connector
import json

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
    FROM clientes
    ORDER BY edad DESC;        
''')

filas = cursor.fetchall()

#Lo combierte en la estructura de un archivo json
resultado_json = json.dumps(filas,ensure_ascii=False, indent=2)
print(resultado_json)
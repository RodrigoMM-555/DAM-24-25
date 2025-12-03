
import mysql.connector
#import matplotlib      /Esto lo he usado porque no funcionaba antes
#matplotlib.use('TkAgg')  # Use TkAgg for local environments
import matplotlib.pyplot as pt


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

cantidades = []
etiquetas = []
for fila in filas:
    cantidades.append(fila[0])
    etiquetas.append(fila[1])
print(cantidades)
print(etiquetas)

pt.pie(cantidades, labels=etiquetas)
pt.show()


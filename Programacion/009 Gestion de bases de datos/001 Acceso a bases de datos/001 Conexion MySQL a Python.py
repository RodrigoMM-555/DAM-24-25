#pip3 install --user mysql-connector-python

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="empresa2026",
    password="Empresa2026$",
    database="empresa2026"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")

for fila in cursor.fetchall():
    print(fila)

cursor.close()
conn.close()

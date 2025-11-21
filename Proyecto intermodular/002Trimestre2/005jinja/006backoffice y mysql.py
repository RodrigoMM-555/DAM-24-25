
#Libreria flask para crear webs
from flask import Flask, render_template
import mysql.connector

#Traemos mysql
conexion = mysql.connector.connect(
    host="localhost",
    user="Trimestral1",
    password="Trimestral123$",
    database="portafolioexamen"
)

cursor = conexion.cursor()
cursor.execute("SHOW TABLES;")
tablas = []
filas = cursor.fetchall()
for fila in filas:
    tablas.append(fila[0])


#Cerramos la app
app = Flask(__name__)

#Ruta de inicio
@app.route('/')
def incio():
    return render_template('backoffice.html',mis_tablas = tablas)

#Ejecutamos la app
if __name__ == '__main__':
    app.run(debug=True)

#Libreria flask para crear webs
from flask import Flask, render_template
import mysql.connector

#############################################################
#Traemos mysql
conexion = mysql.connector.connect(
    host="localhost",
    user="Trimestral1",
    password="Trimestral123$",
    database="portafolioexamen"
)

#------------Esto muestra nuestras tablas-------------------
cursor = conexion.cursor()
cursor.execute("SHOW TABLES;")
tablas = []
filas = cursor.fetchall()
for fila in filas:
    tablas.append(fila[0])

#--------------Estoy trae los titulos de la tabla------------------
cursor.execute("SHOW COLUMNS in piezasportafolio;")
columnas = []
filas = cursor.fetchall()
for fila in filas:
    columnas.append(fila[0])

#----------------------Esto envia toda la tabla----------------------
cursor.execute("SELECT * FROM piezasportafolio;")
contenido_tabla = cursor.fetchall()
#############################################################

#Cerramos la app
app = Flask(__name__)

#Ruta de inicio
@app.route('/')
def inicio():
    return render_template(
        'backoffice.html',
        mis_tablas = tablas,
        mis_columnas = columnas,
        mi_contenido_tabla = contenido_tabla
        )

#Ejecutamos la app
if __name__ == '__main__':
    app.run(debug=True)
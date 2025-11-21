
#Libreria flask para crear webs
from flask import Flask, render_template
import mysql.connector

#Traemos mysql
conexion = mysql.connector.connect(
    host = "localhost", user = "", pasword = "", database = ""
)

cursor = conexion.cursor()
cursor.execute("SHOW TABLES;")
tablas = []


#Cerramos la app
app = Flask(__name__)

#Ruta de inicio
@app.route('/')
def incio():
    return render_template('backoffice.html')

#Ejecutamos la app
if __name__ == '__main__':
    app.run(debug=True)
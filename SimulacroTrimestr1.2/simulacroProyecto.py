
import mysql.connector
from flask import Flask


#Conexion de suusario para mysql
conexion = mysql.connector.connect(
    host="localhost",
    user="Usimulacro",
    password="Simulacro123$",
    database="simulacro"
)

############################################################################

#Cramos el cursor y ejecutamos al consulta, mostramos la vision de piezas y categorias
cursor = conexion.cursor()

cursor.execute('''SELECT *FROM vista_piezas;''')

#Obtenemos las filas
filas = cursor.fetchall()

#Mostramos las filas
for fila in filas:
    titulo,descripcionP,imagen,categoria,descripcionC = fila
    print(fila)
    print(titulo,descripcionP,imagen,categoria,descripcionC)

###############################################################################

app = Flask(__name__)


@app.route("/")
def raiz():
    return "cadena"

if __name__ == "__main__":
    app.run(debug=True)



'''
titulo
descripcion pieza
imagen
categoria
descripcion categoria
'''
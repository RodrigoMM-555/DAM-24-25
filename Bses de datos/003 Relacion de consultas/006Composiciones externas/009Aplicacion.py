from flask import Flask, render_template
import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="composiciones",
  password="Composiciones123$",
  database="composiciones"
)                                      

app = Flask(__name__)
@app.route("/")
def inico():
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM matriculas_join;")  

    filas = cursor.fetchall()
    return str(filas)


if __name__ == "__main__":
  app.run(debug=True)
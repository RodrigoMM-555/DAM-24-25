
from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/envio")
def envio():
    nombre = request.args.get("nombre")
    apellidos = request.args.get("apellidos")
    print(nombre,apellidos)
    return "Nombre: "+nombre+"- Apellidos: "+apellidos

if __name__ == "__main__":
    app.run(debug=True)

#Si pones esto te saldra Rodirgo en la consola
#http://127.0.0.1:5000/?nombre=Rodrigo
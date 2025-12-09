
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def inicio():
    nombre = request.args.get("nombre")
    print(nombre)
    return("Mira en la consola de visual estudio, o la del sistema operativo")

if __name__ == "__main__":
    app.run(debug=True)

#Si pones esto te saldra Rodirgo en la consola
#http://127.0.0.1:5000/?nombre=Rodrigo
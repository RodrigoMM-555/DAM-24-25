
#Libreria flask para crear webs
from flask import Flask, render_template

#Cerramos la app
app = Flask(__name__)

#Ruta de inicio
@app.route('/')
def incio():
    mis_frutas = ["Manzana", "Pera", "Naranja", "Plátano", "Cereza"]
    return render_template('lista.html', frutas = mis_frutas)

#Ejecutamos la app
if __name__ == '__main__':
    app.run(debug=True)
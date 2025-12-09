
#Libreria flask para crear webs
from flask import Flask, render_template

#Cerramos la app
app = Flask(__name__)

#Ruta de inicio
@app.route('/')
def incio():
    return render_template('inicio.html')

#Ruta de sobre mi
@app.route('/sobremi')
def sobremi():
    return render_template('sobremi.html')

#Ruta de contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

#Ejecutamos la app
if __name__ == '__main__':
    app.run(debug=True)
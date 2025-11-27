#Libreria flask para crear webs
from flask import Flask, render_template

#Cerramos la app
app = Flask(__name__)

#Ruta principal
@app.route('/')
def incio():
    return render_template('index4.html')

#Ejecutamos la app
if __name__ == '__main__':
    app.run(debug=True)
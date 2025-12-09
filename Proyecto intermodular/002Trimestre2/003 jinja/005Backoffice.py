
#Libreria flask para crear webs
from flask import Flask, render_template

#Cerramos la app
app = Flask(__name__)

#Ruta de inicio
@app.route('/')
def incio():
    return render_template('backoffice.html')

#Ejecutamos la app
if __name__ == '__main__':
    app.run(debug=True)
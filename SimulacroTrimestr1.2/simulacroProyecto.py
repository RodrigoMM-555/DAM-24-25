import mysql.connector
from flask import Flask, render_template_string


#Conexion de suusario para mysql
conexion = mysql.connector.connect(
    host="localhost",
    user="Usimulacro",
    password="Simulacro123$",
    database="simulacro"
)

########################################################################################

cursor = conexion.cursor()

cursor.execute('''SELECT *FROM vista_piezas;''')

#Obtenemos las filas
filas = cursor.fetchall()

#Mostramos las filas
for fila in filas:
    titulo,descripcionP,imagen,categoria,descripcionC = fila

#########################################################################################

#Creamos una palicacion flask (osea web)
app = Flask(__name__)

#Atrapo la ruta raiz
@app.route("/")

def raiz():
    print("Funciona")
    cadena =  '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <title>Simulacro2</title>
        <meta charset="UTF-8">

        <style>
                body{                                   
                    background:rgb(220, 238, 236);     
                    font-family:monospace;              
                }
                header,main,footer{
                    width:600px;         
                    background:ghostwhite;
                    margin:auto;                
                    padding:20px;
                    text-align: center;     /*Para que el textoe ste centrado*/
                }
                header{
                    background: rgb(226, 226, 233);
                }
                footer{
                    background: rgb(226, 226, 233);
                }
                main{
                    display: grid;
                    grid-template-columns: auto auto auto; /*El numero de auto son el numero de columnas*/
                    gap: 20px;
                }
                main img{
                    width: 100%;
                    height: auto;
                    margin: 0px;
                }


        </style>
    </head>


    <body>
        <header>
            <h1>Rodrigo Menendez Molina</h1>
            <h2>menendez.rodrigo555@gmail.com</h2>
        </header>
        <main>
    '''
    for fila in filas:
        titulo,descripcionP,imagen,categoria,descripcionC = fila
        cadena +=   ("<article>"
                        "<h3>"+str(titulo)+"</h3>"
                        "<img src="+str(imagen)+" alt='En proceso'></img>"
                        "<p>"+str(categoria)+"</p>"
                        "<p>"+str(descripcionP)+"</p>"
                    "</article>")
    cadena +='''
        </main>
        <footer>
            <p>© 2025 Rodrigo Menendez Molina. Todos los derechos reservados.</p>
        </footer>
    </body>


    </html>
    '''
    return cadena

if __name__ == "__main__":
    app.run(debug=True)
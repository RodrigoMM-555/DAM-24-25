
import mysql.connector
from flask import Flask, render_template_string


#Conexion de ususario para mysql
conexion = mysql.connector.connect(
    host="localhost",
    user="Trimestral1",
    password="Trimestral123$",
    database="portafolioexamen"
)

#Creacion y conjexion del cursor
cursor = conexion.cursor()

#Ejecutamos una peticion a la base de datos
cursor.execute('''SELECT *FROM vista_piezas;''')

#Obtenemos las filas de la tabla vista_piezas de la base de datos
filas = cursor.fetchall()

#Creamos una palicacion flask (osea web)
app = Flask(__name__)

#Atrapo la ruta raiz
@app.route("/")

#Creamos la funcion
def raiz():
    #Mensaje de comprovacion
    print("Funciona")
    #Cadena del archivo HTML
    cadena =  '''
    <!--Declaramos el html-->
    <!DOCTYPE html>
    <!--Elegimos el lenguaje-->
    <html lang="es">

    <!--Empezamos el head-->
    <head>
        <!--Imagen de la pestaña de arriba-->
        <link rel="icon" href="engranajes.jpg" type="image/jpeg">
        <!--Ponemos un título-->
        <title>ExamenTri1</title>
        <!--Seleccionamos una codificación-->
        <meta charset="UTF-8">

        <!--Creamos un estilo-->
        <style>
            /*Elegimos fondo y fuente de todo el cuerpo*/
            body{                                   
                background:rgb(220, 238, 236);     
                font-family:monospace;              
            }
            /*Definimos tamaño, margen y otras cosas de los elementos del main*/
            header,main,footer{
                width:600px;         
                margin:auto;                
                padding:20px;
                /*Para que el textoe ste centrado*/
                text-align: center;     
            }
            /*Le damos otro color al header y footer*/
            header,footer{
                background: rgb(226, 226, 233);
            }
            /*Le damos otro color al main así como una forma de red*/
            main{
                background:ghostwhite;
                /*Con esto creamos un grid para los artículos del main*/
                display: grid;
                /*El número de auto son el número de columnas*/
                grid-template-columns: auto auto auto; 
                gap: 20px;
            }
            /*Configuracion para el tamaño de las imagenes en main*/
            main img{
                width: 100%;
                height: auto;
                margin: 0px;
            }
            /*Modificamos un poco los margenes para que quede mejor*/
            main p, main h3{
                margin: 5px;
            }
        </style>
    </head>

    <!--Empezamos el body-->
    <body>
        <!--El cabezal de la web-->
        <header>
            <h1>Rodrigo Menéndez Molina</h1>
            <h2>menendez.rodrigo555@gmail.com</h2>
        </header>
        <main>
    '''
    #Generamos todos los articulos, esta es la seccion que se repetira
    #Habran tantos articulos como hayan en la abse de datos
    #Por cada fila en la tabla las variables cogeran los valores correspondientes
    for fila in filas:
        titulo,descripcion,fecha,categoria,imagen = fila
        #Se suma a la cadena de HTML
        cadena +=   ("<article>"
                        "<h3>"+str(titulo)+"</h3>"
                        "<img src="+str(imagen)+" alt='En proceso'></img>"
                        "<p><u>"+str(categoria)+"</u></p>"
                        "<p>"+str(descripcion)+"</p>"
                        "<p>"+str(fecha)+"</p>"
                    "</article>")
    #Cerramos la generacion de articulos y sumamos lo que queda del HTML
    cadena +='''
        </main>
        <!--Empezamos el pie de página-->
        <footer>
            <!--Copyright-->
            <p>© 2025 Rodrigo Menéndez Molina. Todos los derechos reservados.</p>
        </footer>
    </body>

    </html>
    '''
    #Devolvemos la cadena con todo el HTML
    return cadena

if __name__ == "__main__":
    app.run(debug=True)

    
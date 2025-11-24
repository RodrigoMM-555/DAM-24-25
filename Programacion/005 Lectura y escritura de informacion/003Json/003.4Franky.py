#Este archivo de flask originalmente solo icniaba un servidor. 
#Ahora teambien inicia el servidor con html json y toda la pesca.

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    #Esto es el archivo 003.3.html
    return '''
    <!DOCTYPE html>
<html lang="esp">
    <head>
        <litle>RODRIGOMMblog</litle>
        <meta charset="utf-8">
        <style>
            body{background-color: ghostwhite;color:black;font-family: sans-serif;}
            header,main,footer{background-color: white;padding: 20px;margin: auto;width: 600px;}
            main{color: slateblue;}
        </style>
    </head>

    <body>
        <header><h1>RODRIGOMMblog</h1></header>
        <main>
            <article>
                <h3>Titulo del articulo</h3>
                <time>16/10/2025</time>
                <p>Rodrigo Menendez Molina</p>
                <p>Este es el contenido del articulo ficticio</p>
            </article>
        </main>

        <footer>(c) 2025 Rodrigo Menendez Molina</footer>
    </body>

</html>
'''

if __name__ == "__main__":
    aplicacion.run(debug=True)



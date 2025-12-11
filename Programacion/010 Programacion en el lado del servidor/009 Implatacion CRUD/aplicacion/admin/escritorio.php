<!--http://..../basesdedatosdamdaw2526/008-Proyectos/003-Panel%20de%20control/101-Ejercicios/aplicacion/admin/escritorio.php -->

<!doctype html>
<html lang="es">
	<head>
        <title>El jocarsa - Panel de control</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="css/estilo.css">
        <style>/* ESTILOS GENERALES /////////////  */
            html,body{
                width:100%;
                height:100%;
                margin:0px;
                padding:0px;
            }
            body{
                display:flex;
            }
            nav{
                flex:1;
                background:teal;
            }
            main{
                flex:4;
                background:white;
            }
            /* ESTILOS DEL MENU /////////////  */
            nav{
                display:flex;
                padding:20px;
                flex-direction:column;
                gap:20px;
            }
            nav button{
                background:white;
                border:none;
                color:black;
                padding:10px;
            }
            /* ESTILOS DE LA TABLA /////////////  */
            main{
                padding:20px;
            }
            table{
                width:100%;
                border:1px solid teal;
                border-collapse:collapse;
            }
            table th{
                background:teal;
                color:white;
            }
            table td,table th{
                padding:5px;
            }
        </style>
    </head>
    <body>
        <nav>
            <button>Noticias</button>
            <button>Autores</button>
        </nav>
        <main>
            <?php include "inc/read/leer.php"; ?>
        </main>
    </body>
</html>
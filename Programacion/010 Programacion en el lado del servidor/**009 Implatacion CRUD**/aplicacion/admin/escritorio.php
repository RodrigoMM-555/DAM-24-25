<!--http://..../basesdedatosdamdaw2526/008-Proyectos/003-Panel%20de%20control/101-Ejercicios/aplicacion/admin/escritorio.php -->

<!doctype html>
<html lang="es">
	<head>
        <title>El jocarsa - Panel de control</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="css/estilo.css">
        <style>
            /* ESTILOS GENERALES /////////////  */
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
            #nuevo{
                position:absolute;
                bottom:20px;
                right:20px;
                background:green;
                color:white;
                width:30px;
                height:30px;
                border-radius:40px;
                text-align:center;
                font-size:30px;
                line-height:30px;
                text-decoration:none;
                font-weight:bold;
            }
            .eliminar{
                width:20px;
                height:20px;
                background:red;
                border-radius:30px;
                color:white;
                line-height:20px;
                text-decoration:none;
                display:block;
                text-align:center;
            }
            .editar{
                width:20px;
                height:20px;
                background:gold;
                border-radius:30px;
                color:white;
                line-height:20px;
                text-decoration:none;
                display:block;
                text-align:center;
            }

            /* ESTILOS DEL FORMULARIO /////////////  */
            form{
                display:flex;
                width:100%;
                flex-direction:column;
                gap:20px;
            }
            .controlformulario{
                display:flex;
                width:100%;
                flex-direction:column;
            }
        </style>
    </head>
    <body>
        <nav>
            <button>Noticias</button>
            <button>Autores</button>
        </nav>
        <main>
            <?php
            //Esto es un router en php
                if(isset($_GET['accion'])){							// Si hay "accion" en la URL
                    if($_GET['accion'] == "nuevo"){					// Si la acción es "nuevo"
                    include "inc/create/formulario.php";	        // En ese caso mete el formulario
                    }
                    elseif($_GET["accion"] == "eliminar"){
                    include "inc/delete/eliminar.php";
                    }
                    elseif($_GET["accion"] == "editar"){
                    include "inc/update/actualizarformulario.php";
                    }
                }
                else{													// En caso contrario
                    include "inc/read/leer.php"; 						// Enseñame la tabla
                }
            ?>
            <a href="?accion=nuevo" id="nuevo">+</a>
        </main>
    </body>
</html>

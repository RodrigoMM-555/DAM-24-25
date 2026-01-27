
<?php

session_start(); // Esto para recordar cosas

// Si no existe la variable de sesion idioma
if(!isset($_SESSION['idioma'])){
// En ese caso el idioma por defecto es español
$_SESSION['idioma'] = 'es';
}

// Si la url transporta la variable idioma
if(isset($_GET['idioma'])){
// La sesion es lo que diga la URL
$_SESSION['idioma'] = $_GET['idioma'];
}

$idiomas['es']['inicio'] = 'Inicio';
$idiomas['es']['sobre_mi'] = 'Sobre mi';
$idiomas['es']['proyectos'] = 'Proyectos';
$idiomas['es']['contacto'] = 'Contacto';

$idiomas['en']['inicio'] = 'Home';
$idiomas['en']['sobre_mi'] = 'About me';
$idiomas['en']['proyectos'] = 'Projects';
$idiomas['en']['contacto'] = 'Contact';
?>

<!doctype html>
<html lang="es">
    <head>
        <title>Multi idioma</title>
        <meta charset="utf-8">
        <style>
            body,html{padding:0px;margin:0px;font-family:sans-serif;}
            header{display:flex;background:black;color:white;justify-content:space-between;align-items:center;}
            header a{text-decoration:none;color:inherit;margin:0px 10px;}
            h1{font-size:20px;}
            select{background:none;border:none;}
        </style>
    </head>
    <body>
        <select>
            <option value="es" 
                <?php if($_SESSION['idioma'] == 'es'){echo ' active ';} ?>
            >🇪🇸</option>
            <option value="en"
                <?php if($_SESSION['idioma'] == 'en'){echo ' active ';} ?>
            >🇬🇧</option>
        </select>
        <h1>Rodrigo Menendez Molina</h1>
        <nav>
            <a href=""><?= $idiomas[$_SESSION['idioma']]['inicio'] ?></a>
            <a href=""><?= $idiomas[$_SESSION['idioma']]['sobre_mi'] ?></a>
            <a href=""><?= $idiomas[$_SESSION['idioma']]['proyectos'] ?></a>
            <a href=""><?= $idiomas[$_SESSION['idioma']]['contacto'] ?></a>
        </nav>
    </body>
    <script>
        let selector = document.querySelector('select');    // Selecciono el selector
        selector.onchange = function(){                     // Cuadno cambie el selector
    	    window.location = "?idioma="+this.value	        // Recargo y le paso el idioma en la url        
            }
    </script>
</html>


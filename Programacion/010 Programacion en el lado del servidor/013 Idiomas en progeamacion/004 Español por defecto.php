
<?php
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
    </head>
    <body>
        <select>
        <option value="es">🇪🇸</option>
        <option value="en">🇬🇧</option>
        </select>
        <h1>Rodrigo Menendez Molina</h1>
        <nav>
            <a href=""><?= $idiomas['es']['inicio'] ?></a>
            <a href=""><?= $idiomas['es']['sobre_mi'] ?></a>
            <a href=""><?= $idiomas['es']['proyectos'] ?></a>
            <a href=""><?= $idiomas['es']['contacto'] ?></a>
        </nav>
    </body>
</html>


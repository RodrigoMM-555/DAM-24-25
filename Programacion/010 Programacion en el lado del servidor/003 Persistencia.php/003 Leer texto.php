<?php
    $archivo = fopen("archivo.txt", "r"); // "r" = leer/read
    $contenido = fread($archivo,filesize("archivo.txt"));
    echo $contenido;
    fclose($archivo);
?>
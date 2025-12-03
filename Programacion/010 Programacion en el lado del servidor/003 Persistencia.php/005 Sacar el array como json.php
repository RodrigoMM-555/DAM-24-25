<?php
    $cliente = [];
    $cliente['nombre'] = "Rodigo";
    $cliente['apellidos'] = "Menendez Molina";
    $cliente['email'] = "aja@jocarsa.com";
    
    $json = json_encode($cliente);
    echo $json;
?>
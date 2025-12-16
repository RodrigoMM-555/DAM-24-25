<?php
	
    //Aunque añadamos mas valores a la lista el foreach los recorrera todos
    $cliente = [
        "nombre" => "Rodrigo",
        "apellidos" => "Menendez",
        "email" => "ajajaj@gmail.com"
    ];
    
    //Vomita el array sin estructura
    var_dump( $cliente );
    echo "<br>";

    //Saca la clave y el valor
    foreach($cliente as $clave => $valor){
        echo "$clave: $valor<br>";
    }
?>
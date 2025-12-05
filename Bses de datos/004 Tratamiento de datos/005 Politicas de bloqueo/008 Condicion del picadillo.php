<?php

	// Primera ronda //////////////////////////////////
    $cadena = "Hola";
    echo $cadena;
    echo "<br>";
    
    // Hash mediante md5
    $picadillo1 = md5($cadena);
    echo $picadillo1;
    echo "<br>";
    
    // Segunda ronda //////////////////////////////////
    $cadena2 = "Hola";
    echo $cadena2;
    echo "<br>";
    
    // Hash mediante md5
    $picadillo2 = md5($cadena2);
    echo $picadillo2;
    echo "<br>";

    
// El picadillo es siempre igual, por lo que comparando el picadillo de lo que pones y el picadillo de lo que hay en la BBDD se puede comprovar.

?>


<?php
	session_start();
    
    $_SESSION['nombre'] = "Jose Vicente";
    $_SESSION['apellidos'] = "Carratalá Sanchis";
    
    foreach($_SESSION as $clave=>$valor){
        echo $clave.": ".$valor."<br>";
    }
?>
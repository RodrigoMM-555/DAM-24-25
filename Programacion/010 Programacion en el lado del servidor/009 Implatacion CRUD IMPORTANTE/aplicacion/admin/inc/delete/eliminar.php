<?php

    $id = $_GET["id"];

    $host = "localhost";															            // Me conecto a la base de datos
    $user = "periodico";
    $pass = "Periodico123$";
    $db   = "periodico";

    $conexion = new mysqli($host, $user, $pass, $db);	// Ejecuto la conexion

    $sql = "DELETE FROM noticias WHERE id = ".$id.";";                                          // Lanzo la peticion de delete
    $conexion->query($sql);
        
    $conexion->close();																            // Cierro la conexion
    header("Location: escritorio.php");											// Y me vuelvo al escritorio

?>

Si estas viendo esto es que vamos a eliminar

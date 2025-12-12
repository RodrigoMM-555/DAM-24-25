<?php

	$titulo = $_POST['titulo'];	
    $contenido = $_POST['contenido'];	
    $fecha_publicacion = $_POST['fecha_publicacion'];	
    $autor_id = $_POST['autor_id'];	
    $id = $_POST['id'];	

    $host = "localhost";
    $user = "periodico";
    $pass = "Periodico123$";
    $db   = "periodico";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "
        UPDATE noticias 
        SET
        titulo = '".$titulo."',
        contenido = '".$contenido."',
        fecha_publicacion = '".$fecha_publicacion."',
        autor_id = ".$autor_id.",
        WHERE id = ".$id.";
    ";

    $conexion->query($sql);
        
    $conexion->close(); 
    header(header: "Location: ../../escritorio.php");
    
?>
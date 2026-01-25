<?php
	// Primero cogemos el id que se quiere eliminar
    $id = $_POST['id'];

    // Conectamos
    $host = "localhost";
    $user = "empleados";
    $pass = "Empleados123$";
    $db   = "empleados";

    $conexion = new mysqli($host, $user, $pass, $db);

    // Borramos los datos en la base de datos
    $sql = "
        DELETE FROM empleados
        WHERE id = ".$id."
    ";

    $conexion->query($sql);
        
    $conexion->close();
  
?>
<?php
	// Primero cogemos el id que se quiere eliminar
    $id = $_POST['id'];

    // Conectamos
    $host = "localhost";
    $user = "empleados";
    $pass = "Empleados123$";
    $db   = "empleados";

    $conexion = new mysqli($host, $user, $pass, $db);

    // Mostramos los datos de ese id
    $sql = "
      	SELECT * FROM empleados WHERE id = ".$id.";
    ";
    $resultado = $conexion->query($sql);
    while ($fila = $resultado->fetch_assoc()) {

        // Pintar un formulario en pantalla
        echo '
        <form action="003 Procesar actualizacion.php" method="POST">
            <input type="hidden" name="id" value="'.$id.'">
            <input type="text" name="nombre" placeholder="nombre" value="'.$fila['nombre'].'">
            <input type="text" name="puesto" placeholder="puesto" value="'.$fila['puesto'].'">
            <input type="text" name="salario" placeholder="salario" value="'.$fila['salario'].'">
            <input type="text" name="fecha_contratacion" placeholder="fecha_contratacion" value="'.$fila['fecha_contratacion'].'">
            <input type="text" name="departamento" placeholder="departamento" value="'.$fila['departamento'].'">
            <input type="submit">
        </form>
        ';
    }

    $conexion->query($sql);
        
    $conexion->close();
  
?>

<?php
    $resultado = $conexion->query("
    SHOW TABLES;
    ");
    while ($fila = $resultado->fetch_assoc()) {
            echo '<a href="?tabla='.$fila['Tables_in_'.$db].'">'.$fila['Tables_in_'.$db].'</a>';
    }
?>
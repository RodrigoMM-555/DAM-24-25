<?php
    $sql = "INSERT INTO ".$_GET['tabla']." VALUES (";
    foreach($_POST as $clave=>$valor){
        if($clave == "$id"){
            $sql .= "NULL, ";
        } 
        else {
            $sql .= $clave."='".$valor."', ";
        }
    }
    $sql = substr($sql,0,-1); // Eliminar la última coma para que no haya problemas en MySQL
    $sql .= ");";
    echo $sql;

    $resultado = $conexion->query($sql);						// Proceso el SQL
    header("Location: ?tabla=".$_GET['tabla']);

?>
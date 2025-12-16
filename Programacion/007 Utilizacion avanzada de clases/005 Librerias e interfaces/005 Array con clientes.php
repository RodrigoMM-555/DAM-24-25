<?php
	
    //Aunque añadamos mas valores a la lista el foreach los recorrera todos
    $campos_cliente = [
        "nombre",
        "apellidos",
        "email",
        "telefono",
        "direccion"
    ];
    
    foreach($campos_cliente as $campo){
        echo "<input type='text' placeholder='$campo'><br>";
    }
?>
<input type="submit">
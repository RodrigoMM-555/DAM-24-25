<?php
	
    $cliente = [
        "nombre" => "Rodrigo",
        "apellidos" => "Menendez",
        "email" => "aja@gmail.com"
    ];
    
    foreach($cliente as $clave=>$valor){
        echo "<label>".$clave."</label>";
        echo "<input type='text' value='".$valor."'>";
    }
 
?>
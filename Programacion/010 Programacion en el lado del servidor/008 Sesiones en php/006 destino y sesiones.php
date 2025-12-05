<!--Si reconocera la variable de 006, esto por usar el _SESSION-->
<?php
    session_start();
    echo $_SESSION["nombre"];
?>
<?php
$host = "localhost";
$user = "Ureserva_pistas";
$pass = "Ureserva_pistas2$";
$db   = "reserva_pistas"; // O crea una base de datos test_db para pruebas

$conexion = new mysqli($host, $user, $pass, $db);
if ($conexion->connect_errno) {
    die("Fallo de conexión: " . $conexion->connect_error);
}
?>

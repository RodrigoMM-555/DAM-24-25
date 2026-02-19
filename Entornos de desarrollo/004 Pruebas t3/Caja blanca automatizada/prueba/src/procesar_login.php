<?php

// Opcionalmente puedes seguir usando $_POST si lo llamas desde el formulario,
// pero ahora la función validador recibirá email y password como parámetros.
$email = $_POST['email'] ?? null;
$password = $_POST['password'] ?? null;

function validador($email, $password){
    include __DIR__ . '/inc/conexion_bd.php'; // desde src/

    if (!$conexion) return "error";

    $sql = "SELECT password FROM usuarios WHERE email = ? LIMIT 1";
    $stmt = $conexion->prepare($sql);
    if (!$stmt) return "error";
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $resultado = $stmt->get_result();

    if ($resultado->num_rows === 0) return "invalid_email";

    $stored_password = $resultado->fetch_assoc()['password'];

    if (!password_verify($password, $stored_password)) return "invalid_contra";
    
    // Solo iniciar sesión si no estamos en CLI
    if (php_sapi_name() !== 'cli') {
        session_start();
        $_SESSION["usuario"] = $email;
    }

    return "success";
}

?>

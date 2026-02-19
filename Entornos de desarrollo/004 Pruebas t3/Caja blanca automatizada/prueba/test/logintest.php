
<!-- 
El modulo de login solo comprueba si la contraseña e email estan en la BBDD 
No comprueba el tamaño, formato ni nada parecido pues eso se comprueba ya en el register
vendor/bin/phpunit test/LoginTest.php

-->
<?php
use PHPUnit\Framework\TestCase;
require_once __DIR__ . '/../src/procesar_login.php';
require_once __DIR__ . '/../src/inc/conexion_bd.php';

class LoginTest extends TestCase {
    public function testContraseñaIncorrectaLong() {
        global $conexion;
        $this->assertEquals("invalid_contra", validador("hola@example.com", "wrongpassword"));
    }

    public function testEmailIncorrecto() {
        global $conexion;
        $this->assertEquals("invalid_email", validador("noexiste@example.com", "contrasena1234"));
    }

    public function testContraseñaEmailCorrecta() {
        global $conexion;
        $this->assertEquals("success", validador("hola@example.com", "contrasena1234"));
    }
}
?>

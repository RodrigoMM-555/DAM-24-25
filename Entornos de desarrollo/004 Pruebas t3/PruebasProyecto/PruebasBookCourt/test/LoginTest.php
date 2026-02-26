<?php
use PHPUnit\Framework\TestCase;
require_once __DIR__ . '/../src/LoginService.php';

class LoginTest extends TestCase {

    private $service;

    protected function setUp(): void {
        $this->service = new LoginService();
    }

    public function testEmailNoExiste() {
        $this->assertEquals("email_not_found",
            $this->service->login(null, "1234"));
    }

    public function testPasswordIncorrecta() {
        $this->assertEquals("wrong_password",
            $this->service->login("correcta", "incorrecta"));
    }

    public function testLoginCorrecto() {
        $this->assertEquals("success",
            $this->service->login("1234", "1234"));
    }

    public function testValidarEmailExisteTrue() {
        $this->assertTrue($this->service->validarEmailExiste("dato"));
    }

    public function testValidarEmailExisteFalse() {
        $this->assertFalse($this->service->validarEmailExiste(null));
    }

    public function testValidarPasswordCorrecta() {
        $this->assertTrue($this->service->validarPassword("a","a"));
    }

    public function testValidarPasswordIncorrecta() {
        $this->assertFalse($this->service->validarPassword("a","b"));
    }

    public function testPasswordVacia() {
        $this->assertFalse($this->service->validarPassword("", "1234"));
    }
}
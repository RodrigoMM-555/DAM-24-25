<?php
use PHPUnit\Framework\TestCase;
require_once __DIR__ . '/../src/RegistroService.php';

class RegistroTest extends TestCase {

    private $service;

    protected function setUp(): void {
        $this->service = new RegistroService();
    }

    public function testEmailValido() {
        $this->assertTrue($this->service->validarEmail("test@test.com"));
    }

    public function testEmailInvalido() {
        $this->assertFalse($this->service->validarEmail("no-valido"));
    }

    public function testPasswordMinimaValida() {
        $this->assertTrue($this->service->validarPasswordLongitud("12345678"));
    }

    public function testPasswordDemasiadoCorta() {
        $this->assertFalse($this->service->validarPasswordLongitud("123"));
    }

    public function testPasswordDemasiadoLarga() {
        $this->assertFalse($this->service->validarPasswordLongitud(str_repeat("a",25)));
    }

    public function testPasswordAlfanumericaValida() {
        $this->assertTrue($this->service->validarPasswordAlfanumerica("abc123"));
    }

    public function testPasswordConCaracterEspecial() {
        $this->assertFalse($this->service->validarPasswordAlfanumerica("abc@123"));
    }

    public function testPasswordVacia() {
        $this->assertFalse($this->service->validarPasswordLongitud(""));
    }
}
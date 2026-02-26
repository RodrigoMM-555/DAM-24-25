<?php
use PHPUnit\Framework\TestCase;
require_once __DIR__ . '/../src/BackCrudService.php';

class BackCrudTest extends TestCase {

    private $service;

    protected function setUp(): void {
        $this->service = new BackCrudService();
    }

    public function testTablaExiste() {
        $this->assertTrue(
            $this->service->tablaExiste(["usuarios","reservas"], "usuarios")
        );
    }

    public function testTablaNoExiste() {
        $this->assertFalse(
            $this->service->tablaExiste(["usuarios"], "pistas")
        );
    }

    public function testGenerarInputs() {
        $inputs = $this->service->generarInputs(["nombre","email"]);
        $this->assertCount(2,$inputs);
    }

    public function testGenerarInputsContenido() {
        $inputs = $this->service->generarInputs(["nombre"]);
        $this->assertStringContainsString("nombre",$inputs[0]);
    }

    public function testArrayVacio() {
        $inputs = $this->service->generarInputs([]);
        $this->assertEmpty($inputs);
    }
}
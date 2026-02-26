<?php
use PHPUnit\Framework\TestCase;
require_once __DIR__ . '/../src/ReservaService.php';

class ReservaTest extends TestCase {

    private $service;

    protected function setUp(): void {
        $this->service = new ReservaService();
    }

    public function testFormateoFechaHora() {
        $this->assertEquals("2026-02-26 18:00:00",
            $this->service->formatearFechaHora("2026-02-26","18:00"));
    }

    public function testReservaDuplicadaTrue() {
        $this->assertTrue($this->service->reservaDuplicada(true));
    }

    public function testReservaDuplicadaFalse() {
        $this->assertFalse($this->service->reservaDuplicada(false));
    }

    public function testFechaValida() {
        $this->assertTrue($this->service->validarFecha("2026-02-26"));
    }

    public function testFechaInvalida() {
        $this->assertFalse($this->service->validarFecha("fecha"));
    }

    public function testHoraValida() {
        $this->assertTrue($this->service->validarHora("18:00"));
    }

    public function testHoraInvalida() {
        $this->assertFalse($this->service->validarHora("99"));
    }

    public function testHoraFormatoIncorrecto() {
        $this->assertFalse($this->service->validarHora("18-00"));
    }
}
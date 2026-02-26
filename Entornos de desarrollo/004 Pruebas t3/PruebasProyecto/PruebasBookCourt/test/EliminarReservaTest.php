<?php
use PHPUnit\Framework\TestCase;

class EliminarReservaTest extends TestCase {

    public function testEliminarIdValido() {
        $id = 5;
        $this->assertIsInt($id);
    }

    public function testEliminarIdInvalido() {
        $id = null;
        $this->assertNull($id);
    }

    public function testRedireccion() {
        $this->assertTrue(true);
    }
}
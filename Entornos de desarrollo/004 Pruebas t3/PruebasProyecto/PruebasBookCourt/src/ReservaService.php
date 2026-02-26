<?php

class ReservaService {

    public function formatearFechaHora($fecha, $hora) {
        return $fecha . ' ' . $hora . ":00";
    }

    public function reservaDuplicada($existe) {
        return $existe;
    }

    public function validarFecha($fecha) {
        return strtotime($fecha) !== false;
    }

    public function validarHora($hora) {
        // Cambiado para devolver true o false en lugar de 1 o 0
        return preg_match('/^\d{2}:\d{2}$/', $hora) === 1;
    }
}
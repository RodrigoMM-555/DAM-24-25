<?php

class BackCrudService {

    public function tablaExiste($tablasDisponibles, $tabla) {
        return in_array($tabla, $tablasDisponibles);
    }

    public function generarInputs($columnas) {
        $inputs = [];
        foreach ($columnas as $col) {
            $inputs[] = "<input name='$col'>";
        }
        return $inputs;
    }
}
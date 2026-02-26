<?php

class RegistroService {

    public function validarEmail($email) {
        return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
    }

    public function validarPasswordLongitud($password) {
        return strlen($password) >= 8 && strlen($password) <= 24;
    }

    public function validarPasswordAlfanumerica($password) {
        return preg_match('/^[a-zA-Z0-9]+$/', $password) === 1;
    }
}
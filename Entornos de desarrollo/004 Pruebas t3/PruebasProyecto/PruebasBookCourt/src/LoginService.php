<?php

class LoginService {

    public function validarEmailExiste($resultado) {
        return $resultado !== null;
    }

    public function validarPassword($password, $storedPassword) {
        return $password === $storedPassword;
    }

    public function login($resultadoBD, $passwordIntroducida) {

        if (!$this->validarEmailExiste($resultadoBD)) {
            return "email_not_found";
        }

        if (!$this->validarPassword($passwordIntroducida, $resultadoBD)) {
            return "wrong_password";
        }

        return "success";
    }
}

sudo mysql -u root -p

CREATE DATABASE ejemplclaves;

CREATE TABLE personas(
	nombre VARCHAR(50),
	apellidos VARCHAR(255)
);

--Añado idetificador

ALTER TABLE personas
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

SHOW TABLES;

--Crear tabla emails
CREATE TABLE emails (
  direccion VARCHAR(50),
  persona VARCHAR(255)
);

-- añado identificador

ALTER TABLE emails
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

SHOW TABLES;

--Crear clave ajena
--Paso 1 cambiar tipo de columna
ALTER TABLE emails
MODIFY COLUMN persona INT;

--Paso 2 crear la foreign key
ALTER TABLE emails
ADD CONSTRAINT fk_emails_personas
--Persona es lo que queremos relacionar
FOREIGN KEY (persona) 
--Personas es la otra table e identificador es lo que se relaciona
REFERENCES personas(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

--Explicacion del codigo anterior
ALTER TABLE emails                  -- Altera la tabla de emails
ADD CONSTRAINT fk_emails_personas   -- Crea una restriccion con este nombre
FOREIGN KEY (persona)               -- Creamos una clave hacia persona
REFERENCES personas(identificador)  -- que referencia el identificador
ON DELETE CASCADE                   -- Cuando elimines, cascada
ON UPDATE CASCADE;                  -- Cuando actualices, cascada

--Inserto una persona
INSERT INTO personas VALUES(
	NULL,
	"Rodrigo",
	"Menendez Molina"
);

--Inserto un email el numero dicta a que identificador se une el email
--Gracias a la restriccion no podemos poner un correo a una persona que no existe
--pero si pueden tener el mismo codigo varias personas porque no hemos usado UNIQUE
INSERT INTO emails VALUES(
	NULL,
	"aja@gmail.com",
	1
);
INSERT INTO emails VALUES(
	NULL,
	"jojo@gmail.com",
	1
);
INSERT INTO emails VALUES(
	NULL,
	"perpe@gmail.com",
	1
);

--Peticion cruzada
SELECT * FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;
--Estamos juntando el apartado persona de la tabala emails
--con el apartado identificador del apartado personas







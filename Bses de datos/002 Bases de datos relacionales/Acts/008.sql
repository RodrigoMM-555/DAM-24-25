--Iniciamos mysql
sudo mysql -u root -p

--Vemos las bases de datos
SHOW DATABASES;

--Usamos la abse de datos
USE empresadam

--Creamos las tablas
CREATE TABLE personas(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(50),
	apellidos VARCHAR(50)
);
CREATE TABLE emails(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(50)
);

--Insertamos en personas
INSERT INTO personas VALUES(
	NULL,
	"Rodrigo",
	"Menendez Molina"
);

--Creamos la clave ajena 
ALTER TABLE emails
ADD CONSTRAINT email_a_persona
FOREIGN KEY (identificador)
REFERENCES personas(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

--Insertamos en emails
INSERT INTO emails VALUES(
	1,
	"aja@gmail.com"
);

--Creamos al view
CREATE VIEW personas_correos AS
SELECT 
personas.identificador, personas.nombre, personas.apellidos, emails.email
FROM personas
LEFT JOIN emails
ON personas.identificador = emails.identificador;

--Mostramos la vista
SELECT * FROM personas:correos;
+---------------+---------+-----------------+---------------+
| identificador | nombre  | apellidos       | email         |
+---------------+---------+-----------------+---------------+
|             1 | Rodrigo | Menendez Molina | aja@gmail.com |
+---------------+---------+-----------------+---------------+
1 row in set (0.00 sec)


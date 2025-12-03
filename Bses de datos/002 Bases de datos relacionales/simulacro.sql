--Iniciamos sesion en mysql
sudo mysql -u root -p

--Creamos base de datos
CREATE DATABASE simulacro;

--Comprobamos que se ha creado correctamente
SHOW DATABASES;

--Usamos la base de datos
USE simulacro;

--Creamos una tabla
CREATE TABLE autores(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(100),
	apellidos VARCHAR(100),
	email VARCHAR(100)
);

--Nos aseguramos de que se ha creado y que esta correcto
SHOW TABLES;
DESCRIBE autores;

--En caso de no haber definido bien la tabla, por ejemplo autores sin la primary key
ALTER TABLE autores DROP identificador;
ALTER TABLE autores  ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
--Se puede hacer MODIFY COLUMN en vez de DROP para no borrar sino cambiar la columna 

--Insertamso un autor de prueba
INSERT INTO autores VALUES(
	NULL,
	"Roberto",
	"Comino Santos",
	"ojo@gmail.com"
);

--Comprovamos si se ha intoducido bien
SELECT * FROM autores;

--Creamos la otra tabla
CREATE TABLE entradas(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(100),
	fecha VARCHAR(100),
	imagen VARCHAR(100),
	id_autor INT,
	contenido TEXT
);
--En caso de haber metido mal el id_autor, poniendo VARCHAR en lugar de INT
ALTER TABLE entradas MODIFY COLUMN id_autor INT;

--Cromprobamos que se ha creado
SHOW TABLES;
DESCRIBE entradas;

--Foreign key
--Tabla que queremos modificar
ALTER TABLE entradas
--Nombre de la foreign key
ADD CONSTRAINT autor_a_entrada
--Columna de la tabla que modificamos y a la cual queremos traelre la informacion
FOREIGN KEY (id_autor)
--Tabla de la que quermos traer y (columna) de la que queremos la informacion
REFERENCES autor(identificador)
--En delete o update
ON DELETE CASCADE
ON UPDATE CASCADE;

--Insertamos una entrada
INSERT INTO entradas VALUES(
	NULL,
	"Primera entrada",
	"2025 - 11-  03",
	"imagen.png",
	1,
	"Este es el contenido de la primera entrada"
);

--Comprovamos los datos
SELECT * FROM entradas;

--Peticion cruzada, esto va antes de crear la view
SELECT 
entradas.titulo, entradas.fecha, entradas.imagen, entradas.contenido,
autores.nombre, autores.apellidos
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.identificador;

--Creamos la vista, que es basicamente la peticion pero dentro de un comando mas corto
CREATE VIEW vista_entradas AS
--Seleccionamos que columnas queremos
SELECT 
entradas.titulo, entradas.fecha, entradas.imagen, entradas.contenido,
autores.nombre, autores.apellidos
--Usamos esta tabla. left join es como "y añadimos de esta otra tabla"
FROM entradas
LEFT JOIN autores
--Cambiamos la columna id_autor de entradas por la de identificador de autores
ON entradas.id_autor = autores.identificador;

-- Comprovamos la vista
SELECT * FROM vista_entradas;

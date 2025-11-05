--Iniciamos sesion en mysql
sudo mysql -u root -p

--Creamos base de datos
CREATE DATABASE simulacro;

--Comprobamos que se ha creado correctamente
SHOW DATABASES;
+---------------------+
| Tables_in_simulacro |
+---------------------+
| pieza               |
+---------------------+

--Usamos la base de datos
USE simulacro;

--Creamos la tabla pieza
CREATE TABLE pieza(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(100),
	descripcion VARCHAR(100),
	imagen VARCHAR(100),
	url VARCHAR(100),
	id_categoria INT
);

--Nos aseguramos de que se ha creado y que esta correcto
SHOW TABLES;
DESCRIBE pieza;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| descripcion   | varchar(100) | YES  |     | NULL    |                |
| imagen        | varchar(100) | YES  |     | NULL    |                |
| url           | varchar(100) | YES  |     | NULL    |                |
| id_categoria  | int          | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

--Creamos la tabla categoria
CREATE TABLE categoria(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(100),
	descripcion TEXT
);

--Nos aseguramos de que se ha creado y que esta correcto
SHOW TABLES;
DESCRIBE categoria;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| descripcion   | text         | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

--Foreign key
ALTER TABLE pieza
ADD CONSTRAINT categoria_a_entrada
FOREIGN KEY (id_categoria)
REFERENCES categoria(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

--Creamos una vista
--El AS es para cambiar el nombre del campo para que no se repita
CREATE VIEW vista_piezas AS
SELECT 
pieza.titulo AS titulo_pieza, 
pieza.descripcion AS descripcion_pieza, 
pieza.imagen,
categoria.titulo AS titulo_categoria, 
categoria.descripcion AS descripcion_categoria
FROM pieza
LEFT JOIN categoria
ON pieza.id_categoria = categoria.identificador;

--Comprovamos
DESCRIBE vista_piezas;
+-----------------------+--------------+------+-----+---------+-------+
| Field                 | Type         | Null | Key | Default | Extra |
+-----------------------+--------------+------+-----+---------+-------+
| titulo_pieza          | varchar(100) | YES  |     | NULL    |       |
| descripcion_pieza     | varchar(100) | YES  |     | NULL    |       |
| imagen                | varchar(100) | YES  |     | NULL    |       |
| titulo_categoria      | varchar(100) | YES  |     | NULL    |       |
| descripcion_categoria | text         | YES  |     | NULL    |       |
+-----------------------+--------------+------+-----+---------+-------+

--Insertamos en categoria
INSERT INTO categoria VALUES(
	NULL,
	"Categoria A", 
	"Descripción de la categoría A, que puede incluir información sobre qué tipo de piezas pertenecen a esta categoría."
);

--Comprovamos
SELECT * FROM categoria;
+---------------+-------------+-------------------------------------------------------------------------------------------------------------------------+
| identificador | titulo      | descripcion                                                                                                             |
+---------------+-------------+-------------------------------------------------------------------------------------------------------------------------+
|             1 | Categoria A | Descripción de la categoría A, que puede incluir información sobre qué tipo de piezas pertenecen a esta categoría.      |
+---------------+-------------+-------------------------------------------------------------------------------------------------------------------------+

--Insertamos en pieza
INSERT INTO pieza VALUES(
	NULL,
	"Pieza A",
	"Descripcion de la pieza A",
	"imagen_a.jpg",
	"http://example.com/pieza-a",
	1
);

--Comprovamos
SELECT * FROM pieza;
+---------------+---------+---------------------------+--------------+----------------------------+--------------+
| identificador | titulo  | descripcion               | imagen       | url                        | id_categoria |
+---------------+---------+---------------------------+--------------+----------------------------+--------------+
|             1 | Pieza A | Descripcion de la pieza A | imagen_a.jpg | http://example.com/pieza-a |            1 |
+---------------+---------+---------------------------+--------------+----------------------------+--------------+

--Comprovamos vista
SELECT * FROM vista_piezas;
+--------------+---------------------------+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------+
| titulo_pieza | descripcion_pieza         | imagen       | titulo_categoria | descripcion_categoria                                                                                                   |
+--------------+---------------------------+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------+
| Pieza A      | Descripcion de la pieza A | imagen_a.jpg | Categoria A      | Descripción de la categoría A, que puede incluir información sobre qué tipo de piezas pertenecen a esta categoría.      |
+--------------+---------------------------+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------+


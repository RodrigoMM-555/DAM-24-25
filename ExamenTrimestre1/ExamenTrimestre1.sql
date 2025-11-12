'''
Rodrigo Menendez Molina
Examen trimestre 1 v0.1
Portafolio piezas y categorias
'''

--Iniciamos sesion en mysql
sudo mysql -u root -p

--Mostramos las bases de datos
SHOW DATABASES;

--Creamos la base de datos que usaremos
CREATE DATABASES portafolioexamen;

--Usamos la base de datos
USE portafolioexamen;

--Creamos la tabla de piezas
CREATE TABLE piezasportafolio(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(50),
	descripcion TEXT,
	fecha VARCHAR(50),
	id_categoria INT
);

--Mostramos la tabla
DESCRIBE piezasportafolio;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| identificador | int         | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(50) | YES  |     | NULL    |                |
| descripcion   | text        | YES  |     | NULL    |                |
| fecha         | varchar(50) | YES  |     | NULL    |                |
| id_categoria  | int         | YES  |     | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

--Creamos la tabla de categorias
CREATE TABLE categoriasportafolio(
	identificador INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(50)
);

--Mostramos la tabla
DESCRIBE categoriasportafolio;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| identificador | int         | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(50) | YES  |     | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
2 rows in set (0.01 sec)

--Clave foranea
ALTER TABLE piezasportafolio
ADD CONSTRAINT categoria_a_piezas
FOREIGN KEY (id_categoria)
REFERENCES categoriasportafolio(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

--Insertamos en categorias
INSERT INTO categoriasportafolio VALUES(
	NULL,
	"Categoria A"
);

INSERT INTO categoriasportafolio VALUES(
	NULL,
	"Categoria B"
);


--Mostramos la inserción
SELECT * FROM categoriasportafolio;
+---------------+-------------+
| identificador | nombre      |
+---------------+-------------+
|             1 | Categoria A |
|             2 | Categoria B |
+---------------+-------------+
2 rows in set (0.00 sec)

--Insertamos en piezas
INSERT INTO piezasportafolio VALUES(
	NULL,
	"Pieza 1",
	"Descripcion de la pieza 1",
	"10/11/2025",
	1
);

INSERT INTO piezasportafolio VALUES(
	NULL,
	"Pieza 2",
	"Descripcion de la pieza 2",
	"10/11/2025",
	2
);

--Mostramos la inserción
SELECT * FROM piezasportafolio;
+---------------+---------+---------------------------+------------+--------------+
| identificador | titulo  | descripcion               | fecha      | id_categoria |
+---------------+---------+---------------------------+------------+--------------+
|             1 | Pieza 1 | Descripcion de la pieza 1 | 10/11/2025 |            1 |
|             2 | Pieza 2 | Descripcion de la pieza 2 | 10/11/2025 |            2 |
+---------------+---------+---------------------------+------------+--------------+
2 rows in set (0.00 sec)

--Creamos la peticion cruzada y su vista
CREATE VIEW vista_piezas AS
SELECT 
piezasportafolio.titulo, piezasportafolio.descripcion, piezasportafolio.fecha,
categoriasportafolio.nombre
FROM piezasportafolio
LEFT JOIN categoriasportafolio
ON piezasportafolio.id_categoria = categoriasportafolio.identificador;

--Mostramos la peticion cruzada
SELECT * FROM vista_piezas;
+---------+---------------------------+------------+-------------+
| titulo  | descripcion               | fecha      | nombre      |
+---------+---------------------------+------------+-------------+
| Pieza 1 | Descripcion de la pieza 1 | 10/11/2025 | Categoria A |
| Pieza 2 | Descripcion de la pieza 2 | 10/11/2025 | Categoria B |
+---------+---------------------------+------------+-------------+
2 rows in set (0.00 sec)

--Para actualizar
UPDATE piezasportafolio
SET titulo = "Pieza x"
WHERE identificador = 2;

SELECT * FROM piezasportafolio;
+---------------+---------+---------------------------+------------+--------------+
| identificador | titulo  | descripcion               | fecha      | id_categoria |
+---------------+---------+---------------------------+------------+--------------+
|             1 | Pieza 1 | Descripcion de la pieza 1 | 10/11/2025 |            1 |
|             2 | Pieza x | Descripcion de la pieza 2 | 10/11/2025 |            2 |
+---------------+---------+---------------------------+------------+--------------+
2 rows in set (0.00 sec)

--Para borrar registros
DELETE FROM piezasportafolio
WHERE identificador = 2;

SELECT * FROM piezasportafolio;
+---------------+---------+---------------------------+------------+--------------+
| identificador | titulo  | descripcion               | fecha      | id_categoria |
+---------------+---------+---------------------------+------------+--------------+
|             1 | Pieza 1 | Descripcion de la pieza 1 | 10/11/2025 |            1 |
+---------------+---------+---------------------------+------------+--------------+
1 row in set (0.00 sec)

--Crear un usuario con todos los permisos para la base de datos
--Creamos un usuario
CREATE USER 
'Trimestral1'@'localhost' 
IDENTIFIED  BY 'Trimestral123$';
GRANT USAGE ON *.* TO 'Trimestral1'@'localhost';
ALTER USER 'Trimestral1'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

--Le damos todos los permisos
GRANT ALL PRIVILEGES ON `portafolioexamen`.* 
TO 'Trimestral1'@'localhost';

--Recargamos los permisos 
FLUSH PRIVILEGES;

--Añadimos una columna de imagenes para el ejercicio de proyecto intermodular
ALTER TABLE piezasportafolio
ADD COLUMN imagen VARCHAR(100);

--Lo mismo para la vista
DROP View vista_piezas;

CREATE VIEW vista_piezas AS
SELECT 
piezasportafolio.titulo, piezasportafolio.descripcion, piezasportafolio.fecha,
categoriasportafolio.nombre, piezasportafolio.imagen
FROM piezasportafolio
LEFT JOIN categoriasportafolio
ON piezasportafolio.id_categoria = categoriasportafolio.identificador;
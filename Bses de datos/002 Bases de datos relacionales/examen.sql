--Crear y usar base de datos
CREATE DATABASE biblioteca25;
USE biblioteca25;
SELECT DATABASE();
+--------------+
| DATABASE()   |
+--------------+
| biblioteca25 |
+--------------+
1 row in set (0.00 sec)

--Crear tabala autores
CREATE TABLE autores(
	id 	INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(100)NOT NULL,
	pais VARCHAR(80) NULL
);
--Comprovacion de tabla
DESCRIBE autores;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nombre | varchar(100) | NO   |     | NULL    |                |
| pais   | varchar(80)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)


--Crear tabla libros
CREATE TABLE libros(
	id 	INT AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(200) NOT NULL,
	isbn VARCHAR(20) NOT NULL UNIQUE,
	precio DECIMAL(8,2) NOT NULL CHECK(precio >= 0),
	autor_id INT NOT NULL,
	INDEX idx_titulo (titulo)			--Creamos el indice
);

--FK de autor id
ALTER TABLE libros                  -- Altera la tabla de emails
ADD CONSTRAINT fk_libros_autor
FOREIGN KEY (autor_id)              -- Creamos una clave hacia persona
REFERENCES autores(id)				-- que referencia el identificador
ON UPDATE CASCADE                   -- Cuando elimines, cascada
ON DELETE RESTRICT;                  

--Comprovacion de tabla libros
DESCRIBE libros;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(200) | NO   | MUL | NULL    |                |
| isbn     | varchar(20)  | NO   | UNI | NULL    |                |
| precio   | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   | MUL | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

--Comprovacion del indice de libros
SHOW INDEX FROM libros;
+--------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table  | Non_unique | Key_name        | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+--------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| libros |          0 | PRIMARY         |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          0 | isbn            |            1 | isbn        | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          1 | idx_titulo      |            1 | titulo      | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          1 | fk_libros_autor |            1 | autor_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+--------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
4 rows in set (0.02 sec)

--Tabla de socios
CREATE TABLE socios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    CHECK (email LIKE '%_@__%.__%'),
    fecha_alta DATE NOT NULL DEFAULT (CURRENT_DATE)
);
--Comprovacion de tabla
DESCRIBE socios;
+------------+--------------+------+-----+-----------+-------------------+
| Field      | Type         | Null | Key | Default   | Extra             |
+------------+--------------+------+-----+-----------+-------------------+
| id         | int          | NO   | PRI | NULL      | auto_increment    |
| nombre     | varchar(100) | NO   |     | NULL      |                   |
| email      | varchar(120) | NO   | UNI | NULL      |                   |
| fecha_alta | date         | NO   |     | curdate() | DEFAULT_GENERATED |
+------------+--------------+------+-----+-----------+-------------------+
4 rows in set (0.01 sec)


--Tabla de prestamos
CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    socio_id INT NOT NULL,
    libro_id INT NOT NULL,
    fecha_prestamo DATE NOT NULL DEFAULT (CURRENT_DATE),
    fecha_devolucion DATE NULL,
    INDEX idx_socio_libro (socio_id, libro_id),
    CHECK (fecha_devolucion IS NULL OR fecha_devolucion >= fecha_prestamo)
);

--FK de socios y lobros id
ALTER TABLE prestamos
ADD CONSTRAINT fk_prestamos_socio
FOREIGN KEY (socio_id)
REFERENCES socios(id)
ON UPDATE CASCADE
ON DELETE CASCADE;                

ALTER TABLE prestamos
ADD CONSTRAINT fk_prestamos_libro
FOREIGN KEY (libro_id)
REFERENCES libros(id)
ON UPDATE CASCADE
ON DELETE RESTRICT;     

--Comprovacion de la tabla
DESCRIBE prestamos;
+------------------+------+------+-----+-----------+-------------------+
| Field            | Type | Null | Key | Default   | Extra             |
+------------------+------+------+-----+-----------+-------------------+
| id               | int  | NO   | PRI | NULL      | auto_increment    |
| socio_id         | int  | NO   | MUL | NULL      |                   |
| libro_id         | int  | NO   | MUL | NULL      |                   |
| fecha_prestamo   | date | NO   |     | curdate() | DEFAULT_GENERATED |
| fecha_devolucion | date | YES  |     | NULL      |                   |
+------------------+------+------+-----+-----------+-------------------+
5 rows in set (0.00 sec)

--Comprovacion del indice
SHOW INDEX FROM prestamos;
+-----------+------------+--------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table     | Non_unique | Key_name           | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+-----------+------------+--------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| prestamos |          0 | PRIMARY            |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | idx_socio_libro    |            1 | socio_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | idx_socio_libro    |            2 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | fk_prestamos_libro |            1 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+-----------+------------+--------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
4 rows in set (0.02 sec)


--Inserts de autores
INSERT INTO autores VALUES(
	NULL,
	"Isabel Allende",
	"Chile"
);
INSERT INTO autores VALUES(
	NULL,
	"Gabriel García Márquez",
	"Colombia"
);
INSERT INTO autores VALUES(
	NULL,
	"Haruki Murakami",
	"Japón"
);
SELECT * FROM autores;
+----+--------------------------+----------+
| id | nombre                   | pais     |
+----+--------------------------+----------+
|  1 | Isabel Allende           | Chile    |
|  2 | Gabriel García Márquez   | Colombia |
|  3 | Haruki Murakami          | Japón    |
+----+--------------------------+----------+
3 rows in set (0.00 sec)


--Insert de libros
INSERT INTO libros VALUES(
	NULL,
	"La casa de los espíritus",
	"9788401352836",
	15,
	1
);
INSERT INTO libros VALUES(
	NULL,
	"Cien años de soledad",
	"9780307474728",
	15,
	2
);
INSERT INTO libros VALUES(
	NULL,
	"Kafka en la orilla",
	"9788499082478",
	15,
	3
);
SELECT * FROM libros;
+----+---------------------------+---------------+--------+----------+
| id | titulo                    | isbn          | precio | autor_id |
+----+---------------------------+---------------+--------+----------+
|  1 | La casa de los espíritus  | 9788401352836 |  15.00 |        1 |
|  2 | Cien años de soledad      | 9780307474728 |  15.00 |        2 |
|  3 | Kafka en la orilla        | 9788499082478 |  15.00 |        3 |
+----+---------------------------+---------------+--------+----------+
3 rows in set (0.00 sec)


--Insarts de socios
INSERT INTO socios VALUES(
	NULL,
	"Ana Ruiz",
	"ana.ruiz@example.com",
	DEFAULT
);
INSERT INTO socios VALUES(
	NULL,
	"Luis Pérez",
	"luis.perez@example.com",
	DEFAULT
);
SELECT * FROM socios;
+----+-------------+------------------------+------------+
| id | nombre      | email                  | fecha_alta |
+----+-------------+------------------------+------------+
|  1 | Ana Ruiz    | ana.ruiz@example.com   | 2025-10-31 |
|  2 | Luis Pérez  | luis.perez@example.com | 2025-10-31 |
+----+-------------+------------------------+------------+
2 rows in set (0.00 sec)


--Insert de prestamos
INSERT INTO prestamos VALUES(
	NULL,
	1,
	1,
	DEFAULT,
	NULL					--Ponemos NULL porque no se ha devuelto aun
);
INSERT INTO prestamos VALUES(
	NULL,
	2,
	2,
	DEFAULT,
	'2025-10-31'			--Ponemos la fecha de devolución
);

SELECT * FROM prestamos;
+----+----------+----------+----------------+------------------+
| id | socio_id | libro_id | fecha_prestamo | fecha_devolucion |
+----+----------+----------+----------------+------------------+
|  1 |        1 |        1 | 2025-10-31     | NULL             |
|  2 |        2 |        2 | 2025-10-31     | 2025-10-31       |
+----+----------+----------+----------------+------------------+
2 rows in set (0.00 sec)

--Prueba general
SHOW TABLES;
DESCRIBE autores;
DESCRIBE libros;
DESCRIBE socios;
DESCRIBE prestamos;

mysql> SHOW TABLES;
+------------------------+
| Tables_in_biblioteca25 |
+------------------------+
| autores                |
| libros                 |
| prestamos              |
| socios                 |
+------------------------+
4 rows in set (0.00 sec)

mysql> DESCRIBE autores;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nombre | varchar(100) | NO   |     | NULL    |                |
| pais   | varchar(80)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> DESCRIBE libros;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(200) | NO   | MUL | NULL    |                |
| isbn     | varchar(20)  | NO   | UNI | NULL    |                |
| precio   | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   | MUL | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

mysql> DESCRIBE socios;
+------------+--------------+------+-----+-----------+-------------------+
| Field      | Type         | Null | Key | Default   | Extra             |
+------------+--------------+------+-----+-----------+-------------------+
| id         | int          | NO   | PRI | NULL      | auto_increment    |
| nombre     | varchar(100) | NO   |     | NULL      |                   |
| email      | varchar(120) | NO   | UNI | NULL      |                   |
| fecha_alta | date         | NO   |     | curdate() | DEFAULT_GENERATED |
+------------+--------------+------+-----+-----------+-------------------+
4 rows in set (0.00 sec)

mysql> DESCRIBE prestamos;
+------------------+------+------+-----+-----------+-------------------+
| Field            | Type | Null | Key | Default   | Extra             |
+------------------+------+------+-----+-----------+-------------------+
| id               | int  | NO   | PRI | NULL      | auto_increment    |
| socio_id         | int  | NO   | MUL | NULL      |                   |
| libro_id         | int  | NO   | MUL | NULL      |                   |
| fecha_prestamo   | date | NO   |     | curdate() | DEFAULT_GENERATED |
| fecha_devolucion | date | YES  |     | NULL      |                   |
+------------------+------+------+-----+-----------+-------------------+
5 rows in set (0.00 sec)

SELECT User, Host FROM mysql.user WHERE User='lector_ro';
Empty set (0.00 sec)


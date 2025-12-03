--Priemro creamos y usamos la base de datos
CREATE DATABASE videojuegos;
USE videojuegos;

--Luego creamos la tabla y designamos los tipos de datos de cada caracteristica
CREATE TABLE jugadores (
    id_jugador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20),
    edad INT
);

--Por ultimo añadimos los jugadores
INSERT INTO jugadores VALUES(
	NULL,
	"AjaGamer",
	18
);

INSERT INTO jugadores VALUES(
	NULL,
	"OjoGamer",
	20
);

INSERT INTO jugadores VALUES(
	NULL,
	"EjeGamer",
	23
);

--Y comprovamos el resultado
SELECT * FROM jugadores;
+------------+----------+------+
| id_jugador | nombre   | edad |
+------------+----------+------+
|          1 | AjaGamer |   18 |
|          2 | OjoGamer |   20 |
|          3 | EjeGamer |   23 |
+------------+----------+------+
3 rows in set (0.00 sec)


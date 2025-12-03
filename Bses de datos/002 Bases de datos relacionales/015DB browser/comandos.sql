CREATE TABLE "clientes" (
	"identificador"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
-----------------------------------------------------
CREATE TABLE "productos" (
	"identificador"	INTEGER,
	"nombre"	TEXT,
	"descripcion"	TEXT,
	"precio"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
---------------------------------------------------
INSERT INTO clientes VALUES(
	NULL,
	'Rodrigo',
	'Menendez Molina',
	'aja@gmail.com'
);
----------------------------------------------------
SELECT * FROM clientes;
----------------------------------------------
UPDATE clientes
SET email = "ojo@gmail.com"
WHERE identificador = 1;
----------------------------------------------
DELETE FROM clientes
WHERE identificador = 1;

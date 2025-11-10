006Comandos basicos CRUD

--Insert			#Meter los valores en la tabla
INSERT INTO clientes VALUES(
	"12345678A",
	"Rodrigo",
	"Menendez",
	"aja@gmail.com"
);	

+----------------------+
| Tables_in_empresaDAM |
+----------------------+
| clientes             |
+----------------------+
1 row in set (0.00 sec)


--Read				#Mostrar los valores de la tabla
SELECT * FROM clientes;

+-----------+---------+-----------+---------------+
| dni       | nombre  | apellidos | email         |
+-----------+---------+-----------+---------------+
| 12345678A | Rodrigo | Menendez  | aja@gmail.com |
+-----------+---------+-----------+---------------+
1 row in set (0.00 sec)


--Describe			#Muestra lso tipos de valores de cada elemento de la tabla
Describe clientes;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| dni       | varchar(9)   | YES  |     | NULL    |       |
| nombre    | varchar(20)  | YES  |     | NULL    |       |
| apellidos | varchar(255) | YES  |     | NULL    |       |
| email     | varchar(100) | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
4 rows in set (0.00 sec)



--Update			#Cambiar los valores de la tabla de un lugar concreto
UPDATE clientes
SET dni = "11111111A"
WHERE nombre = "Rodrigo";

SELECT * FROM clientes;

+-----------+---------+-----------+---------------+
| dni       | nombre  | apellidos | email         |
+-----------+---------+-----------+---------------+
| 11111111A | Rodrigo | Menendez  | aja@gmail.com |
+-----------+---------+-----------+---------------+
1 row in set (0.00 sec)

UPDATE clientes
SET apellidos = "Molina"
WHERE nombre = "Rodrigo";

SELECT * FROM clientes;

+-----------+---------+-----------+---------------+
| dni       | nombre  | apellidos | email         |
+-----------+---------+-----------+---------------+
| 11111111A | Rodrigo | Molina    | aja@gmail.com |
+-----------+---------+-----------+---------------+
1 row in set (0.00 sec)


--Delete			#Borrar los datos de la tabla
DELETE FROM clientes
WHERE dni = "11111111A";





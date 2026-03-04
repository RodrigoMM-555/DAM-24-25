
CREATE TABLE jugadores(
	dni VARCHAR(9),
	nombre VARCHAR(20),		
	apellidos VARCHAR(255),
	email VARCHAR(100)
);

INSERT INTO jugadores VALUES(
	"98765432Z",
	"Ana María",
	"García López",
	"ana.garcia@example.com"
);	

mysql> select * from jugadores;
+-----------+------------+----------------+------------------------+
| dni       | nombre     | apellidos      | email                  |
+-----------+------------+----------------+------------------------+
| 98765432Z | Ana María  | García López   | ana.garcia@example.com |
+-----------+------------+----------------+------------------------+
1 row in set (0.01 sec)



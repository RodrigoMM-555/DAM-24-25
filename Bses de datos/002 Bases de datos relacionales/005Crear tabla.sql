Crear tabla

SHOW TABLES;

#El valor maximo en MySQL es 255
CREATE TABLE clientes(
	dni VARCHAR(9),
	nombre VARCHAR(20),		
	apellidos VARCHAR(255),
	email VARCHAR(100)
);

SHOW TABLES;
#Esta es la respuesta
+----------------------+
| Tables_in_empresaDAM |
+----------------------+
| clientes             |
+----------------------+
1 row in set (0.00 sec)


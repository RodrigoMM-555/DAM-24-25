--sudo mysql -u root -p

--Seleccionamos base de datos
SHOW DATABASES:
USE clientes;

--Selecciones basicas
SELECT nombre FROM clientes;
SELECT * FROM clientes;

--Podemos operar comparaciones (0 es no, 1 es si)
SELECT nombre, apellidos, edad, edad<30 AS "Es menor de 30" FROM clientes;

SELECT nombre, apellidos, edad, 
edad < 30 AS "Menor de 30",
edad >= 30 && edad <= 40 AS "Entre 30 y 40 años",
edad > 40 AS "Mayor de 40"
FROM clientes;



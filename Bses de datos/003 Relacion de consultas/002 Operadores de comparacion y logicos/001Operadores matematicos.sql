--sudo mysql -u root -p

--Seleccionamos base de datos
SHOW DATABASES:
USE clientes;

--Selecciones basicas
SELECT nombre FROM clientes;
SELECT * FROM clientes;

--Podemos operar matematicamente
SELECT nombre, apellidos, edad+500 FROM clientes;
SELECT nombre, apellidos, edad-500 FROM clientes;
SELECT nombre, apellidos, edad*500 FROM clientes;
SELECT nombre, apellidos, edad/500 FROM clientes;




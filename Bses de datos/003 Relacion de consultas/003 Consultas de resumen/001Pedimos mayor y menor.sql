-- sudo mysql -u root -p

--Entramos en la BD
USE clientes;

--Numero de nombres que tenemos en la BD
SELECT COUNT(nombre)
FROM clientes;

--Cliente más joven
SELECT 
nombre, apellidos, edad
FROM clientes
ORDER BY edad ASC
LIMIT 1;

--Cliente mas viejo
SELECT 
nombre, apellidos, edad
FROM clientes
ORDER BY edad DESC
LIMIT 1;



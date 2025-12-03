--Select normal, de todas las columnas. El asterisco selecciona todo
SELECT * FROM clientes;

--Select controlado, da lo mismo que el de arriba
SELECT
nombre,
apellidos,
edad
FROM
clientes;

--Select de solo dos columnas
SELECT
nombre,
edad
FROM
clientes;

--Select con nombre, no se modifica solo se muestra con otro nombre.
SELECT
nombre AS "Nombre del cliente",
apellidos AS "Apellidos del cliente",
edad AS "Edad del cliente"
FROM
clientes;

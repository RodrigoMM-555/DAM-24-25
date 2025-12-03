SELECT
nombre AS "Nombre del cliente",
apellidos AS "Apellidos del cliente",
edad AS "Edad del cliente"
FROM
clientes
--Se ordenara por apellidos
ORDER BY
apellidos;

--Si no especificamos sera ascendiente por defecto(A,B,C...)
--Es una buena prteactica pese a que es ascendiente por defecto especificarlo
SELECT
nombre AS "Nombre del cliente",
apellidos AS "Apellidos del cliente",
edad AS "Edad del cliente"
FROM
clientes

ORDER BY
apellidos ASC;

--Tambien existe el descndiente
SELECT
nombre AS "Nombre del cliente",
apellidos AS "Apellidos del cliente",
edad AS "Edad del cliente"
FROM
clientes

ORDER BY
edad DESC;

--Se puede ordenar por varias columnas
SELECT
nombre AS "Nombre del cliente",
apellidos AS "Apellidos del cliente",
edad AS "Edad del cliente"
FROM
clientes

ORDER BY
edad DESC,
apellidos ASC;
--Primero los ordena por edad y si hay dos iguales los ordena po apellidos.

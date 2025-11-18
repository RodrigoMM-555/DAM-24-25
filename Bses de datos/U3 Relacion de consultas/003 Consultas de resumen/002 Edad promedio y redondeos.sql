
--Edad promedio
SELECT 
AVG(edad)
FROM clientes;

--Redondeo normal
SELECT 
ROUND(AVG(edad))
FROM clientes;

--Redondeo al alta
SELECT 
CEIL(AVG(edad))
FROM clientes;

--Redondeo a la baja
SELECT 
FLOOR(AVG(edad))
FROM clientes;

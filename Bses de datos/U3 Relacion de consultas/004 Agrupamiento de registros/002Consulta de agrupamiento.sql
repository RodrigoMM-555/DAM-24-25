--Cantidad de colores
SELECT COUNT(color)
FROM productos;

--Juntamos por colores
SELECT COUNT(color), color
FROM productos
GROUP BY color;

--Ordenamos
SELECT COUNT(color), color
FROM productos
GROUP BY color
ORDER BY COUNT(color) ASC;


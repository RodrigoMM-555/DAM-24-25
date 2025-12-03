
CREATE VIEW personas_correos AS

SELECT
emails.direccion,
personas.nombre,
personas.apellidos
FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;

--Hemos creado una tabla con la que ver la combinacionde otras dos
--esta tabla es de solo lectura, no se puede editar, 
SELECT * FROM personas_correos;

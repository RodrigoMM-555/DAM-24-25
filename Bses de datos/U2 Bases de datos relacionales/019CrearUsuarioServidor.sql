
-- crea usuario (Rodrigo) nuevo con contraseña (Perepe) y el servidor ()
--si el servidor es localhos quiere decir que tiene los archivos py al lado

CREATE USER 
'Rodrigo'@'localhost' 
IDENTIFIED  BY 'Abcdefg_55';

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'Rodrigo'@'localhost';

-- quitale todos los limites que tenga
ALTER USER 'Rodrigo'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `empresaDAM`.* 
TO 'Rodrigo'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
